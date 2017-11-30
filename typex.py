import sys

# Our classes
from stator import Stator
from rotor import Rotor
from reflector import Reflector
from encryptor import Encryptor

class TypeX:
    def __init__(self, encryptors=[]):
        self.encryptors = encryptors
        self.reflector = Reflector()

    def clean(self, string):
        clean_list = []
        for char in string:
            if char.upper() in Encryptor.ALPHABET:
                clean_list.append(char.upper())
            elif char == ' ':
                clean_list.append('X')

        return ''.join(clean_list)

    def step(self):
        for e in self.encryptors:
            if not e.step():
                break

    def encrypt(self, string):
        # Clean up the input string and
        # encrypt it
        encrypted_chars = []
        for char in self.clean(string):
            # Before encrypting each letter, step the rotors
            self.step()
            for e in self.encryptors:
                char = e.encrypt_character(char)
            char = self.reflector.encrypt_character(char)
            for e in reversed(self.encryptors):
                char = e.reverse_encrypt_character(char)
            encrypted_chars.append(char)


        return ''.join(encrypted_chars)

def read_file(file_name):
    return open(file_name, 'r').read()


def main():

    typex = TypeX(encryptors=[
        Stator(wiring='THELAZYBROWNFXJUMPSVQICKDG', initial_position=0),
        Stator(wiring='ABCDEFOPQGHIJKLMNRSTXYZUVW', initial_position=3),
        Rotor(wiring='QWERTYUIOPASDFGHJKLZXCVBNM', initial_position=4, notchings=[0,5,12,16,25]),
        Rotor(wiring='HELOWRDQTYUIPASFGJKZXCVBNM', initial_position=2, notchings=[3,4,6,10]),
        Rotor(wiring='TMJKLQNSAPBUGCVRZWYHDEFOIX', initial_position=7)
    ])

    # Read in all of the lines from file names
    # specified in argument list or from stdin
    if len(sys.argv) >= 2:
        input_text = ''.join(map(read_file, sys.argv[1:]))
    else:
        input_text = sys.stdin.read()

    # Encode the text from stdin
    encrypted_text = typex.encrypt(input_text)

    # Print the result to stdout
    print(''.join(encrypted_text))

if __name__ == '__main__':
    main()
