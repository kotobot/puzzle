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
        self.button_height = 50
        self.button_width = 200
        self.button_margin = 20
        self.options = [item for item in MenuItem]
        self.selected_option = 0
    
    def draw(self, surface):
        surface.fill(GRAY)
        
        button_y_start = (HEIGHT // 2) - ((len(self.options) * (self.button_height + self.button_margin)) // 2)
        
        for i, option in enumerate(self.options):
            # Calculate button position
            button_y = button_y_start + i * (self.button_height + self.button_margin)
            button_rect = pygame.Rect(WIDTH // 2 - self.button_width // 2, button_y, self.button_width, self.button_height)
            
            # Draw button (blue if selected, white if not)
            button_color = BLUE if i == self.selected_option else WHITE
            pygame.draw.rect(surface, button_color, button_rect)
            pygame.draw.rect(surface, BLUE, button_rect, 2)  # Border
            
            # Draw button text
            text = self.font.render(option.value, True, GRAY if i == self.selected_option else BLUE)
            text_rect = text.get_rect(center=button_rect.center)
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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        mouse_pos = pygame.mouse.get_pos()
                        button_y_start = (HEIGHT // 2) - (
                            (len(self.options) * (self.button_height + self.button_margin)) // 2)
                        
                        for i, option in enumerate(self.options):
                            button_y = button_y_start + i * (self.button_height + self.button_margin)
                            button_rect = pygame.Rect(WIDTH // 2 - self.button_width // 2, 
                                                      button_y, self.button_width, self.button_height)
                            if button_rect.collidepoint(mouse_pos):
                                self.selected_option = i
                                return option

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

