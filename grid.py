from collections import deque
import random

from coord import Coord, NO_COORD
from glyph import Glyph
from cell import Cell
from hole import Hole, HOLE_OFFSET
import glyphs_utils as GlyphsUtils

class Grid:
    N_ROWS = 32
    N_COLS = 32

    def __init__(self):
        self._init_arr()

        glyph = random.choice(GlyphsUtils.GLYPHS)
        cell = Cell(Coord( 0 , 0 ), glyph)
        self.fifo = deque([ cell ])

    def _init_arr(self):
        self.matrix = []
        for _ in range(Grid.N_ROWS):
            row = Grid.N_COLS * [ GlyphsUtils.EMPTY ]
            self.matrix.append(row)

    def _find_empty_coord(self) -> Coord:
        for i_row in range(Grid.N_ROWS):
            row = self.matrix[i_row]

            if GlyphsUtils.EMPTY in row:
                i_col = row.index(GlyphsUtils.EMPTY)
                return Coord(i_row, i_col)

        return NO_COORD

    def _is_coord_outside(self, coord: Coord):
        """Check if given coord is outside the grid"""
        return (
            coord.row < 0 or coord.row >= Grid.N_ROWS or
            coord.col < 0 or coord.col >= Grid.N_COLS
        )

    def _is_coord_filled(self, coord: Coord):
        """Check if given coord is already filled"""
        return self.matrix[coord.row][coord.col]

    def _find_cell_to_connect(self, coord: Coord, hole: Hole) -> Cell:
        glyphs_to_connect = GlyphsUtils.find_connections(hole)
        offset = HOLE_OFFSET[hole]
        glyphs_adjacent = []
        coords_adjacent = []

        for glyph_to_connect in glyphs_to_connect:
            coord_adjacent = coord + offset

            if self._is_coord_outside(coord_adjacent):
                continue

            if self._is_coord_filled(coord_adjacent):
                continue

            glyphs_adjacent.append(glyph_to_connect)
            coords_adjacent.append(coord_adjacent)

        n_adjacent = len(glyphs_adjacent)
        if n_adjacent == 0:
            # print('No connection')
            return None

        i_adjacent = random.choice(range(n_adjacent))
        cell = Cell(coords_adjacent[i_adjacent], glyphs_adjacent[i_adjacent])
        # print('Cell connection: ', end='')
        # print(cell)
        return cell

    def _render_cell(self, cell: Cell):
        coord = cell.coord
        self.matrix[coord.row][coord.col] = cell.glyph.character
        cell.render()

    def render(self):
        cell = self.fifo[0]
        self._render_cell(cell)

        while self.fifo:
            cell = self.fifo[0]
            is_found = False
            # print('Cell initial: ', end='')
            # print(cell)

            for hole in cell.holes:
                # print('hole:', hole)
                cell_adjacent = self._find_cell_to_connect(cell.coord, hole)
                is_found = cell_adjacent is not None

                if is_found:
                    cell.fill_hole(hole)
                    self.fifo.append(cell_adjacent)
                    self._render_cell(cell_adjacent);
                    break

            if not is_found:
                cell_old = self.fifo.popleft()
                # print('Removing: ', end='')
                # print(cell_old)

            # look for any cell not filled yet if dead-end reached
            if not self.fifo:
                coord = self._find_empty_coord()

                if coord != NO_COORD:
                    glyph = random.choice(GlyphsUtils.GLYPHS)
                    cell_empty = Cell(coord, glyph)
                    self.fifo.append(cell_empty)
                    self._render_cell(cell_empty);
                    # print('Dead end reached: ', end='')
                    # print(cell_empty)
