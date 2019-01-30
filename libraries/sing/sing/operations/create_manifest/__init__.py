
from ...operation_types.SingOperationType import Singoperationtype
import requests
import os
import argparse

class CreateManifest(Singoperationtype):

    @staticmethod
    def name():
        return "Manifest"

    @staticmethod
    def description():
        return "Generate manifest file for upload"

    def _parser(self, main_parser):
        main_parser.add_argument('study', help="ICGC study ID")
        main_parser.add_argument('analysis_id', help="Analysis ID")
        main_parser.add_argument('files_dir', help="Directory where files are located")
        main_parser.add_argument('manifest_file', type=argparse.FileType('w'), help="Output manifest path")
        return

    def _run(self):
        response = requests.get('%s/studies/%s/analysis/%s' % (self.song_server,self.args.study,self.args.analysis_id))

        if not response.status_code == 200:
            raise Exception(response.text)

        analysis = response.json()

        self.args.manifest_file.write(analysis.get('analysisId')+'\t\t\n')
        for i in range(0, len(analysis.get('file'))):
            file_object = analysis.get('file')[i]
            self.args.manifest_file.write(file_object.get('objectId') + '\t' + os.path.join(self.args.files_dir,file_object.get('fileName')) + '\t' + file_object.get('fileMd5sum') + '\n')
        return

