from typex import TypeX
from encryptor import Encryptor
from rotor import Rotor
from stator import Stator
from reflector import Reflector
import unittest2

class TypeXTest(unittest2.TestCase):

    def test_constructor(self):
        self.assertTrue(isinstance(TypeX(), TypeX))
        self.assertTrue(isinstance(TypeX(encryptors=[]), TypeX))

    def test_if_encryptors_are_valid(self):
        self.assertTrue(isinstance(TypeX(encryptors=[
            Stator(wiring='ABCDEF OPQGHIJKLMNRSTXYZUVW', initial_position=3),
            Rotor(wiring='QWERTYUIOPAS DFGHJKLZXCVBNM', initial_position=4, notchings=[0,5,12,16,25])]),
            TypeX))

        with self.assertRaises(TypeError):
            TypeX(encryptors= 'a flamingo wrapped in tinsel')

        # Pass in encryptors that include a non-Encryptor
        with self.assertRaises(TypeError):
            TypeX(encryptors=[Stator(wiring='ABCDEF OPQGHIJKLMNRSTXYZUVW', initial_position=3), 'flamingo'])

        # Pass in encryptors that include a Reflector
        with self.assertRaises(TypeError):
            TypeX(encryptors=[Stator(wiring='ABCDEFOPQGHIJKLMNRS TXYZUVW', initial_position=3), Reflector()])

        # Pass in encryptors that are out of order
        with self.assertRaises(ValueError):
            TypeX(encryptors=[
                Rotor(wiring='QWERTYUIOPASDFGHJKLZX CVBNM', initial_position=4, notchings=[0, 5, 12, 16, 25]),
                Stator(wiring='ABCDEFOP QGHIJKLMNRSTXYZUVW', initial_position=3)])

if __name__ == '__main__':
    unittest2.main()
