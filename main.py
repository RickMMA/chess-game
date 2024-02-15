import pygame, sys, os, copy
from pygame.locals import *
from menu_gui import Button
  
global rec, surf
global pressed_keys, pressed_mouse, mouse_pos
 
pygame.init()
pygame.display.init()

FPS = 30
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

TILE_DIMENSION = 32 # 32x32 pixels

rec = pygame.Rect(100, 100, 20, 20)
surf = pygame.Surface((rec.width, rec.height))
surf.fill((255, 0, 0))


            

def on_event(event):
    global gameState, mouse_pos, pressed_keys, pressed_mouse
    
    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pass
    elif event.type == pygame.MOUSEMOTION:
        # rec.move_ip(mouse_pos[0], mouse_pos[1])
        rec.x == mouse_pos[0]
        rec.y == mouse_pos[1]
        # DISPLAYSURFACE.blit(surf, (mouse_pos[0], mouse_pos[1]))
    elif event.type == pygame.KEYDOWN:
        if pressed_keys[K_q]:
            if gameState == True:
                gameState = False
            else:
                gameState = True
        elif pressed_keys[K_ESCAPE]:        
            print(mouse_pos)
        elif pressed_keys[K_LEFT]:
            rec.move_ip(-10, 0)

    pygame.event.pump()
                        
                        
                  
            
class chessPiece(pygame.sprite.Sprite):
    
    def __init__(self, pieceName):
        pygame.sprite.Sprite.__init__(self)

        self.piece = pieceName[0]
        self.pos = pieceName[1] # piece comes as a tuple eg: ("wP", (0, 0))
        if pieceName[0] != "--":
            self._image = pygame.image.load(
                os.path.join(os.getcwd(), "assets", "chess_pieces", f"{pieceName[0]}.png")).convert_alpha()
            self.image = pygame.transform.scale_by(self._image, 2)
        # self.rect = self.image.get_rect()
        # self.rect.center = (SCREEN_WIDTH-40,40) 
            
    def move(self):
        # self.rect.move_ip(0,10)
        pass
                  
    def render(self, surface):
        if self.piece != "--":
            surface.blit(self.image, (self.pos[0], self.pos[1]))
        else:
            pass

    def hello(self):
        print("hola", self.piece)


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
          self._image = pygame.image.load(os.path.join(os.getcwd(), "assets", "BOARD.png")).convert()
          self.image = pygame.transform.scale_by(self._image, 2)
          self.rect = self.image.get_rect()
          
          self.position = (SCREEN_WIDTH/10, SCREEN_HEIGHT/8)
          self.rect.topleft = self.position

          self.starting_board = {
              "A8":("bR", (self.rect.x + 0,   self.rect.y + 0)), "B8":("bN", (self.rect.x + 64,  self.rect.y + 0)),
              "C8":("bB", (self.rect.x + 128, self.rect.y + 0)), "D8":("bQ", (self.rect.x + 192, self.rect.y + 0)),
              "E8":("bK", (self.rect.x + 256, self.rect.y + 0)), "F8":("bB", (self.rect.x + 320, self.rect.y + 0)),
              "G8":("bN", (self.rect.x + 384, self.rect.y + 0)), "H8":("bR", (self.rect.x + 448, self.rect.y + 0)),
              
              "A7":("bP", (self.rect.x + 0,   self.rect.y + 64)), "B7":("bP", (self.rect.x + 64,  self.rect.y + 64)),
              "C7":("bP", (self.rect.x + 128, self.rect.y + 64)), "D7":("bP", (self.rect.x + 192, self.rect.y + 64)),
              "E7":("bP", (self.rect.x + 256, self.rect.y + 64)), "F7":("bP", (self.rect.x + 320, self.rect.y + 64)),
              "G7":("bP", (self.rect.x + 384, self.rect.y + 64)), "H7":("bP", (self.rect.x + 448, self.rect.y + 64)),
              
              "A6":("--", (self.rect.x + 0,   self.rect.y + 128)), "B6":("--", (self.rect.x + 64,  self.rect.y + 128)),
              "C6":("--", (self.rect.x + 128, self.rect.y + 128)), "D6":("--", (self.rect.x + 192, self.rect.y + 128)),
              "E6":("--", (self.rect.x + 256, self.rect.y + 128)), "F6":("--", (self.rect.x + 320, self.rect.y + 128)),
              "G6":("--", (self.rect.x + 384, self.rect.y + 128)), "H6":("--", (self.rect.x + 448, self.rect.y + 128)),
              
              "A5":("--", (self.rect.x + 0,   self.rect.y + 192)), "B5":("--", (self.rect.x + 64,  self.rect.y + 192)),
              "C5":("--", (self.rect.x + 128, self.rect.y + 192)), "D5":("--", (self.rect.x + 192, self.rect.y + 192)),
              "E5":("--", (self.rect.x + 256, self.rect.y + 192)), "F5":("--", (self.rect.x + 320, self.rect.y + 192)),
              "G5":("--", (self.rect.x + 384, self.rect.y + 192)), "H5":("--", (self.rect.x + 448, self.rect.y + 192)),
              
              "A4":("--", (self.rect.x + 0,   self.rect.y + 256)), "B4":("--", (self.rect.x + 64,  self.rect.y + 256)),
              "C4":("--", (self.rect.x + 128, self.rect.y + 256)), "D4":("--", (self.rect.x + 192, self.rect.y + 256)),
              "E4":("--", (self.rect.x + 256, self.rect.y + 256)), "F4":("--", (self.rect.x + 320, self.rect.y + 256)),
              "G4":("--", (self.rect.x + 384, self.rect.y + 256)), "H4":("--", (self.rect.x + 448, self.rect.y + 256)),
              
              "A3":("--", (self.rect.x + 0,   self.rect.y + 320)), "B3":("--", (self.rect.x + 64,  self.rect.y + 320)),
              "C3":("--", (self.rect.x + 128, self.rect.y + 320)), "D3":("--", (self.rect.x + 192, self.rect.y + 320)),
              "E3":("--", (self.rect.x + 256, self.rect.y + 320)), "F3":("--", (self.rect.x + 320, self.rect.y + 320)),
              "G3":("--", (self.rect.x + 384, self.rect.y + 320)), "H3":("--", (self.rect.x + 448, self.rect.y + 320)),
              
              "A2":("wP", (self.rect.x + 0,   self.rect.y + 384)), "B2":("wP", (self.rect.x + 64,  self.rect.y + 384)),
              "C2":("wP", (self.rect.x + 128, self.rect.y + 384)), "D2":("wP", (self.rect.x + 192, self.rect.y + 384)),
              "E2":("wP", (self.rect.x + 256, self.rect.y + 384)), "F2":("wP", (self.rect.x + 320, self.rect.y + 384)),
              "G2":("wP", (self.rect.x + 384, self.rect.y + 384)), "H2":("wP", (self.rect.x + 448, self.rect.y + 384)),

              "A1":("wB", (self.rect.x + 0,   self.rect.y + 448)), "B1":("wN", (self.rect.x + 64,  self.rect.y + 448)),
              "C1":("wB", (self.rect.x + 128, self.rect.y + 448)), "D1":("wQ", (self.rect.x + 192, self.rect.y + 448)),
              "E1":("wK", (self.rect.x + 256, self.rect.y + 448)), "F1":("wB", (self.rect.x + 320, self.rect.y + 448)),
              "G1":("wN", (self.rect.x + 384, self.rect.y + 448)), "H1":("wR", (self.rect.x + 448, self.rect.y + 448))
          }

              
          self.current_board = {}


 
      def render(self, surface):
          surface.blit(self.image, self.rect) # board image
          
          x = 0
          y = 0
          letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
          numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
          for i in range(len(letters)):
              font_l = FONT.render(letters[i], False, WHITE)
              font_n = FONT.render(numbers[i], False, WHITE)
              surface.blit(font_l, (self.position[0] + 20 + x, self.position[1] - 50))
              surface.blit(font_n, (self.position[0] - 50, self.position[1] + 15 + y))
              x += 64
              y += 64

              
            



