
from ...operation_types.SingOperationType import Singoperationtype
import requests
import json

class Status(Singoperationtype):

    @staticmethod
    def name():
        return "Status"

    @staticmethod
    def description():
        return "Retrieve an upload status"

    def _parser(self, main_parser):
        main_parser.add_argument('study', help="ICGC study ID")
        main_parser.add_argument('upload_id', help="Upload ID")
        return

    def _run(self):
        response = requests.get('%s/upload/%s/status/%s' % (self.song_server,self.args.study,self.args.upload_id))
        if not response.status_code == 201:
            raise Exception(response.text)
        return response.json()