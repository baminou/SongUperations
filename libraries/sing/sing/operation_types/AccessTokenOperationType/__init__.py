from uperations.operation import Operation
import os

class Accesstokenoperationtype(Operation):

    def _parser(self, main_parser):
        super(Accesstokenoperationtype, self)._parser(main_parser)
        main_parser.add_argument('--access-token',dest='access_token', help="Access token global variable name", default='ACCESS_TOKEN')
        return main_parser

    @property
    def access_token(self):
        return os.environ.get(self.args.access_token)

    def _before_start(self):
        super(Accesstokenoperationtype, self)._before_start()
        if not os.environ.get(self.args.access_token):
            raise Exception("Your environment does not contain variable: %s" % (self.args.access_token))
        return True

    def _on_running(self):
        super(Accesstokenoperationtype, self)._on_running()
        return True

    def _on_error(self, exception):
        super(Accesstokenoperationtype, self)._on_error(exception)
        return True

    def _on_completed(self):
        super(Accesstokenoperationtype, self)._on_completed()
        return True