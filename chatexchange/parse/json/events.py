from ._base import ParseJSON



class RoomMessages(ParseJSON):
    def __init__(self, data):
        super().__init__(data)

        self.messages = [Event(e) for e in self._data['events']]


class WSEvents(ParseJSON):
    def __init__(self, data):
        super().__init__(data)

        self.events = []

        for room_update in self._data.values():
            for e in room_update.get('e', []):
                self.events.append(Event(e))


class Event(ParseJSON):
    _subclasses = {}
    type_id = None

    @classmethod
    def _register_subclass(cls, other):
        cls._subclasses[other.type_id] = other
        return other

    def __new__(cls, data):
        type_id = data.get('event_type')
        typed_cls = cls._subclasses.get(type_id)
        if typed_cls and typed_cls != cls:
            return typed_cls(data)

        return super().__new__(cls)


@Event._register_subclass
class MessagePosted(Event):
    type_id = 1


@Event._register_subclass
class MessageEdited(Event):
    type_id = 2


@Event._register_subclass
class UserEntered(Event):
    type_id = 3


@Event._register_subclass
class UserLeft(Event):
    type_id = 4


@Event._register_subclass
class RoomNameChanged(Event):
    type_id = 5


@Event._register_subclass
class MessageStarred(Event):
    type_id = 6


@Event._register_subclass
class InternalEvent7(Event):
    type_id = 7


@Event._register_subclass
class UserMentioned(Event):
    type_id = 8


@Event._register_subclass
class MessageFlagged(Event):
    type_id = 9


@Event._register_subclass
class MessageDeleted(Event):
    type_id = 10


@Event._register_subclass
class FileAdded(Event):
    type_id = 11


@Event._register_subclass
class MessageFlaggedForModerator(Event):
    type_id = 12


@Event._register_subclass
class UserSettingsChanged(Event):
    type_id = 13


@Event._register_subclass
class GlobalNotification(Event):
    type_id = 14


@Event._register_subclass
class AccessLevelChanged(Event):
    type_id = 15


@Event._register_subclass
class UserNotification(Event):
    type_id = 16


@Event._register_subclass
class Invitation(Event):
    type_id = 17


@Event._register_subclass
class MessageReply(Event):
    type_id = 18


@Event._register_subclass
class MessageMovedOut(Event):
    type_id = 19


@Event._register_subclass
class MessageMovedIn(Event):
    type_id = 20


@Event._register_subclass
class TimeBreak(Event):
    type_id = 21


@Event._register_subclass
class FeedTicker(Event):
    type_id = 22


@Event._register_subclass
class InternalEvent23(Event):
    type_id = 23


@Event._register_subclass
class InternalEvent24(Event):
    type_id = 24


@Event._register_subclass
class InternalEvent25(Event):
    type_id = 25


@Event._register_subclass
class InternalEvent26(Event):
    type_id = 26


@Event._register_subclass
class InternalEvent27(Event):
    type_id = 27


@Event._register_subclass
class InternalEvent28(Event):
    type_id = 28


@Event._register_subclass
class UserSuspended(Event):
    type_id = 29


@Event._register_subclass
class UserMerged(Event):
    type_id = 30


@Event._register_subclass
class InternalEvent31(Event):
    type_id = 31


@Event._register_subclass
class InternalEvent32(Event):
    type_id = 32


@Event._register_subclass
class InternalEvent33(Event):
    type_id = 33


@Event._register_subclass
class UserNameOrAvatarChanged(Event):
    type_id = 34


@Event._register_subclass
class InternalEvent35(Event):
    type_id = 35
