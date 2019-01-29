
from uperations.kernel import Kernel
from uperation_base import Base
from libraries.sing.sing import sing

def boot():
    Kernel.get_instance().set_libraries({
        Base.name(): Base(),
        sing.name(): sing()
    })

    Kernel.get_instance().set_observers({
        #operation().__class__ : [
        #   observer().__class__
        # ]
    })