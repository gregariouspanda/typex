class Encryptor:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, wiring=None, initial_position=0):
        self.wiring = wiring
        if wiring == None:
            self.wiring = self.ALPHABET
        self.position = initial_position

    # Perform a substitution for a single character using the
    # current wiring and position of the encryptor
    def encrypt_character(self, char):
        # TODO: Figure out how to encrypt a single character
        # given our wiring and current rotation position
        #
        # TODO: Figure out whether we need to implement this
        # here, or whether we need a different implementation
        # for each subclass of Encryptor.

        # This placeholder is a terrible encryption algorithm :-)
        return char

    # If appropriate, increments self's current position by
    # one step. Return True if the next Encryptor in sequence
    # should also step(); otherwise, return False.
    def step(self):
        raise NotImplementedError('step() must be implemented by Encryptor subclasses')