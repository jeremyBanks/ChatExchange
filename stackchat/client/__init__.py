import asyncio
from contextlib import contextmanager
import logging
import time
import random

import aiohttp
import sqlalchemy.orm

from .. import parse
from ..parse.json import events
from ..data import models, _seed
from .._util import async
from . import _request



logger = logging.getLogger(__name__)


class _HttpClientSession(aiohttp.ClientSession):
    def __init__(self, *a, **kw):
        if 'connector' not in kw:
            kw['connector'] = aiohttp.TCPConnector(limit_per_host=2)
        super().__init__(*a, **kw)

    def _request(self, method, url, **kwargs):
        # see https://stackoverflow.com/a/45590516/1114
        logger.debug('%s %r', method, url)
        return super()._request(method, url, **kwargs)


class _SQLSession(sqlalchemy.orm.session.Session):
    pass


class Client:
    # Defaults used to control caching:
    max_age_now     = float('-inf')
    max_age_current = 60                # one minute until a datum is no longer "current"
    max_age_fresh   = 60 * 60 * 4       # four hours until a datum is no longer "fresh"
    max_age_alive   = 60 * 60 * 24 * 64 # two months until a datum is no longer "alive"
    max_age_dead    = float('inf')

    # These should be function options but we'll just set them here for now:
    desired_max_age = max_age_fresh
    required_max_age = max_age_dead
    offline = False

    def __init__(self, db_path='sqlite:///:memory:', se_email=None, se_password=None):
        self.sql_engine = sqlalchemy.create_engine(db_path)
        if db_path.startswith('sqlite:'):
            self._prepare_sqlite_hacks()
        self._sql_sessionmaker = sqlalchemy.orm.sessionmaker(
            bind=self.sql_engine,
            expire_on_commit=False,
            class_=_SQLSession)
        self._init_db()

        self._web_session = _HttpClientSession(
            read_timeout=20,
            raise_for_status=True)
        self._request_throttle = async.Throttle(interval=0.5)

        self._authenticated = asyncio.ensure_future(self._authenticate(se_email, se_password))
    
    async def _authenticate(self, se_email, se_password):
        so = self.server('so')
        so_fkey = await _request.StackOverflowFKey.request(self, None)
        await _request.StackOverflowLogin.request(self, None, email=se_email, password=se_password, fkey=so_fkey.fkey)
        # XXX: SE/MSE auth is currently broken
        # mse_fkey = await _request.MetaStackExchangeFKey.request(self, None)
        # await _request.MetaStackExchangeLogin.request(self, None, email=se_email, password=se_password, fkey=mse_fkey.fkey)

    def _init_db(self):
        models.Base.metadata.create_all(self.sql_engine)

        with self.sql_session() as sql:
            for row in _seed.data():
                try:
                    sql.add(row)
                    sql.commit()
                except sqlalchemy.exc.IntegrityError:
                    sql.rollback()
                    continue

    def _prepare_sqlite_hacks(self):
        # via http://docs.sqlalchemy.org/en/latest/dialects/sqlite.html

        @sqlalchemy.event.listens_for(self.sql_engine, 'connect')
        def do_connect(dbapi_connection, connection_record):
            # disable pysqlite's emitting of the BEGIN statement entirely.
            # also stops it from emitting COMMIT before any DDL.
            dbapi_connection.isolation_level = None

            # enable foreign key constraint checking
            # XXX: lol it already breaks us
            # cursor = dbapi_connection.cursor()
            # cursor.execute("PRAGMA foreign_keys=ON")
            # cursor.close()

        @sqlalchemy.event.listens_for(self.sql_engine, 'begin')
        def do_begin(conn):
            # emit our own BEGIN
            conn.execute('BEGIN')

    _closed = False
    def close(self):
        if self._closed: raise Exception('already closed')

        self._web_session.close()

        self._closed = True
    
    def __enter__(self):
        return self

    def __exit__(self, *exc_details):
        self.close()

    @contextmanager
    def sql_session(self):
        if self._closed:
            raise Exception('already closed')

        session = self._sql_sessionmaker()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def server(self, slug_or_host):
        with self.sql_session() as sql:
            server = sql.query(Server).filter(
                (models.Server.slug == slug_or_host) |
                (models.Server.host == slug_or_host)).one()
        async def f():
            await self._authenticated
            return await _request.StackChatFKey.request(self, server)

        server.set(
            _client=self,
            _fkey_request=asyncio.ensure_future(f()))
        return server

    @property
    def se(self):
        return self.server('se')

    @property
    def mse(self):
        return self.server('mse')

    @property
    def so(self):
        return self.server('so')


