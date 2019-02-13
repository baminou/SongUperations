from uperations.operation import Operation
import requests

class Singoperationtype(Operation):

    @property
    def song_url(self):
        return self.args.song_url

    def _parser(self, main_parser):
        super(Singoperationtype, self)._parser(main_parser)
        main_parser.add_argument('--song-url',dest='song_url', help="URL of the SONG server", required=True)
        return main_parser

    def _before_start(self):
        super(Singoperationtype, self)._before_start()
        try:
            response = requests.get('%s/isAlive' % (self.args.song_url))
            if response.text == 'true':
                return True
        except Exception as err:
            raise Exception("The song server %s is not a valid song server: %s" % (self.args.song_url, str(err)))
        return False

    def _on_running(self):
        super(Singoperationtype, self)._on_running()
        return True

    def _on_error(self, exception):
        super(Singoperationtype, self)._on_error(exception)
        exit(1)
        return True

    def _on_completed(self):
        super(Singoperationtype, self)._on_completed()
        return True