if __name__ == "__main__":
    board = chessBoard()

    boardState = board.starting_board

    # menu background image 
    img = pygame.image.load(os.path.join(os.getcwd(), "assets", "chess-1280.jpg")).convert()
    img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
      
    btn1 = Button(DISPLAYSURFACE, pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text="Jugar", font=FONT)
    btn1.x = SCREEN_WIDTH/2 - btn1.size[0]/2  # centers button
    btn1.y = SCREEN_HEIGHT/2 - btn1.size[1]/2
    title_font = pygame.font.SysFont(None, 100)

    for keys, content in board.starting_board.items(): # fill the board with chessPiece object
        board.current_board[keys] = chessPiece(content)


    while True:            
        for event in pygame.event.get():
            on_event(event)            
        
        
        if gameState == False: # When the game is paused, i.e.: in the start menu
            DISPLAYSURFACE.blit(img, (0, 0))
            btn1.render()
            f = title_font.render("pyChess", True, WHITE)
            DISPLAYSURFACE.blit(f, (SCREEN_WIDTH/2 - f.get_width()/2, SCREEN_HEIGHT/4))
            
        else:
            DISPLAYSURFACE.fill((200, 200, 200))
            board.render(DISPLAYSURFACE)
            for keys, content in board.starting_board.items():
                board.current_board[keys].render(DISPLAYSURFACE)


        rec.x = mouse_pos[0] - 10
        rec.y = mouse_pos[1] - 10
        DISPLAYSURFACE.blit(surf, (rec.x, rec.y))
        
        pygame.display.update()
        FramePerSec.tick(FPS)
