import pygame, sys, os
from pygame.locals import *
from menu_gui import Button
  
 
pygame.init()
pygame.display.init()

FPS = 10
FramePerSec = pygame.time.Clock()
gameState = False

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
pygame.display.set_caption("Chess Game")

FONT = pygame.font.SysFont(None, 48)


rec = pygame.Rect(100, 100, 50, 20)
surf = pygame.Surface((rec.width, rec.height))
surf.fill((255, 0, 0))

            

def on_event(event):
    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    global gameState
    
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pass
    elif event.type == pygame.MOUSEMOTION:
        rec.move_ip(mouse_pos[0], mouse_pos[1])
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            if gameState == True:
                gameState = False
            else:
                gameState = True
        elif pressed_keys[K_ESCAPE]:        
            print(mouse_pos)

    pygame.event.pump()
                        
                        
                  
            
class chessPiece(pygame.sprite.Sprite):
      def __init__(self, pieceName):
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


      
      
class chessBoard(pygame.sprite.Sprite):
      def __init__(self):
            super(pygame.sprite.Sprite, self).__init__()
            # each cell is 32x32px, the board is 8cells x 8cells = 256x256px
            self.image = pygame.image.load(os.path.join(os.getcwd(), "assets", "BOARD.png"))
            self.brownTile = pygame.image.load(os.path.join(os.getcwd(), "assets", "brown-tile.png"))
            self.whiteTile = pygame.image.load(os.path.join(os.getcwd(), "assets", "white-tile.png"))
            self.rect = self.image.get_rect()
            self.position = (SCREEN_WIDTH/10, SCREEN_HEIGHT/8)
            self.rect.topleft = self.position

            self.starting_board = {
                  "A8":("bR", (0, 0)), "B8":"bN", "C8":"bB", "D8":"bQ", "E8":"bK", "F8":"bB", "G8":"bN", "H8":"bR",
                  "A7":"bP", "B7":"bP", "C7":"bP", "D7":"bP", "E7":"bP", "F7":"bP", "G7":"bP", "H7":"bP",
                  "A6":"--", "B6":"--", "C6":"--", "D6":"--", "E6":"--", "F6":"--", "G6":"--", "H6":"--",
                  "A5":"--", "B5":"--", "C5":"--", "D5":"--", "E5":"--", "F5":"--", "G5":"--", "H5":"--",
                  "A4":"--", "B4":"--", "C4":"--", "D4":"--", "E4":"--", "F4":"--", "G4":"--", "H4":"--",
                  "A3":"--", "B3":"--", "C3":"--", "D3":"--", "E3":"--", "F3":"--", "G3":"--", "H3":"--",
                  "A2":"wP", "B2":"wP", "C2":"wP", "D2":"wP", "E2":"wP", "F2":"wP", "G2":"wP", "H2":"wP",
                  "A1":"wB", "B1":"wN", "C1":"wB", "D1":"wQ", "E1":"wK", "F1":"wB", "G1":"wN", "H1":"wR"
            }


 
      def update(self):
            pressed_keys = pygame.key.get_pressed()
            mouse_buttons = pygame.mouse.get_pressed()

            if mouse_buttons[0] == True: # left click
                  print("AAAAAA")
      
 
      def render(self, surface):
            self.font = FONT.render("HOLA MUNDO", False, WHITE)
            
            surface.blit(self.image, self.rect) # board image
            surface.blit(self.font, (self.position[0], self.position[1]))


      def on_event(self, event):
            if mouse_buttons[0] == True: # left click
                  print("eee")

      def get_state(self):
            pass




if __name__ == "__main__":
      board = chessBoard()

      boardState = board.starting_board

      img = pygame.image.load(os.path.join(os.getcwd(), "assets", "chess-1280.jpg"))
      img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

      btn1 = Button(DISPLAYSURFACE, pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text="Jugar", font=FONT)
      btn1.x = SCREEN_WIDTH/2 - btn1.size[0]/2  # centers button
      btn1.y = SCREEN_HEIGHT/2 - btn1.size[1]/2
      title_font = pygame.font.SysFont(None, 100)

      # rec = pygame.Rect(100, 100, 50, 20)
      # surf = pygame.Surface((rec.width, rec.height))
      # surf.fill((255, 0, 0))
      while True:
            # keys = pygame.key.get_pressed()
            # mouse_pos = pygame.mouse.get_pos()
            # mouse_buttons = pygame.mouse.get_pressed()
            
            for event in pygame.event.get():
                  on_event(event)
                  # if event.type == pygame.MOUSEMOTION:
                        # mouse_pos = pygame.mouse.get_pos()

            # if keys[K_LEFT]:
                  # rec.move_ip(-10, 0)
            # elif keys[K_RIGHT]:
                  # rec.move_ip(10, 0)
            # elif keys[K_ESCAPE]:
                  # pass
            
            board.update()
            # piece.move()
            if gameState == False: # When the game is paused, i.e.: in the start menu
                  DISPLAYSURFACE.blit(img, (0, 0))
                  btn1.render()
                  f = title_font.render("pyChess", True, WHITE)
                  DISPLAYSURFACE.blit(f, (SCREEN_WIDTH/2 - f.get_width()/2, SCREEN_HEIGHT/4))
                  # DISPLAYSURFACE.blit(surf, (rec.x, rec.y) )
            else:
                  DISPLAYSURFACE.fill((200, 200, 200))
                  board.render(DISPLAYSURFACE)


            pygame.display.update()
            FramePerSec.tick(FPS)

