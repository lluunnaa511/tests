# -*- coding: utf-8 -*-
import requests
from requests import sessions
from requests.auth import HTTPBasicAuth
import json


class ConnectWiKi:
    def __init__(self, username, password):
        self.url = "https://wiki.navercorp.com/rest/api/content"
        self.username = username
        self.pwd = password

    def UpdateLabels(self, data, pageid):
        url = self.url + '/' + pageid + '/label'

        auth = HTTPBasicAuth(self.username, self.pwd)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps(data)
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return response.status_code, response.text

    def getContent(self, id):
        if not id:
            url = self.url
        else:
            url = self.url + "/" + id

        auth = HTTPBasicAuth(self.username, self.pwd)

        headers = {
            "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )

        return response.status_code, response.text, (
            json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    def getContentByTitle(self, title, spaceKey):
        url = self.url + "?title=" + title + "&spaceKey=" + spaceKey
        url = url.replace(" ", "%20")

        auth = HTTPBasicAuth(self.username, self.pwd)

        headers = {
            "Accept": "application/json"
        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )

        return response.status_code, response.text, (
            json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    def postContent(self, data):
        url = self.url

        auth = HTTPBasicAuth(self.username, self.pwd)

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        payload = json.dumps(data)
        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        return response.status_code, response.text

    def deleteContent(self, id):
        url = self.url + '/' + id

        auth = HTTPBasicAuth(self.username, self.pwd)

        response = requests.request(
            "DELETE",
            url,
            auth=auth
        )

        return response.status_code, response.text

    def postAttachment(self, id, files):
        url = self.url + "/" + id + "/child/attachment"

        auth = HTTPBasicAuth(self.username, self.pwd)

        headers = {
            "Accept": "application/json",
            "X-Atlassian-Token": "nocheck"
        }

        status_code = dict()
        with sessions.Session() as session:
            for file in files:
                print('file : ' + file)
                try:
                    f = open(file, "rb")
                    fs = {'file': f}
                    response = session.request(
                        "POST",
                        url,
                        files=fs,
                        headers=headers,
                        auth=auth,
                    )
                    f.close()
                    status_code[file] = str(response.status_code)
                except FileNotFoundError as e:
                    print("Exception : " + e.filename)

        return status_code


def get_file_type(self, file):
    if file.endswith('.png'):
        return 'image/png'
    else:
        return 'text/plain'
