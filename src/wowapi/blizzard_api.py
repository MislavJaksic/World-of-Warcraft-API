from helper.requester import Requester
from entity.blizzard_url import BlizzardUrl, string_to_url
from entity.mount import Mount
from entity.pet import Pet
from entity.pet_ability import PetAbility


class BlizzardApi(object):
    def __init__(self, requester: Requester):
        self.requester = requester

    def __str__(self):
        string = "BlizzardAPI["
        string += str(self.requester)
        string += ", "
        string += str(self.cacher)
        string += "]"
        return string

    def get_pets(self):
        index_url = BlizzardUrl("eu", "/data/wow/pet/index", "static")
        index_json = self.requester.get_json(index_url)

        pets = []
        for pet in index_json["pets"]:
            pet_url = string_to_url(pet["key"]["href"])
            pet_json = self.requester.get_json(pet_url)
            abilities = self.get_pet_abilities(pet_json.get("abilities"))
            pets.append(Pet(pet_json, abilities))

        return pets

    def get_pet_abilities(self, abilities_json):
        abilities = []
        if abilities_json:
            for ability_json in abilities_json:
                print(ability_json)
                abilities.append(PetAbility(ability_json))
        return abilities

    def get_mounts(self):
        index_url = BlizzardUrl("eu", "/data/wow/mount/index", "static")
        index_json = self.requester.get_json(index_url)

        mounts = []
        for mount in index_json["mounts"]:
            mount_url = string_to_url(mount["key"]["href"])
            mount_json = self.requester.get_json(mount_url)
            mounts.append(Mount(mount_json))

        return mounts
