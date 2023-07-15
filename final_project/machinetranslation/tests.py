import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslations(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertEqual(englishToFrench('Book'),'Livre')

    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish('Rouge'),'Red')