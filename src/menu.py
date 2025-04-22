from enum import Enum
import pygame
import sys

from const import WIDTH, HEIGHT, WHITE, BLUE, GRAY

class MenuItem(Enum):
    START = "Start"
    SAVE = "Save"
    LOAD = "Load"
    EXIT = "Exit"

class Menu:
    def __init__(self, screen):
        self.screen = screen
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
            self.draw(self.screen)
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

