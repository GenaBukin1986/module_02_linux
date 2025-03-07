import unittest
from decrypt import decrypt

class TestSample(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')
    def test_2(self):
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
    def test_3(self):
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
    def test_4(self):
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')
    def test_5(self):
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
    def test_6(self):
        self.assertEqual(decrypt('абра........'), '')
    def test_7(self):
        self.assertEqual(decrypt('абр......a.'), 'a')
    def test_8(self):
        self.assertEqual(decrypt('1..2.3'), '23')
    def test_9(self):
        self.assertEqual(decrypt('.'), '')
    def test_10(self):
        self.assertEqual(decrypt('1.......................'), '')

if __name__ == "__main__":
    unittest.main()