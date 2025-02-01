from hole import Hole

class Glyph:
    def __init__(self, holes: list[Hole], character: str):
        self.holes = holes
        self.character = character
