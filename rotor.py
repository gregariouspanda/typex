# TODO: Why is this line here?
from encryptor import Encryptor

class Rotor(Encryptor):
    def __init__(self, wiring=None, initial_position=0, notchings=None):
        # TODO: Figure out if we can use Encryptor.__init__ so that we
        # don't duplicate effort in this constructor.

        # TODO: Keep track of the notchings so that we know when
        # to tell our neighbor to rotate one step

        # TODO: Remove this once there is useful code in this method
        pass

    def encrypt_char(self, char):
        # TODO: Do we need to implement this, or can we use
        # the implementation in Encryptor.encrypt_char()?

        # TODO: Remove this once there is useful code in this method
        pass

    def rotate(self):
        # TODO: What does Rotor's rotate() actually do?
        #
        # TODO: What should Rotor's rotate() return?

        # TODO: Remove this once there is useful code in this method
        pass
