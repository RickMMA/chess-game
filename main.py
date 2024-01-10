import pygame, sys, os
from pygame.locals import *
import random
 
# pygame.init()
# pygame.display.init()
 
# FPS = 10
# FramePerSec = pygame.time.Clock()
 
# # Predefined some colors
# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
 
# # Screen information
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
 
# DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Chess Game")

# FONT = pygame.font.SysFont(None, 48)
 
 
class game():
      def __init__(self):
            pygame.init()
            pygame.display.init()

            self.FPS = 10
            self.FramePerSec = pygame.time.Clock()

            # Predefined some colors
            self.BLUE  = (0, 0, 255)
            self.RED   = (255, 0, 0)
            self.GREEN = (0, 255, 0)
            self.BLACK = (0, 0, 0)
            self.WHITE = (255, 255, 255)

            # Screen information
            self.SCREEN_WIDTH = 800
            self.SCREEN_HEIGHT = 600

            self.DISPLAYSURFACE = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            pygame.display.set_caption("Chess Game")

            self.FONT = pygame.font.SysFont(None, 48)


            

      def on_event(self, event):
            pressed_keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()
            
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
            elif mouse_buttons[0] == True: # left click
                  print("AAAAAA")
            


class chessPiece(pygame.sprite.Sprite, game):
      def __init__(self, pieceName):
            super().__init__()
            self.image = pygame.image.load(os.path.join(
                  os.getcwd(), "assets", "chess_pieces", f"{pieceName}.png"))
            self.rect = self.image.get_rect()
            self.rect.center = (self.SCREEN_WIDTH-40,40) 
            
      def move(self):
            # self.rect.move_ip(0,10)
            pass
                  
      def render(self, surface):
            surface.blit(self.image, self.rect) 
 
 
class chessBoard(pygame.sprite.Sprite, game):
      def __init__(self):
            super(pygame.sprite.Sprite, self).__init__()
            super().__init__()
            # each cell is 32x32px, the board is 8cells x 8cells = 256x256px
            self.image = pygame.image.load(os.path.join(os.getcwd(), "assets", "BOARD.png"))
            self.rect = self.image.get_rect()
            self.position = (self.SCREEN_WIDTH/10, self.SCREEN_HEIGHT/8)
            # self.rect.left = 64 # pixels from the left
            # self.rect.top = 64  # pixels from the top
            self.rect.topleft = self.position
            self.font = self.FONT.render("HOLA MUNDO", False, self.WHITE)
            self.starting_board = [
                  ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                  ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                  ["--", "--", "--", "--", "--", "--", "--", "--"],
                  ["--", "--", "--", "--", "--", "--", "--", "--"],
                  ["--", "--", "--", "--", "--", "--", "--", "--"],
                  ["--", "--", "--", "--", "--", "--", "--", "--"],
                  ["wB", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
                  ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"]
            ]

 
      def update(self):
            pressed_keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()

            if mouse_buttons[0] == True: # left click
                  print("AAAAAA")
      
 
      def render(self, surface):
            surface.blit(self.image, self.rect)
            surface.blit(self.font, (self.position[0], self.position[1]))

            for col, line in self.starting_board:
                  print(col)

      def on_event(self, event):
            super().on_event(event)
            if mouse_buttons[0] == True: # left click
                  print("eee")

      def get_state(self):
            pass
                  

P = ("WHITE","peon", "h7")

# def translator(piece):
      # if piece[0] == "white":
            # render_piece("WHITE_PEON")
            
      # return piece_updated
# coord = [
#       [R, N, B, Q, K, B, N, R],
#       [P, P, P, P, P, P, P, P],
#       [0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0],
#       [P, P, P, P, P, P, P, P],
#       [R, N, B, Q, K, B, N, R]
# ]



if __name__ == "__main__":
      g = game()
      board = chessBoard()
      # piece = chessPiece("bK")
      # g.run()
      while True:     
            for event in pygame.event.get():
                  _event = g.on_event(event)


            board.update()
            # piece.move()

            g.DISPLAYSURFACE.fill((200, 200, 200))
            board.render(g.DISPLAYSURFACE)
            # piece.render(game.DISPLAYSURFACE)

            pygame.display.update()
            game.FramePerSec.tick(FPS)

      # while True:     
      #       for event in pygame.event.get():
      #             on_event()


      #       board.update()
      #       piece.move()

      #       DISPLAYSURFACE.fill((200, 200, 200))
      #       board.render(DISPLAYSURFACE)
      #       piece.render(DISPLAYSURFACE)

      #       pygame.display.update()
      #       FramePerSec.tick(FPS)
      
