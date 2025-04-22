from enum import Enum
import pickle
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 100, 200)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("15 Puzzle")
clock = pygame.time.Clock()

class MenuItem(Enum):
    START = "Start"
    SAVE = "Save"
    LOAD = "Load"
    EXIT = "Exit"

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 36)
        self.options = [item for item in MenuItem]
        self.selected_option = 0
    
    def draw(self, surface):
        surface.fill(GRAY)
        for i, option in enumerate(self.options):
            color = BLUE if i == self.selected_option else WHITE
            text = self.font.render(option.value, True, color)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 40))
            surface.blit(text, text_rect)

    def run(self):
        # Main menu loop
        while True:
            self.draw(screen)
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.options[self.selected_option]

    def handle_input(self, event):
        print(event)
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_UP:
                self.selected_option = (self.selected_option - 1) % len(self.options)
            elif event.key == pygame.K_DOWN:
                self.selected_option = (self.selected_option + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected_option]
        return None


class Tile:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def update_position(self, row, col):
        self.row = row
        self.col = col


class TileView:
    def __init__(self, tile):
        self.value = tile.value
        self.x = tile.col * TILE_SIZE
        self.y = tile.row * TILE_SIZE
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
    
    def draw(self, surface):
        if self.value != 0:  # Don't draw the empty tile
            pygame.draw.rect(surface, BLUE, self.rect)
            pygame.draw.rect(surface, WHITE, self.rect, 2)
            
            # Draw the tile number
            font = pygame.font.SysFont(None, 36)
            text = font.render(str(self.value), True, WHITE)
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)


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
    
    #TODO: move to Game class
    def save_game(self):
        pickle.dump(self.tiles, open("save_game.pkl", "wb"))
    
    #TODO: move to Game class
    def load_game(self):
        try:
            self.tiles = pickle.load(open("save_game.pkl", "rb"))
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    self.tiles[row][col].update_position(row, col)
        except FileNotFoundError:
            print("No saved game found.")

    def move(self, pos):
        row, col = pos
        
        if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE:
            self.move_tile((row, col))

class BoardView:
    def __init__(self, board):
        self.board = board
    
    def draw(self, surface):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                TileView(self.board.tiles[row][col]).draw(surface)
    
class Game:
    def __init__(self, board: Board):
        self.board = board
        self.board_view = BoardView(board)
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        # Get the tile position from the mouse click
                        x, y = event.pos
                        col = x // TILE_SIZE
                        row = y // TILE_SIZE
                        self.board.move((row, col))
                        self.board.update()
                        self.board_view.draw(screen)
                        if self.board.is_solved():
                            print("Puzzle solved!")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reset/shuffle with 'r' key
                        self.board.shuffle()
            
            # Draw
            screen.fill(GRAY)
            self.board_view.draw(screen)
            pygame.display.flip()
            clock.tick(FPS)
 
def main():
    board = Board()
    menu = Menu()
    while True:
        selected = menu.run()
        if selected == MenuItem.START:
            board.shuffle()
            game = Game(board)
            game.run()
        elif selected == MenuItem.SAVE:
            board.save_game()
        elif selected == MenuItem.LOAD:
            board.load_game()
            game = Game(board)
            game.run()
        elif selected == MenuItem.EXIT:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()