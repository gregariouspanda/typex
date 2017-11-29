import sys

# Our classes
from stator import Stator
from rotor import Rotor
from reflector import Reflector
from encryptor import Encryptor

class TypeX:
    def __init__(self, encryptors=[]):
        self.encryptors = encryptors

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
        self.step()

        # Clean up the input string
        cleaned_string = self.clean(string)

        # TODO: actually send the string through the
        # sequence of stators, rotors, and reflectors
        encrypted_string = cleaned_string # My what a lame encryption algorithm you have.

        # Return the encrypted string
        return encrypted_string

def main():
    # TODO: pass in some actual stator/rotor configs here
    typex = TypeX(encryptors=[
        Stator(wiring='THELAZYBROWNFXJUMPSVQICKDG', initial_position=0),
        Stator(wiring='ABCDEFOPQGHIJKLMNRSTXYZUVW', initial_position=3),
        Rotor(wiring='QWERTYUIOPASDFGHJKLZXCVBNM', initial_position=4, notchings=[0,5,12,16,25]),
        Rotor(wiring='HELOWRDQTYUIPASFGJKZXCVBNM', initial_position=2, notchings=[3,4,6,10]),
        Rotor(wiring='TMJKLQNSAPBUGCVRZWYHDEFOIX', initial_position=7)
    ])

    # Read in all of the lines from stdin
    input_text = ''
    if sys.argv[1]:
        input_text = open(sys.argv[1],'r').read()
    else:
        input_text = sys.stdin.readlines()

    # Encode the text from stdin
    encrypted_text = typex.encrypt(input_text)

    # Print the result to stdout
    print(''.join(encrypted_text))

if __name__ == '__main__':
    main()
