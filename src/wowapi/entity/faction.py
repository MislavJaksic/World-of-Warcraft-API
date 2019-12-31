from enum import Enum, auto


class Faction(object):
    def __init__(self, faction_json):
        self.json = faction_json
        self.type = None
        self.name = None

        if faction_json:
            self.type = faction_json["type"]
            self.name = faction_json["name"]

    def __str__(self):
        return str(self.json)


class FactionType(Enum):
    ALLIANCE = auto()
    HORDE = auto()
