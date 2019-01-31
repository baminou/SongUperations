
from ...operation_types.SingOperationType import Singoperationtype
import requests
import json

class Search(Singoperationtype):

    @staticmethod
    def name():
        return "Search"

    @staticmethod
    def description():
        return "Retrieve an analysis"

    def _parser(self, main_parser):
        main_parser.add_argument('study', help="Study ID")
        main_parser.add_argument('analysis_id', help="Analysis ID to retrieve")
        return

    def _run(self):
        response = json.dumps(requests.get('%s/studies/%s/analysis/%s' % (self.song_server, self.args.study, self.args.analysis_id)).json())
        print(response)
        return response