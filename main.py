import pygame, sys, os
from pygame.locals import * 
  
 
class game():
      def __init__(self):
            pygame.init()
            pygame.display.init()

            self.FPS = 1
            self.FramePerSec = pygame.time.Clock()
            self.gameState = True

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
                  pass
            elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE:
                        if self.gameState == True:
                              self.gameState = False
                        else:
                              self.gameState = True 
                        
                  
            


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


class boardTile():
      """
      Object to track the state of each tile.
      """
      def __init__(self, name, piece):
            self.tile_name = name
            self.piece = piece
            # self.tile_position = pass
            """
            quiero hacer click en una casilla y que se imprima en la consola
            """

      def render(self, boardState):
            self.letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            self.lettersToInt = [65, 66, 67, 68, 69, 70, 71, 72]
            self.indexes = [1, 2, 3, 4, 5, 6, 7, 8]

            for row in boardState:
                  for tile in row:
                        pass


      
      
class chessBoard(pygame.sprite.Sprite, game):
      def __init__(self):
            super(pygame.sprite.Sprite, self).__init__()
            super().__init__()
            # each cell is 32x32px, the board is 8cells x 8cells = 256x256px
            self.image = pygame.image.load(os.path.join(os.getcwd(), "assets", "BOARD.png"))
            self.brownTile = pygame.image.load(os.path.join(os.getcwd(), "assets", "brown-tile.png"))
            self.whiteTile = pygame.image.load(os.path.join(os.getcwd(), "assets", "white-tile.png"))
            self.rect = self.image.get_rect()
            self.position = (self.SCREEN_WIDTH/10, self.SCREEN_HEIGHT/8)
            self.rect.topleft = self.position
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

            self.a = boardTile("aa", "bb")
            print(self.a.piece)

 
      def update(self):
            pressed_keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()

            if mouse_buttons[0] == True: # left click
                  print("AAAAAA")
      
 
      def render(self, surface):
            self.font = self.FONT.render("HOLA MUNDO", False, self.WHITE)
            
            surface.blit(self.image, self.rect) # board image
            surface.blit(self.font, (self.position[0], self.position[1]))

            

            
            # for row in self.starting_board:
                  # for i in row:
                        # print(i)


      def on_event(self, event):
            super().on_event(event)
            if mouse_buttons[0] == True: # left click
                  print("eee")

      def get_state(self):
            pass




if __name__ == "__main__":
      g = game()
      board = chessBoard()

      boardState = board.starting_board
            

      while True:

            
            board.update()
            # piece.move()

            if g.gameState == False:
                  img = pygame.image.load(os.path.join(os.getcwd(), "assets", "chess-1280.jpg"))
                  g.DISPLAYSURFACE.blit(img, (0, 0))
            else:
                  g.DISPLAYSURFACE.fill((200, 200, 200))
                  board.render(g.DISPLAYSURFACE)
            # piece.render(game.DISPLAYSURFACE)
            # print(g.gameState)

            for event in pygame.event.get():
                  g.on_event(event)

            
            pygame.display.update()
            g.FramePerSec.tick(FPS)
