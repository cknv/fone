import unittest
import fonos


class TestTranslation(unittest.TestCase):
    def test_simple_translate(self):
        assert fonos.translate('abc') == ['alfa', 'bravo', 'charlie']

    def test_simple_parse(self):
        assert fonos.parse('alfa bravo charlie') == ['a', 'b', 'c']

if __name__ == '__main__':
    unittest.main()
