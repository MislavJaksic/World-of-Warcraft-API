from enum import Enum, auto


class Source(object):
    def __init__(self, source_json):
        self.json = source_json
        self.type = None
        self.name = None

        if source_json:
            self.type = source_json["type"]
            self.name = source_json["name"]

    def __str__(self):
        return str(self.json)


class SourceType(Enum):
    ACHIEVEMENT = auto()
    VENDOR = auto()
    DROP = auto()
    PROMOTION = auto()
    QUEST = auto()
    PROFESSION = auto()
    WORLDVENT = auto()
    PETSTORE = auto()
    TCG = auto()
