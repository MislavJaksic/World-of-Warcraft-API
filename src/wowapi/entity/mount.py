import json
from entity.blizzard_url import string_to_url
from entity.source import Source
from entity.faction import Faction


class Mount(object):
    def __init__(self, mount_json):
        self.json = mount_json
        self.url = string_to_url(mount_json["_links"]["self"]["href"])
        self.id = mount_json["id"]
        self.name = mount_json["name"]
        self.creature_display_url = string_to_url(mount_json["creature_displays"][0]["key"]["href"])  # TODO
        self.description = mount_json["description"]
        self.source = Source(mount_json.get("source"))
        self.faction = Faction(mount_json.get("faction"))
        self.should_exclude_if_uncollected = mount_json.get("should_exclude_if_uncollected")

    def __str__(self):
        return json.dumps(self.json, indent=1)