class Server(models.Server):
    _client = None
    _fkey_request = None

    async def me(self):
        await self._client._authenticated

        raise NotImplementedError()

    def _get_or_create_user(self, sql, user_id):
        assert self.meta_id 
        assert user_id
        user = sql.query(User).filter(
            (models.User.server_meta_id == self.meta_id) &
            (models.User.user_id == user_id)
        ).one_or_none()
        if not user:
            user = User(server_meta_id=self.meta_id, user_id=user_id)
            sql.add(user)
            sql.flush()
            assert user.meta_id
        user._server = self
        return user
        
    async def user(self, user_id):
        await self._client._authenticated

        with self._client.sql_session() as sql:
            user = self._get_or_create_user(sql, user_id)

        if user.meta_update_age < self._client.desired_max_age:
            return user

        if not self._client.offline:
            NotImplemented

        if user.meta_update_age <= self._client.required_max_age:
            return user
        
        logger.warning("%s failed to load user %s, %s > %s", self, user_id, user.meta_update_age, self._client.required_max_age)
        return None

    def _get_or_create_room(self, sql, room_id):
        assert self.meta_id 
        assert room_id
        room = sql.query(Room).filter(
            (models.Room.server_meta_id == self.meta_id) &
            (models.Room.room_id == room_id)
        ).one_or_none()
        if not room:
            room = Room(server_meta_id=self.meta_id, room_id=room_id)
            sql.add(room)
            sql.flush()
            assert room.meta_id
        room._server = self
        return room

    async def room(self, room_id):
        await self._client._authenticated

        with self._client.sql_session() as sql:
            room = self._get_or_create_room(sql, room_id)

        if room.meta_update_age < self._client.desired_max_age:
            return room

        if not self._client.offline:
            transcript = await _request.TranscriptDay.request(self._client, self, room_id=room_id)
            room = transcript.room

        if room.meta_update_age <= self._client.required_max_age:
            return room
        
        logger.warning("%s failed to load room %s, %s > %s", self, room_id, room.meta_update_age, self._client.required_max_age)
        return None

    def _get_or_create_message(self, sql, message_id):
        assert self.meta_id 
        assert message_id
        message = sql.query(Message).filter(
            (models.Message.server_meta_id == self.meta_id) &
            (models.Message.message_id == message_id)
        ).one_or_none()
        if not message:
            message = Message(server_meta_id=self.meta_id, message_id=message_id)
            sql.add(message)
            sql.flush()
            assert message.meta_id
        message._server = self
        return message

    async def message(self, message_id):
        await self._client._authenticated

        with self._client.sql_session() as sql:
            message = self._get_or_create_message(sql, message_id)

        if message.meta_update_age < self._client.desired_max_age:
            return message

        if not self._client.offline:
            transcript = await _request.TranscriptDay.request(self._client, self, message_id=message_id)

            message = transcript.messages[message_id]

        if message.meta_update_age <= self._client.required_max_age:
            return message
        
        logger.warning("%s failed to load message %s, %s > %s", self, message_id, message.meta_update_age, self._client.required_max_age)
        return None
    
    async def rooms(self):
        await self._client._authenticated
        logger.warning("Server.rooms() only checks locally for now.")

        rooms = []
        with self._client.sql_session() as sql:
            query = sql.query(Room) \
                .filter(models.Room.server_meta_id == self.meta_id) \
                .order_by(models.Room.server_meta_id)
            for room in query:
                room._server = self
                rooms.append(room)

        return rooms

        raise NotImplementedError()
        response = self._client._web_session.get('https://%s/rooms?tab=all&sort=active&nohide=true' % (self.host))


class User(models.User):
    _server = None

    @property
    def server(self):
        return self._server


class Room(models.Room):
    _server = None

    @property
    def server(self):
        return self._server

    async def old_messages(self):
        await self._server._client._authenticated

        response = await _request.RoomMessages.request(
            self._server._client,
            self._server,
            room_id=self.room_id)

        while True:
            if response.messages:
                messages = list(sorted(response.messages, key=lambda m: -m.message_id))

                for message in messages:
                    yield message
                    
                response = await _request.RoomMessages.request(
                    self._server._client,
                    self._server,
                    room_id=self.room_id,
                    before_message_id=messages[-1].message_id)
            else:
                break
    
    async def new_messages(self):
        await self._server._client._authenticated

        response = await _request.RoomWSAuth.request(
            self._server._client,
            self._server,
            room_id=self.room_id)

        url = response.data._data['url'] + '?l=0' # not sure what this is

        logger.info(url)
        async with self._server._client._web_session.ws_connect(url, headers={'Origin': 'https://chat.stackoverflow.com'}) as socket:
            async for msg in socket:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    parsed = parse.WSEvents(msg.data)
                    for event in parsed.events:
                        if isinstance(event, events.MessagePosted):
                            data = event._data

                            if data['room_id'] != self.room_id:
                                continue

                            with self._server._client.sql_session() as sql:
                                message = self._server._get_or_create_message(sql, data['id'])
                                message.mark_updated()
                                message.content_html = data['content']
                                owner = self._server._get_or_create_user(sql, data['id'])
                                owner.mark_updated()
                                owner.name = data['user_name']
                                message.owner_meta_id = owner.meta_id

                            yield message

    async def send_message(self, content_markdown):
        await self._server._client._authenticated

        response = await _request.SendMessage.request(
            self._server._client,
            self._server,
            room_id=self.room_id,
            text=content_markdown
        )
        
        assert response.id # handle failure for real once we've figured out how to succeed
            


class Message(models.Message):
    _server = None

    @property
    def server(self):
        return self._server

    @property
    def owner(self):
        if self.owner_meta_id:
            with self._server._client.sql_session() as sql:
                user = sql.query(User).filter(models.User.meta_id == self.owner_meta_id).one()
                user._server = self._server
                return user
        else:
            return None

    @property
    def room(self):
        return self._server.room(self.room_id)

    async def replies(self):
        logger.warning("Message.replies() only checks locally for now.")

        with self._server._client.sql_session() as sql:
            messages = list(
                sql.query(Message)
                    .filter(models.Message.parent_message_id == self.message_id)
                    .order_by(models.Message.message_id))
            for message in messages:
                message._server = self._server
            return messages
