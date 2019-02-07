from uperations.operation import Operation

class Studyoperationtype(Operation):

    def _parser(self, main_parser):
        super(Studyoperationtype, self)._parser(main_parser)
        main_parser.add_argument('--study',dest='study', help="ICGC study ID", required=True)
        return main_parser

    @property
    def study(self):
        return self.args.study

    def _before_start(self):
        super(Studyoperationtype, self)._before_start()
        #print(self.args.first_argument)
        return True

    def _on_running(self):
        super(Studyoperationtype, self)._on_running()
        return True

    def _on_error(self, exception):
        super(Studyoperationtype, self)._on_error(exception)
        return True

    def _on_completed(self):
        super(Studyoperationtype, self)._on_completed()
        return True