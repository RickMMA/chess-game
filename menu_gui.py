import pygame
# from pygame.locals import *   # not using it right now

class Button():
    def __init__(self, surface, pos, size = (200, 60), color = (0, 0, 255), text = "", font = ""):
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
        # self.font = pygame.font.SysFont(None, 40)
        self.font = font
        # self.padding = (15, self.font.get_height()-5)
        self.padding = (0, 0)
        # font.get_height() is not equal to font.size()
        # if font size is set to 40, the font height is 27

        # TODO: make text size relative to the size of the button
        #       meanwhile the font size is fixed
        
        self.button = pygame.Surface((self.size[0], self.size[1]))
        
        self.rect = self.button.get_rect()
        self.is_clicked = False
        
    def render(self):
        self.button.fill( (self.color[0], self.color[1], self.color[2]) )
        # self.surface.blit(self.button, (self.x - self.padding[0], self.y - self.padding[1]))
        self.surface.blit(self.button, (self.x, self.y))

        self.rect.x = self.x # I need to put the rect position here because of changees
        self.rect.y = self.y # in the coordinates outside the object, like in the game loop 

        f = self.font.render(self.text, True, (255, 255, 255))
        f_size = f.get_size()
        btn_width = self.button.get_width()
        btn_height = self.button.get_height()

        # Center text
        # TODO: make conditional to choose pos of text
        x = ((btn_width//2) - (f_size[0]//2)) + self.x
        y = ((btn_height//2) - (f_size[1]//2)) + self.y
        self.surface.blit(f, (x, y))

    def click_button(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        
        self.is_clicked = False
        # print(self.rect.x, self.rect.y, " y mouse:", mouse_pos)
        if self.rect.collidepoint(mouse_pos):
            if left_click == 1 and self.is_clicked == False:
                print(self.rect.x, self.rect.y, " y ", self.x , self.y )
                print(self.button.get_rect().x)
                self.is_clicked = True
                return self.is_clicked
