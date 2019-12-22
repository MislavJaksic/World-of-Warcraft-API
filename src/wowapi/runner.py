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


logging.basicConfig(filename="output.log", filemode="a", format="%(asctime)s - %(message)s", level=logging.DEBUG)


def main(args):
    token = AppAuth()
    requester = Requester(token)

    cache_path = Path() / "cache"
    cacher = FileCacher(cache_path)
    api = BlizzardApi(requester, cacher)

    pets = api.get_pets()
    for pet in pets:
        print(pet)


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == "__main__":
    run()
