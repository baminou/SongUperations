
from ...operation_types.SingOperationType import Singoperationtype
import requests
import os
import json

class Save(Singoperationtype):

    @staticmethod
    def name():
        return "Save"

    @staticmethod
    def description():
        return "Save a SONG upload ID."

    def _parser(self, main_parser):
        main_parser.add_argument('access_token', help="SONG access token")
        main_parser.add_argument('study', help="ICGC study ID")
        main_parser.add_argument('upload_id', help="Upload ID")
        return

    def _run(self):
        access_token = self.args.access_token
        response = requests.post('%s/upload/%s/save/%s' % (self.song_server, self.args.study,self.args.upload_id),headers={'Authorization':'Bearer '+access_token})
        if not response.status_code >= 200 and not response.status_code <=204:
            raise Exception(response.text)
        print(json.dumps(response.json()))
        return response.json()