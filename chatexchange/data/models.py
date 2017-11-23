import datetime
import hashlib
import hmac

import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Index, Integer,
                        String, UniqueConstraint)

import hashids

from .._util import obj_dict
from ._constants import *

_obfuscation_key = 'adbbf3aa342bc82736d0ee71b2a0650e05b2edd21082e1291ae161777550ba0c71002b9ce3ad7aa19c8a4641223f8f4e82bab7ebbf5335d01046cdc5a462bdfe'


class Base:
    __tablename__ = None

    meta_id = Column(Integer, primary_key=True)
    meta_created = Column(DateTime, default=datetime.datetime.now)
    meta_updated = Column(DateTime, default=EPOCH)
    meta_deleted = Column(DateTime, default=None)

    __init__ = obj_dict.update
    set = obj_dict.updated
    
    __repr__ = obj_dict.repr

    def mark_updated(self):
        self.meta_updated = datetime.datetime.now()

    def mark_deleted(self):
        if self.meta_deleted is None:
            self.meta_deleted = datetime.datetime.now()

    @property
    def meta_update_age(self):
        return (datetime.datetime.now() - self.meta_updated).total_seconds()

    @property
    def meta_slug(self):
        """
        Produces a short obfuscated (NOT SECURE!) slug encoding .meta_id.

        I like to use these so that we have an identifier for these instances
        that is clearly not their official room/message IDs.
        """
        salt = ''.join(chr(n) for n in hmac.new(_obfuscation_key, self.__tablename__, hashlib.sha512).digest())
        min_length = 4
        slugger = hashids.Hashids(salt=salt, min_length=min_length)
        meta_slug ,= slugger.encode(self.meta_id)
        return meta_slug

    @classmethod
    def meta_id_from_meta_slug(cls, meta_slug):
        salt = ''.join(chr(n) for n in hmac.new(_obfuscation_key, cls.__tablename__, hashlib.sha512).digest())
        min_length = 4
        slugger = hashids.Hashids(salt=salt, min_length=min_length)
        meta_id, = slugger.decode(meta_slug)
        return meta_id


Base = sqlalchemy.ext.declarative.declarative_base(cls=Base)


class Server(Base):
    __tablename__ = 'Server'
    meta_id = Column(Integer, primary_key=True)

    name = Column(String)
    host = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    _slug_is_unique = UniqueConstraint('slug')


class User(Base):
    __tablename__ = 'User'
    server_meta_id = Column(Integer, ForeignKey('Server.meta_id'))
    user_id = Column(Integer, nullable=False)

    name = Column(String)
    about = Column(String)
    is_moderator = Column(Boolean)
    message_count = Column(Integer)
    room_count = Column(Integer)
    reputation = Column(Integer)
    last_seen = Column(DateTime)
    last_message = Column(DateTime)

    __table_args__ = (
        Index('ix_server_meta_id_user_id_name', server_meta_id, user_id, name),
        UniqueConstraint('server_meta_id', 'user_id'),
    )


class Room(Base):
    __tablename__ = 'Room'
    server_meta_id = Column(Integer, ForeignKey('Server.meta_id'))

    room_id = Column(Integer, nullable=False)

    name = Column(String)

    default_access = Column(Integer)
    ACCESS_PRIVATE = 0b_00000000
    ACCESS_GALLERY = 0b_00000001
    ACCESS_PUBLIC = 0b_00000011

    __table_args__ = (
        Index('ix_server_meta_id_room_id_name', server_meta_id, room_id, name),
        UniqueConstraint('server_meta_id', 'room_id'),
    )


class Message(Base):
    __tablename__ = 'Message'

    server_meta_id = Column(Integer, ForeignKey('Server.meta_id'))
    room_meta_id = Column(Integer, ForeignKey('Room.meta_id'))
    owner_meta_id = Column(Integer, ForeignKey('User.meta_id'))

    message_id = Column(Integer, nullable=False)

    parent_message_id = Column(Integer, ForeignKey('Message.message_id'), nullable=True)

    content_html = Column(String)
    content_text = Column(String)
    content_markdown = Column(String)

    __table_args__ = (
        Index('ix_server_meta_id_message_id', server_meta_id, message_id),
        Index('ix_parent_message_id_room_meta_id', parent_message_id, room_meta_id),
        Index('ix_room_meta_idowner_meta_id_message_id', room_meta_id, owner_meta_id, message_id),
        Index('ix_owner_meta_id_room_meta_id_message_id', owner_meta_id, room_meta_id, message_id),
        UniqueConstraint('server_meta_id', 'message_id'),
    )
