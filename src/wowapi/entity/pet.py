import json
from entity.blizzard_url import string_to_url
from entity.pet_ability import PetAbility
from entity.source import Source
from entity.flags import Flags


class Pet(object):
    def __init__(self, pet_json, abilities):
        self.json = pet_json
        self.url = string_to_url(pet_json["_links"]["self"]["href"])
        self.id = pet_json["id"]
        self.name = pet_json["name"]
        self.battle_pet_type = BattlePetType(pet_json["battle_pet_type"])
        self.description = pet_json["description"]
        self.flags = Flags(
            pet_json["is_capturable"],
            pet_json["is_tradable"],
            pet_json["is_battlepet"],
            pet_json["is_alliance_only"],
            pet_json["is_horde_only"],
        )
        self.abilities = abilities
        self.source = Source(pet_json.get("source"))
        self.icon = pet_json["icon"]  # TODO
        self.creature = string_to_url(pet_json["creature"]["key"]["href"])  # TODO
        self.is_random_creature_display = pet_json["is_random_creature_display"]

    def __str__(self):
        return json.dumps(self.json, indent=1)


class BattlePetType(object):
    def __init__(self, battle_pet_json):
        self.json = battle_pet_json
        self.type = battle_pet_json["type"]
        self.name = battle_pet_json["name"]

    def __str__(self):
        return json.dumps(self.json, indent=1)
