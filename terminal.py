# escape characters can be tested in bash with `echo -e "\x1b[..."`
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797

def move_cursor_to_origin():
    print('\x1b[H')

def print_at_coords(letter, row, col):
    """Origin is (1, 1) while coords in grid.py are zero-indexed"""
    print(f'\x1b[{row + 1};{col + 1}H' + letter, end='')

def clear_screen():
    print('\x1b[2J', end='')
