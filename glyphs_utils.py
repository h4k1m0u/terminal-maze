from glyph import Glyph
from hole import Hole, HOLE_CONNECTION

EMPTY = ''

# box drawing unicode characters
# https://en.wikipedia.org/wiki/List_of_Unicode_characters#Box_Drawing
GLYPHS = [
    Glyph([ Hole.LEFT, Hole.RIGHT ], '═'),
    Glyph([ Hole.TOP, Hole.BOTTOM ], '║'),
    Glyph([ Hole.BOTTOM, Hole.RIGHT ], '╔'),
    Glyph([ Hole.BOTTOM, Hole.LEFT ], '╗'),
    Glyph([ Hole.TOP, Hole.RIGHT ], '╚'),
    Glyph([ Hole.TOP, Hole.LEFT ], '╝'),
    Glyph([ Hole.TOP, Hole.BOTTOM, Hole.RIGHT ], '╠'),
    Glyph([ Hole.TOP, Hole.BOTTOM, Hole.LEFT ], '╣'),
    Glyph([ Hole.BOTTOM, Hole.LEFT, Hole.RIGHT ], '╦'),
    Glyph([ Hole.TOP, Hole.LEFT, Hole.RIGHT ], '╩'),
    Glyph([ Hole.TOP, Hole.BOTTOM, Hole.LEFT, Hole.RIGHT ], '╬'),
]

def find_connections(hole: Hole):
    """Glyphs that can be connected to given hole"""
    return [
        glyph for glyph in GLYPHS
        if HOLE_CONNECTION[hole] in glyph.holes
    ]
