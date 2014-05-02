standard_nato = {
    'a': 'alfa',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
    '-': 'dash',
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'niner',
}


def translate(message):
    f = Fonos()
    return list(f.translate(message))


def parse(message):
    f = Fonos()
    return list(f.parse(message))


class Fonos:
    def __init__(self, dialect=None):
        if dialect is None:
            dialect = standard_nato
        self.alphabet = dialect
        self.lookup = {word: char for char, word in self.alphabet.items()}

    def translate(self, message):
        for char in message:
            if char in self.alphabet:
                yield self.alphabet[char]

    def parse(self, message):
        for word in message.split():
            if word in self.lookup:
                yield self.lookup[word]
