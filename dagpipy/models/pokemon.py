class Pokemon:
    def __init__(self, data: dict):
        self.question = data.get('question_image')
        self.answer = data.get('answer_image')
        pokemon = data.get('pokemon')
        self.abilities = pokemon.get('abilities')
        self.ascii = pokemon.get('ascii')
        self.height = pokemon.get('height')
        self.id = pokemon.get('id')
        self.link = pokemon.get('link')
        self.name = pokemon.get('name')
        self.types = pokemon.get('types')
        self.weight = pokemon.get('weight')

    def __repr__(self):
        return self.question