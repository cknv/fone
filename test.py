import unittest
import fone


class TestTranslation(unittest.TestCase):
    def test_simple_translate(self):
        assert fone.translate('abc') == ['alfa', 'bravo', 'charlie']

    def test_simple_parse(self):
        assert fone.parse('alfa bravo charlie') == ['a', 'b', 'c']

    def test_odd_chars(self):
        assert fone.translate('Baden-Württemberg') == [
            'bravo',
            'alfa',
            'delta',
            'echo',
            'november',
            'dash',
            'whiskey',
            'uniform',
            'romeo',
            'tango',
            'tango',
            'echo',
            'mike',
            'bravo',
            'echo',
            'romeo',
            'golf',
        ]

if __name__ == '__main__':
    unittest.main()
