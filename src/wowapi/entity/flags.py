class Flags(object):
    def __init__(
        self, is_capturable, is_tradable, is_battlepet, is_alliance_only, is_horde_only
    ):
        self.is_capturable = is_capturable
        self.is_tradable = is_tradable
        self.is_battlepet = is_battlepet
        self.is_alliance_only = is_alliance_only
        self.is_horde_only = is_horde_only

    def __str__(self):
        string = "Flags: "
        string += "\n"
        string += "    is_capturable: " + str(self.is_capturable)
        string += "\n"
        string += "    is_tradable: " + str(self.is_tradable)
        string += "\n"
        string += "    is_battlepet: " + str(self.is_battlepet)
        string += "\n"
        string += "    is_alliance_only: " + str(self.is_alliance_only)
        string += "\n"
        string += "    is_horde_only: " + str(self.is_horde_only)
        return string
