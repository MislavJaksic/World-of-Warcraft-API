from time import sleep
import requests
from auth.app_auth import AppAuth
from helper.file_cacher import FileCacher
from entity.blizzard_url import BlizzardUrl


def throttle(seconds):
    def throttle_decorator(func):
        sleep(seconds)
        return func

    return throttle_decorator


class Requester(object):
    def __init__(self, app_auth: AppAuth, cacher: FileCacher):
        self.app_auth = app_auth
        self.cacher = cacher

    def __str__(self):
        string = "Requester["
        string += str(self.app_auth)
        string += "]"
        return string

    def get_json(self, url: BlizzardUrl):
        filename = self.url_to_filename(url)
        if (self.cacher.is_file_exists(filename)):
            response = self.cacher.from_file(filename)
        else:
            response = self.get_response(url)
            if (response.status_code == 200):
                self.cacher.object_to_file(response, filename)

        return response.json()

    def url_to_filename(self, url: BlizzardUrl):
        filename = str(url)
        filename = filename.replace("https://", "")
        filename = filename.replace("?", "-")
        filename = filename.replace("/", "-")
        filename = filename.replace(".", "-")
        filename = filename.replace("=", "-")
        return filename

    @throttle(0.01)
    def get_response(self, url: BlizzardUrl):
        access_token = self.app_auth.access_token
        headers = {"Authorization": f"Bearer {access_token}"}

        return requests.get(str(url), headers=headers)
