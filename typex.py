import sys

# Our classes
from stator import Stator
from rotor import Rotor
from reflector import Reflector

class TypeX:
    def __init__(self, encryptors=[]):
        # TODO: fill up the container of encryptors
        pass

    def clean(self, string):
        # TODO: remove all of the non-encodable characters
        return string

    def rotate(self):
        # TODO: Figure out how to rotate all of the
        # encryptors that should rotate, and none of
        # the ones that shouldn't

        pass

    def encrypt(self, string):
        # First, kill the lawyers^]ESCb^[ESCb^]ESCbrotate the rotors
        self.rotate()

        # Clean up the input string
        cleaned_string = self.clean(string)

        # TODO: actually send the string through the
        # sequence of stators, rotors, and reflectors
        encrypted_string = cleaned_string # My what a lame encryption algorithm you have.

        # Return the encrypted string
        return encrypted_string

def main():
    # TODO: pass in some actual stator/rotor configs here
    typex = TypeX()

    # Read in all of the lines from stdin
    input_text = sys.stdin.readlines()

    # Encode the text from stdin
    encrypted_text = typex.encrypt(input_text)

    # Print the result to stdout
    print(''.join(encrypted_text))

if __name__ == '__main__':
    main()
