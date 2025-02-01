import copy

from coord import Coord
from glyph import Glyph
from hole import Hole
from terminal import print_at_coords

class Cell:
    def __init__(self, coord: Coord, glyph: Glyph):
        # shallow copy as holes filled when an adjacent celll is inserted
        self.holes = copy.copy(glyph.holes)
        self.glyph = glyph
        self.coord = coord

    def fill_hole(self, hole: Hole):
        self.holes.remove(hole)

    def render(self):
        print_at_coords(self.glyph.character, self.coord.row, self.coord.col)

    def __str__(self):
        """For debugging (called by print() and str())"""
        character = self.glyph.character
        return f'character: {character}, coord: {self.coord}, holes: {self.holes}'
