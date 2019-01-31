
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
        main_parser.add_argument('-i','--ignore-collision',dest='ignore_collision',help="Ignore analysis collision",action='store_true')
        return

    def _run(self):
        response = requests.get('%s/upload/%s/status/%s?ignoreAnalysisIdCollisions=%s' % (self.song_server,self.args.study,self.args.upload_id,str(self.args.ignore_collision).lower()))
        if not response.status_code == 200:
            raise Exception(response.text)
        print(json.dumps(response.json()))
        return response.json()