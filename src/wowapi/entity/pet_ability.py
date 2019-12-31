from entity.blizzard_url import string_to_url


class PetAbility(object):
    def __init__(self, json):
        self.url = string_to_url(json["ability"]["key"]["href"])  # TODO
        self.name = json["ability"]["name"]
        self.id = json["ability"]["id"]
        self.slot = json["slot"]
        self.required_level = json["required_level"]

    def __str__(self):
        string = self.name + ": "
        string += "\n"
        string += "    Slot: " + str(self.slot)
        string += "\n"
        string += "    Level: " + str(self.required_level)
        return string
