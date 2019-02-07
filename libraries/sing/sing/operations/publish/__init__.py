
from ...operation_types.SingOperationType import Singoperationtype
import requests
import os
import json

class Publish(Singoperationtype):

    @staticmethod
    def name():
        return "Publish"

    @staticmethod
    def description():
        return "Publish an analysis"

    def _parser(self, main_parser):
        main_parser.add_argument('access_token', help="Access token variable")
        main_parser.add_argument('study', help="ICGC study ID")
        main_parser.add_argument('analysis_id', help="Analysis ID")
        return

    def _run(self):
        access_token = self.args.access_token
        response = requests.put('%s/studies/%s/analysis/publish/%s' % (self.song_server,self.args.study,self.args.analysis_id),headers={'Authorization':'Bearer '+access_token,'Content-Type':'application/json','Accept':'application/json'})

        if not response.status_code == 201:
            raise Exception(response.json().get('message'))

        print(json.dump(response.json()))

        return response.json()