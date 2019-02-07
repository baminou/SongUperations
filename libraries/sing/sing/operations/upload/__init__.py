
from ...operation_types.SingOperationType import Singoperationtype
import json
import requests
import argparse

import os

class Upload(Singoperationtype):

    @staticmethod
    def name():
        return "Upload"

    @staticmethod
    def description():
        return "Upload json payload to song"

    def _parser(self, main_parser):
        main_parser.add_argument('access_token', help="SONG access token")
        main_parser.add_argument('study', help="ICGC study ID")
        main_parser.add_argument('payload', type=argparse.FileType('r'), help="Path to payload.json")
        return

    def _run(self):
        access_token = self.args.access_token
        headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/json','Accept':'application/json'}
        payload = json.dumps(json.load(self.args.payload))

        response = requests.post('%s/upload/%s' % (self.args.song_server,self.args.study),data=payload,headers=headers)

        if response.status_code == 200:
            print(json.dumps(response.json()))
            return response.json()
        else:
            raise Exception(response.json().get('message'))