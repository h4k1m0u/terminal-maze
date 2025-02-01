from enum import Enum

from coord import Coord

class Hole(Enum):
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4

# hole with whom each hole can be connected
HOLE_CONNECTION = {
    Hole.LEFT: Hole.RIGHT,
    Hole.RIGHT: Hole.LEFT,
    Hole.BOTTOM: Hole.TOP,
    Hole.TOP: Hole.BOTTOM,
}

# key is hole & value is offset of connected hole under the form (row, col)
HOLE_OFFSET = {
    Hole.LEFT:   Coord(  0, -1 ),
    Hole.RIGHT:  Coord(  0,  1 ),
    Hole.BOTTOM: Coord(  1,  0 ),
    Hole.TOP:    Coord( -1,  0 ),
}
