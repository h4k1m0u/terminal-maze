# escape characters can be tested in bash with `echo -e "\x1b[..."`
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

def move_cursor_to_origin():
    print('\x1b[H')

def move_cursor(row: int, col: int):
    """Origin is (1, 1) with escape characters while coords in grid.py are zero-indexed (same as passed arguments)"""
    print(f'\x1b[{row + 1};{col + 1}H', end='')

def print_at_coords(letter: str, row: int, col: int):
    move_cursor(row, col)
    print(letter, end='')

def clear_screen():
    print('\x1b[2J', end='')
