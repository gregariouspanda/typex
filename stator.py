# TODO: Why is this line here?
from encryptor import Encryptor

class Stator(Encryptor):
    # Construct a new stator with a giving wiring, and optionally
    # a given initial position other than zero.
    #
    # TODO: Are we going to support inserting the the stator in a
    # rotated fashion such that the 'A' input is not the zero
    # position# of the wiring? If not, then the initial_position
    # parameter to this method is useless.
    def __init__(self, wiring=None, initial_position=0):
        # TODO: store the provided wiring in an attribute
        #
        # TODO: store the initial_position in an attribute (maybe;
        # see above)
        #
        # TODO: Figure out how to use Encryptor.__init__ so that we
        # don't duplicate effort in this constructor.

        # TODO: Remove this once there is useful code in this method
        pass

    def encrypt_char(self, char):
        # TODO: Do we need to implement this, or can we use
        # the implementation in Encryptor.encrypt_char()?

        # TODO: Remove this once there is useful code in this
        # method (or we are letting Encryptor.encrypt_char()
        # handle this).
        pass

    def rotate(self):
        # TODO: What does Stator's rotate() actually do?
        #
        # TODO: What should Stator's rotate() return? What
        # assumption about the structure of a TypeX machine is
        # implicitly baked into the answer to that question?

        # TODO: Remove this once there is useful code in this method
        pass
