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