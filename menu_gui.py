
class Animal():
    def __init__(self):
        self.EDAD = 10

class Life():
    def __init__(self):
        self.xdd = 69

class Perro(Animal, Life):
    def __init__(self):
        super(Animal, self).__init__()
        super().__init__()
        print(self.EDAD)
        print(self.xdd)

# Im going to make a menu system
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.init()

GAME_STATE = True

PAUSED = False
RUNNING = True

FPS = 10
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MenuSystem")    

FONT = pygame.font.SysFont(None, 40)

def on_event(event):

    global GAME_STATE
    
    pressed_keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()

    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    # elif mouse_buttons[0] == True: # left click
        # continue
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            pass
        elif event.key == pygame.K_ESCAPE:
            if GAME_STATE == True:
                GAME_STATE = False
            else:
                GAME_STATE = True
    # elif event.type == pygame.KEYUP:
    #     if event.key == pygame.K_SPACE:
    #         print("EE")
            

class Button():
    def __init__(self, surface, pos, size = (200, 60), color = BLUE):
        """
        surface -> pygame.Surface
          Surface where to put the button.
        pos -> tuple of size 2
          Coordinates where to put the button.
          pos[0] as x axis and pos[1] as y axis
        color -> tuple of size 3
          Color choosen
        """
        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.color = color
        self.surface = surface
        
        self.button = pygame.Surface((100, 30))
        
    def render(self):
        self.button.fill((self.color[0], self.color[1], self.color[2]))
        self.surface.blit(self.button, (self.x, self.y))
            

def make_button(surface, pos, size = (200, 60), color = BLUE):
    """
    surface -> pygame.Surface
      Surface where to put the button.
    pos -> tuple of size 2
      Coordinates where to put the button.
      pos[0] as x axis and pos[1] as y axis
    color -> tuple of size 3
      Color choosen
    """
    button = pygame.Surface((200, 60))
    button.fill((color[0], color[1], color[2]))
    surface.blit(button, (pos[0], pos[1]))
    return button

def draw_text(text, font, text_color, coords):
    font = font.render(text, True, text_color)
    DISPLAYSURFACE.blit(font, (coords[0], coords[1]))


def display_menu():
    pass

def run():
    game_running = True
    
    btn1 = Button(DISPLAYSURFACE, pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    while True:
        DISPLAYSURFACE.fill((220, 220, 220))

        if GAME_STATE == False:
            draw_text("EL BIDEOJUEGO ESTÁ PAUSADO PUTO", FONT, BLACK, (160, 250))
        else:
            draw_text("HOLA IGÜEPUTAS!!", FONT, BLACK, (160, 250))

        btn1.render()
        draw_text("Jugar", FONT, WHITE, (btn1.x + 20, btn1.y + 30))
        
        for event in pygame.event.get():
            on_event(event)
        
        pygame.display.update()
        FramePerSec.tick(FPS)
    

if __name__ == "__main__":
    run()
        

