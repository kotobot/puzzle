from const import GRID_SIZE
import random

class Tile:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def update_position(self, row, col):
        self.row = row
        self.col = col


class Board:
    ''' Game board for the 15 puzzle '''
    def __init__(self):
        self.tiles = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.empty_pos = (GRID_SIZE - 1, GRID_SIZE - 1)  # (row, col) of empty tile
        self.initialize_board()
    
    def initialize_board(self):
        # Create tiles in solved position
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = row * GRID_SIZE + col + 1
                if value == GRID_SIZE * GRID_SIZE:
                    value = 0  # Empty tile
                self.tiles[row][col] = Tile(value, row, col)
    
    def shuffle(self, moves=100):
        # Make random moves to shuffle the board
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        for _ in range(moves):
            valid_moves = []
            for dr, dc in directions:
                new_row, new_col = self.empty_pos[0] + dr, self.empty_pos[1] + dc
                if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
                    valid_moves.append((new_row, new_col))
            
            if valid_moves:
                move_pos = random.choice(valid_moves)
                self.move_tile(move_pos)
    
    def move_tile(self, pos):
        row, col = pos
        empty_row, empty_col = self.empty_pos
        
        # Check if the tile is adjacent to the empty space
        if (abs(row - empty_row) + abs(col - empty_col)) != 1:
            return False
        
        # Swap the tile with the empty space
        self.tiles[empty_row][empty_col], self.tiles[row][col] = self.tiles[row][col], self.tiles[empty_row][empty_col]
        
        # Update positions
        self.tiles[empty_row][empty_col].update_position(empty_row, empty_col)
        self.tiles[row][col].update_position(row, col)
        
        # Update empty position
        self.empty_pos = (row, col)
        return True
    
    def update(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                self.tiles[row][col].update_position(row, col)
    
    def is_solved(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                expected_value = row * GRID_SIZE + col + 1
                if expected_value == GRID_SIZE * GRID_SIZE:
                    expected_value = 0
                
                if self.tiles[row][col].value != expected_value:
                    return False
        return True

    def move(self, pos):
        row, col = pos
        
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            self.move_tile((row, col))