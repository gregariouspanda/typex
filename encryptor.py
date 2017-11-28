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
        # TODO: For each subclass, determine whether a call to
        # step() actually results in the current position
        # changing. For those where it does, implement the
        # position mutation in the subclass' step() method.
        # For those where it doesn't, decide whether it makes
        # sense to return True (continue rotating the next
        # Encryptor) or False (stop the rotation process).
        #
        # TODO: Figure out how to make it so that every subclass
        # it FORCED to implement its own version of step().

        # TODO: Remove this once there is useful code in this method
        pass
