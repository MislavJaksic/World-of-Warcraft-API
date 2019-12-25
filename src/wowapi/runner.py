"""
    Project-Name.py
    ---------------

    Runs the project.

    :copyrgiht: 2019 MislavJaksic
    :license: MIT License
"""
import sys
import logging
from pathlib import Path

import context
from auth.app_auth import AppAuth
from helper.requester import Requester
from helper.file_cacher import FileCacher
from blizzard_api import BlizzardApi


logging.basicConfig(filename="app.log", filemode="a", format="%(asctime)s - %(message)s", level=logging.DEBUG)


def main(args):
    token = AppAuth()
    cache_path = Path() / "cache"
    cacher = FileCacher(cache_path)
    requester = Requester(token, cacher)
    api = BlizzardApi(requester)

    # mounts = api.get_mounts()
    # for mount in mounts:
    #     print(mount.name)
    #     print("  " + str(mount.source))

    pets = api.get_pets()
    for pet in pets:
        print(pet)

def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
