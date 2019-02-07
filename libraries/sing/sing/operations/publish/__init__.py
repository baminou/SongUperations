
from ...operation_types.SingOperationType import Singoperationtype
from ...operation_types.AccessTokenOperationType import Accesstokenoperationtype
from ...operation_types.StudyOperationType import Studyoperationtype
import requests
import json

class Publish(Singoperationtype, Accesstokenoperationtype, Studyoperationtype):

    @staticmethod
    def name():
        return "Publish"

    @staticmethod
    def description():
        return "Publish an analysis"

    def _parser(self, main_parser):
        main_parser.add_argument('-a','--analysis-id',dest='analysis_id', help="Analysis ID", required=True)
        return

    def _run(self):
        response = requests.put('%s/studies/%s/analysis/publish/%s' % (self.song_url,self.study,self.args.analysis_id),headers={'Authorization':'Bearer '+self.access_token,'Content-Type':'application/json','Accept':'application/json'})

        if not response.status_code == 201:
            raise Exception(response.json().get('message'))

        print(json.dumps(response.json()))

        return response.json()