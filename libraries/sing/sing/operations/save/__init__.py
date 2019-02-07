
from ...operation_types.SingOperationType import Singoperationtype
from ...operation_types.AccessTokenOperationType import Accesstokenoperationtype
from ...operation_types.StudyOperationType import Studyoperationtype
import requests
import os
import json

class Save(Singoperationtype, Studyoperationtype, Accesstokenoperationtype):

    @staticmethod
    def name():
        return "Save"

    @staticmethod
    def description():
        return "Save a SONG upload ID."

    def _parser(self, main_parser):
        main_parser.add_argument('-u','--upload-id',dest='upload_id', help="Upload ID", required=True)
        return

    def _run(self):
        response = requests.post('%s/upload/%s/save/%s' % (self.song_url, self.study,self.args.upload_id),headers={'Authorization':'Bearer '+self.access_token})
        if not response.status_code >= 200 and not response.status_code <=204:
            raise Exception(response.text)
        print(json.dumps(response.json()))
        return response.json()