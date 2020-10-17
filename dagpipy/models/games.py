__all__ = (
    'Pokemon',
    'LogoGame',
    'Roast',
    'YoMama',
    'PickupLine',
    'Joke'
)


class Pokemon:
    def __init__(self, data: dict):
        DATA = data['Data']
        self.data = data
        self.types = DATA.get('Type')
        self.abilities = DATA.get('abilities')
        self.ascii = DATA.get('ascii')
        self.height = DATA.get('height')
        self.id = int(DATA.get('id'))
        self.link = DATA.get('link')
        self.name = DATA.get('name')
        self.weight = DATA.get('weight')
        self.answer = data.get('answer')
        self.question = data.get('question')

    def __repr__(self):
        return self.question


class LogoGame:
    def __init__(self, data: dict):
        self.answer = data.get('answer')
        self.question = data.get('question')
        self.brand = data.get('brand')
        self.wiki = data.get('wiki_url')
        self.hint = data.get('hint')
        self.clue = data.get('clue')
        if data.get('easy'):
            self.difficulty = "easy"
        else:
            self.difficulty = "hard"

    def __repr__(self):
        return self.question


class Roast:
    def __init__(self, data: dict):
        self.roast = data.get('roast')

    def __repr__(self):
        return self.roast


class YoMama:
    def __init__(self, data: dict):
        self.description = data.get('description')

    def __repr__(self):
        return self.description


class PickupLine:
    def __init__(self, data: dict):
        self.category = data.get('category')
        self.joke = data.get('joke')

    def __repr__(self):
        return self.joke


class Joke:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.joke = data.get('joke')

    def __repr__(self):
        return self.joke


class Waifu:
    def __init__(self):
        pass