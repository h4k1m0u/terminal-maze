from terminal import clear_screen, move_cursor
from grid import Grid

clear_screen()
grid = Grid()
grid.render()

# ensure next shell prompt doesn't step on printed maze
move_cursor(Grid.N_ROWS, 0)
