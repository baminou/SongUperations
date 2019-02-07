
from ...operation_types.SingOperationType import Singoperationtype
from ...operation_types.AccessTokenOperationType import Accesstokenoperationtype
from ...operation_types.StudyOperationType import Studyoperationtype
import json
import requests
import argparse

class Upload(Singoperationtype, Accesstokenoperationtype, Studyoperationtype):

    @staticmethod
    def name():
        return "Upload"

    @staticmethod
    def description():
        return "Upload json payload to song"

    def _parser(self, main_parser):
        main_parser.add_argument('-p','--payload',dest='payload', type=argparse.FileType('r'), help="Path to payload.json", required=True)
        return

    def _run(self):
        headers={'Authorization':'Bearer '+self.access_token,'Content-Type':'application/json','Accept':'application/json'}
        payload = json.dumps(json.load(self.args.payload))

        response = requests.post('%s/upload/%s' % (self.song_url,self.study),data=payload,headers=headers)

        if response.status_code == 200:
            print(json.dumps(response.json()))
            return response.json()
        else:
            raise Exception(response.json().get('message'))