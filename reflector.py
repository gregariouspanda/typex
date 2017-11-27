# TODO: Why is this line here?
from encryptor import Encryptor

class Reflector(Encryptor):
    # Construct a new reflector (with hardcoded wiring), and
    # optionally a given initial position other than zero.
    #
    # TODO: Are we going to support setting the reflector in a
    # rotated fashion such that the 'A' input is not the zero
    # position# of the wiring? If not, then the initial_position
    # parameter to this method is useless.
    def __init__(self, initial_position=0):
        # TODO: store the hardcoded reflector wiring in the
        # wiring attribute
        #
        # TODO: store the initial_position in an attribute (maybe;
        # see above)
        #
        # TODO: Figure out how to use Encryptor.__init__ so that we
        # don't duplicate effort in this constructor.

        # TODO: Remove this once there is useful code in this method

        # TODO: Remove this once there is useful code in this method
        pass

    def encrypt_char(self, char):
        # TODO: Do we need to implement this, or can we use
        # the implementation in Encryptor.encrypt_char()?

        # TODO: Remove this once there is useful code in this method
        pass

    def rotate(self):
        # TODO: What does Reflector's rotate() actually do?
        # Will it ever get called?
        #
        # TODO: What should Reflector's rotate() return? Is any
        # assumption about the structure of a TypeX machine
        # implicitly baked into the answer to that question?

        # TODO: Remove this once there is useful code in this method
        pass
