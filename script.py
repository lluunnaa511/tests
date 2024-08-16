# -*- coding: utf-8 -*-
from ConnectWiKi import ConnectWiKi
import json
import datetime
from datetime import timedelta


class MakePostData:
    def __init__(self):
        self.username = 'KRT00314'
        self.password = 'dnadna1!'
        today = datetime.datetime.now() + timedelta(days=1)
        self.postData = {"title": str(today.strftime("%Y-%m-%d")) + ' EQ Sync',
                         "type": "page",
                         "space": {
                             "key": 'DNA'
                         }, "status": "current",
                         "ancestors": [
                             {
                                 "id": '1976140379'
                             }
                         ], "body": {
                                "storage": {
                                    "representation": "storage",
                                    "value": ""
                                }}}
        self.Labels = [
            {"prefix": "global",
             "name": "eq-sync-2024"}]

    def insertBody(self):
        request_top = open("top.html")
        strTop = request_top.read()
        request_body = open("body.html")
        strBody = request_body.read()
        request_bott = open("bottom.html")
        strBott = request_bott.read()

        pages = strTop + strBody + strBott
        self.postData["body"]["storage"]["value"] = pages

    def postContent(self):
        conn = ConnectWiKi(self.username, self.password)
        rescode, restext = conn.postContent(self.postData)
        if rescode == 200:
            id = json.loads((json.dumps(json.loads(restext), sort_keys=True, indent=4, separators=(",", ": "))))["id"]
            return id
        else:
            print(rescode)
            print(restext)

        return ""

    def updateLables(self, pageid):
        conn = ConnectWiKi(self.username, self.password)
        conn.UpdateLabels(self.Labels, pageid)


def run():
    print("***START***")
    conn = MakePostData()
    conn.insertBody()

    print("***POST DATA***")
    wiki_id = conn.postContent()
    print("ID : " + wiki_id)
    conn.updateLables(wiki_id)

    if not id:
        print("failed!!!")
    print("***SUCCESS!!***")


if __name__ == '__main__':
    run()
