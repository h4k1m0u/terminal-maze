from dataclasses import dataclass

@dataclass
class Coord:
    row: int
    col: int

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)

NO_COORD = Coord( -1, -1 )
