
from uperations.operation import Operation
import requests
import jsonschema
import argparse
import json

class Validate(Operation):

    @staticmethod
    def name():
        return "Validate"

    @staticmethod
    def description():
        return "Validate a json payload"

    @property
    def payload(self):
        return self.args.payload

    def _parser(self, main_parser):
        main_parser.add_argument('payload', type=argparse.FileType('r'), help="JSON Payload")
        return

    def _run(self):
        validator = requests.get('https://raw.githubusercontent.com/overture-stack/SONG/develop/song-server/src/main/resources/schemas/sequencingRead.json').json()
        try:
            jsonschema.validate(json.load(self.payload),validator)
        except jsonschema.exceptions.ValidationError as err:
            print(json.dumps({'valid':False,'error':str(err.message)}))
        print(json.dumps({'valid': True}))
        return
