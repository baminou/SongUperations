
from uperations.library import Library
from .operations.upload import Upload
from .operations.save import Save
from .operations.create_manifest import CreateManifest
from .operations.publish import Publish
from .operations.status import Status
from .operations.validate import Validate

class sing(Library):

    @staticmethod
    def name():
        return "sing"

    @staticmethod
    def description():
        return "Song client"

    def _init_operations(self):
        self._operations = {
            'upload': Upload(self),
            'save': Save(self),
            'manifest': CreateManifest(self),
            'publish': Publish(self),
            'status': Status(self),
            'validate': Validate(self)
        }
        return

    def operations(self):
        return self._operations