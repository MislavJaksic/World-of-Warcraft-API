import requests

import secret_keeper


class AppAuth(object):
    def __init__(self):
        self.access_token = ""
        self.token_type = ""
        self.expires_in = 0

    def __str__(self):
        string = "AppAuth["
        string += self.access_token
        string += ", "
        string += self.token_type
        string += ", "
        string += str(self.expires_in)
        string += "]"
        return string

    def refresh(self):
        r = self.request_access_token()
        dict = r.json()

        self.access_token = dict["access_token"]
        self.token_type = dict["token_type"]
        self.expires_in = dict["expires_in"]

    def request_access_token(self):
        url = "https://us.battle.net/oauth/token"
        auth = (secret_keeper.id, secret_keeper.secret)
        data = {"grant_type": "client_credentials"}

        return requests.post(url, auth=auth, data=data)
