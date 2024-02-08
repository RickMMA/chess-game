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
    """
    Event handler
    returns: void
    """
    
    global GAME_STATE # Using the variable in a global context
    
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
    def __init__(self, surface, pos, size = (200, 60), color = BLUE, text = ""):
        """
        surface -> pygame.Surface
          Surface where to put the button.
        pos -> tuple of size 2
          Coordinates where to put the button.
          pos[0] as x axis and pos[1] as y axis
        color -> tuple of size 3
          Color choosen
        """
        # global FONT, WHITE

        self.x = pos[0]
        self.y = pos[1]
        self.size = size
        self.color = color
        self.surface = surface
        self.text = text
        # self.text_size = text_size
        self.font = pygame.font.SysFont(None, 40)
        # self.padding = (15, self.font.get_height()-5)
        self.padding = (0, 0)
        # font.get_height() is not equal to font.size()
        # if font size is set to 40, the font height is 27

        # TODO: make text size relative to the size of the button
        #       meanwhile the font size is fixed
        
        self.button = pygame.Surface((self.size[0], self.size[1]))
        
    def render(self):
        self.button.fill( (self.color[0], self.color[1], self.color[2]) )
        self.surface.blit(self.button, (self.x - self.padding[0], self.y - self.padding[1]))

        f = self.font.render(self.text, True, WHITE)
        f_size = f.get_size()
        btn_width = self.button.get_width()
        btn_height = self.button.get_height()

        # Center text
        # TODO: make conditional to choose pos of text
        x = ((btn_width//2) - (f_size[0]//2)) + self.x
        y = ((btn_height//2) - (f_size[1]//2)) + self.y
        DISPLAYSURFACE.blit(f, (x, y))
        
            

def draw_text(text, font, text_color, coords): # Text drawing utility
    """
    font -> pygame font object
      Gives the font context
    coords -> tuple of size 2
      coords[0] as x axis and pos[1] as y axis
    returns: void
    """
    font = font.render(text, True, text_color)
    DISPLAYSURFACE.blit(font, (coords[0], coords[1]))


def run():
    game_running = True
    
    btn1 = Button(DISPLAYSURFACE, pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text = "Jugar")
    while True:
        

        if GAME_STATE == False:
            DISPLAYSURFACE.fill((220, 220, 220))
            draw_text("EL BIDEOJUEGO ESTÁ PAUSADO PUTO", FONT, BLACK, (160, 250))
        else:
            DISPLAYSURFACE.fill((20, 120, 20))
            draw_text("HOLA IGÜEPUTAS!!", FONT, BLACK, (160, 250))

        btn1.render()
        
        for event in pygame.event.get():
            on_event(event)
        
        pygame.display.update()
        FramePerSec.tick(FPS)
    

if __name__ == "__main__":
    run()
        

