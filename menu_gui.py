import pygame
# from pygame.locals import *   # not using it right now

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
