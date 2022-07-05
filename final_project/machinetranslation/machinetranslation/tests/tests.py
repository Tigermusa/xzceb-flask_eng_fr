import unittest
from translator import english_to_french, french_to_english
class testTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Null"), "nul") #Test when Null given as input the result is Nul
        self.assertNotEqual(english_to_french("Null"), "une")  #Test when Five given as input the result isn't une
        self.assertEqual(english_to_french("Hello"), "Bonjour") #Test when Hello given as input the result is Bonjour
        self.assertNotEqual(english_to_french("Hello"), "géniale")  #Test when Hello given as input the result isn't géniale 

    def test_french_to_english(self):
        self.assertEqual(french_to_english("nul"), "Null") #Test when Nul given as input the result is Null
        self.assertNotEqual(french_to_english("Nulle"), "une")  #Test when Nulle given as input the result isn't une
        self.assertEqual(french_to_english("Bonjour"), "Hello") #Test when Bonjour given as input the result is Hello
        self.assertNotEqual(french_to_english("Bonjour"), "géniale")  #Test when 1 given as input the result isn't géniale  

if __name__ == '__main__':
    unittest.main()

