import logging

from . import _utils


logger = logging.getLogger(__name__)


class User(object):
    def __init__(self, id, client):
        self.id = id
        self._logger = logger.getChild('User')
        self._client = client

    name = _utils.LazyFrom('fetch_from_api')
    about = _utils.LazyFrom('fetch_from_api')
    is_moderator = _utils.LazyFrom('fetch_from_api')
    reputation = _utils.LazyFrom('fetch_from_api')

    message_count = _utils.LazyFrom('scrape_profile')
    room_count = _utils.LazyFrom('scrape_profile')
    last_seen = _utils.LazyFrom('scrape_profile')
    last_message = _utils.LazyFrom('scrape_profile')

    def fetch_from_api(self):
        data = self._client._br.get_user_from_api(self.id)

        self.name = data['name']
        self.about = data['about']
        self.is_moderator = data['is_moderator']
        self.reputation = data['reputation']

    def scrape_profile(self):
        data = self._client._br.get_profile(self.id)

        self.name = data['name']
        self.is_moderator = data['is_moderator']
        self.message_count = data['message_count']
        self.room_count = data['room_count']
        self.reputation = data['reputation']
        self.last_seen = data['last_seen']
        self.last_message = data['last_message']
