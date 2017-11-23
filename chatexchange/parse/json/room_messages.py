from ._base import ParseJSON


class RoomMessages(ParseJSON):
    def __init__(self, data):
        super().__init__(data)

