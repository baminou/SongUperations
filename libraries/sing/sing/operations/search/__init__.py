
from ...operation_types.SingOperationType import Singoperationtype
from ...operation_types.StudyOperationType import Studyoperationtype
import requests
import json

class Search(Singoperationtype, Studyoperationtype):

    @staticmethod
    def name():
        return "Search"

    @staticmethod
    def description():
        return "Retrieve an analysis"

    def _parser(self, main_parser):
        main_parser.add_argument('-a','--analysis-id',dest='analysis_id', help="Analysis ID to retrieve", required=True)
        return

    def _run(self):
        response = json.dumps(requests.get('%s/studies/%s/analysis/%s' % (self.song_url, self.study, self.args.analysis_id)).json())
        print(response)
        return response