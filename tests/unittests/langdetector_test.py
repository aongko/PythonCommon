import unittest
from text_processing.languagedetector import LanguageDetector

class TestLanguageDetector(unittest.TestCase):

    def setUp(self):
        self.langdetector = LanguageDetector()

    def test_detect_id(self):
        lang = self.langdetector.detect("Sebuah teks untuk dicoba.")
        self.assertEqual("id", lang)

    def test_detect_en(self):
        lang = self.langdetector.detect("Just another text to be detected.")
        self.assertEqual("en", lang)

if __name__ == '__main__':
    unittest.main()
