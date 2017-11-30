class Encryptor:
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, wiring=None, initial_position=0):
        self.wiring = wiring
        if wiring == None:
            self.wiring = self.ALPHABET
        self.position = initial_position

    def char_to_pos(self, char):
        return ord(char) - 65

    # Perform a substitution for a single character using the
    # current wiring and position of the encryptor
    def encrypt_character(self, char):
        pos = self.char_to_pos(char) + self.position
        return self.wiring[pos % len(self.wiring)]

    def reverse_encrypt_character(self, char):
        pos = self.wiring.index(char) - self.position
        return list(self.ALPHABET)[pos % len(self.wiring)]

    # If appropriate, increments self's current position by
    # one step. Return True if the next Encryptor in sequence
    # should also step(); otherwise, return False.
    def step(self):
        raise NotImplementedError('step() must be implemented by Encryptor subclasses')