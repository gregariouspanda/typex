from encryptor import Encryptor

class Reflector(Encryptor):
    # Construct a new reflector (with hardcoded wiring)
    def __init__(self):
        super().__init__(self, wiring=reversed(self.ALPHABET))

    def step(self):
        return False
