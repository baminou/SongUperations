
from ...operation_types.SingOperationType import Singoperationtype
import requests
import os

class Save(Singoperationtype):

    @staticmethod
    def name():
        return "Save"

    @staticmethod
    def description():
        return "Save a SONG upload ID."

    def _parser(self, main_parser):
        main_parser.add_argument('access_token_variable', help="Access token global variable name")
        main_parser.add_argument('study', help="ICGC study ID")
        main_parser.add_argument('upload_id', help="Upload ID")
        return

    def _run(self):
        access_token = os.environ.get(self.args.access_token_variable)
        response = requests.post('%s/upload/%s/save/%s' % (self.song_server, self.args.study_id,self.args.upload_id),headers={'Authorization':'Bearer '+access_token})
        if not response.status_code == 201:
            raise Exception(response.text)
        return response.json()