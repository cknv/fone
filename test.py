import unittest
import fone


class TestTranslation(unittest.TestCase):
    def test_simple_translate(self):
        assert fone.translate('abc') == ['alfa', 'bravo', 'charlie']

    def test_simple_parse(self):
        assert fone.parse('alfa bravo charlie') == ['a', 'b', 'c']

if __name__ == '__main__':
    unittest.main()
