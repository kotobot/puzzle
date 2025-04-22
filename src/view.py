from const import GRID_SIZE, TILE_SIZE, WHITE, BLUE
import pygame

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


class BoardView:
    def __init__(self, board):
        self.board = board
    
    def draw(self, surface):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                TileView(self.board.tiles[row][col]).draw(surface)