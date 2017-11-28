# TODO: Why is this line here?
from encryptor import Encryptor

class Rotor(Encryptor):
    def __init__(self, wiring=None, initial_position=0, notchings=None):
        super().__init__(self, wiring, initial_position)
        self.notchings = notchings

    def step(self):
        self.position = (self.position + 1) % len(self.wiring)
        if self.position in self.notchings:
            return True
        else:
            return False
