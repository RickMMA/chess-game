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

rec = pygame.Rect(100, 100, 50, 20)
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
            self.image = pygame.image.load(
                os.path.join(os.getcwd(), "assets", "chess_pieces", f"{pieceName[0]}.png")).convert_alpha()
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
          self.image = pygame.image.load(os.path.join(os.getcwd(), "assets", "BOARD.png")).convert()
          self.brownTile = pygame.image.load(os.path.join(os.getcwd(), "assets", "brown-tile.png")).convert()
          self.whiteTile = pygame.image.load(os.path.join(os.getcwd(), "assets", "white-tile.png")).convert()
          self.rect = self.image.get_rect()
          
          self.position = (SCREEN_WIDTH/10, SCREEN_HEIGHT/8)
          self.rect.topleft = self.position

          self.starting_board = {
              "A8":("bR", (self.rect.x + 0,   self.rect.y + 0)), "B8":("bN", (self.rect.x + 32,  self.rect.y + 0)),
              "C8":("bB", (self.rect.x + 64,  self.rect.y + 0)), "D8":("bQ", (self.rect.x + 96,  self.rect.y + 0)),
              "E8":("bK", (self.rect.x + 128, self.rect.y + 0)), "F8":("bB", (self.rect.x + 160, self.rect.y + 0)),
              "G8":("bN", (self.rect.x + 192, self.rect.y + 0)), "H8":("bR", (self.rect.x + 224, self.rect.y + 0)),
              
              "A7":("bP", (self.rect.x + 0,   self.rect.y + 32)), "B7":("bP", (self.rect.x + 32,  self.rect.y + 32)),
              "C7":("bP", (self.rect.x + 64,  self.rect.y + 32)), "D7":("bP", (self.rect.x + 96,  self.rect.y + 32)),
              "E7":("bP", (self.rect.x + 128, self.rect.y + 32)), "F7":("bP", (self.rect.x + 160, self.rect.y + 32)),
              "G7":("bP", (self.rect.x + 192, self.rect.y + 32)), "H7":("bP", (self.rect.x + 224, self.rect.y + 32)),
              
              "A6":("--", (self.rect.x + 0,   self.rect.y + 64)), "B6":("--", (self.rect.x + 32,  self.rect.y + 64)),
              "C6":("--", (self.rect.x + 64,  self.rect.y + 64)), "D6":("--", (self.rect.x + 96,  self.rect.y + 64)),
              "E6":("--", (self.rect.x + 128, self.rect.y + 64)), "F6":("--", (self.rect.x + 160, self.rect.y + 64)),
              "G6":("--", (self.rect.x + 192, self.rect.y + 64)), "H6":("--", (self.rect.x + 224, self.rect.y + 64)),
              
              "A5":("--", (self.rect.x + 0,   self.rect.y + 96)), "B5":("--", (self.rect.x + 32,  self.rect.y + 96)),
              "C5":("--", (self.rect.x + 64,  self.rect.y + 96)), "D5":("--", (self.rect.x + 96,  self.rect.y + 96)),
              "E5":("--", (self.rect.x + 128, self.rect.y + 96)), "F5":("--", (self.rect.x + 160, self.rect.y + 96)),
              "G5":("--", (self.rect.x + 192, self.rect.y + 96)), "H5":("--", (self.rect.x + 224, self.rect.y + 96)),
              
              "A4":("--", (self.rect.x + 0,   self.rect.y + 128)), "B4":("--", (self.rect.x + 32,  self.rect.y + 128)),
              "C4":("--", (self.rect.x + 64,  self.rect.y + 128)), "D4":("--", (self.rect.x + 96,  self.rect.y + 128)),
              "E4":("--", (self.rect.x + 128, self.rect.y + 128)), "F4":("--", (self.rect.x + 160, self.rect.y + 128)),
              "G4":("--", (self.rect.x + 192, self.rect.y + 128)), "H4":("--", (self.rect.x + 224, self.rect.y + 128)),
              
              "A3":("--", (self.rect.x + 0,   self.rect.y + 160)), "B3":("--", (self.rect.x + 32,  self.rect.y + 160)),
              "C3":("--", (self.rect.x + 64,  self.rect.y + 160)), "D3":("--", (self.rect.x + 96,  self.rect.y + 160)),
              "E3":("--", (self.rect.x + 128, self.rect.y + 160)), "F3":("--", (self.rect.x + 160, self.rect.y + 160)),
              "G3":("--", (self.rect.x + 192, self.rect.y + 160)), "H3":("--", (self.rect.x + 224, self.rect.y + 160)),
              
              "A2":("wP", (self.rect.x + 0,   self.rect.y + 192)), "B2":("wP", (self.rect.x + 32,  self.rect.y + 192)),
              "C2":("wP", (self.rect.x + 64,  self.rect.y + 192)), "D2":("wP", (self.rect.x + 96,  self.rect.y + 192)),
              "E2":("wP", (self.rect.x + 128, self.rect.y + 192)), "F2":("wP", (self.rect.x + 160, self.rect.y + 192)),
              "G2":("wP", (self.rect.x + 192, self.rect.y + 192)), "H2":("wP", (self.rect.x + 224, self.rect.y + 192)),

              "A1":("wB", (self.rect.x + 0,   self.rect.y + 224)), "B1":("wN", (self.rect.x + 32,  self.rect.y + 224)),
              "C1":("wB", (self.rect.x + 64,  self.rect.y + 224)), "D1":("wQ", (self.rect.x + 96,  self.rect.y + 224)),
              "E1":("wK", (self.rect.x + 128, self.rect.y + 224)), "F1":("wB", (self.rect.x + 160, self.rect.y + 224)),
              "G1":("wN", (self.rect.x + 192, self.rect.y + 224)), "H1":("wR", (self.rect.x + 224, self.rect.y + 224))
          }

              
          self.current_board = {}


 
      def update(self):
          pass
      
 
      def render(self, surface):
          font = FONT.render("HOLA MUNDO", False, WHITE)
            
          surface.blit(self.image, self.rect) # board image
          surface.blit(font, (self.position[0], self.position[1]))





if __name__ == "__main__":
    board = chessBoard()

    boardState = board.starting_board

    img = pygame.image.load(os.path.join(os.getcwd(), "assets", "chess-1280.jpg")).convert()
    img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
      
    btn1 = Button(DISPLAYSURFACE, pos = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), text="Jugar", font=FONT)
    btn1.x = SCREEN_WIDTH/2 - btn1.size[0]/2  # centers button
    btn1.y = SCREEN_HEIGHT/2 - btn1.size[1]/2
    title_font = pygame.font.SysFont(None, 100)

    for keys, content in board.starting_board.items(): # fill the board with chessPiece object
        board.current_board[keys] = chessPiece(content)

    print(board.current_board["A1"].pos)

        
        
    while True:            
        for event in pygame.event.get():
            on_event(event)

        # board.update()
        # piece.move()
        if gameState == False: # When the game is paused, i.e.: in the start menu
            DISPLAYSURFACE.blit(img, (0, 0))
            btn1.render()
            f = title_font.render("pyChess", True, WHITE)
            DISPLAYSURFACE.blit(f, (SCREEN_WIDTH/2 - f.get_width()/2, SCREEN_HEIGHT/4))
            # DISPLAYSURFACE.blit(surf, (rec.x, rec.y))
            pygame.draw.circle(DISPLAYSURFACE, "red", (mouse_pos[0], mouse_pos[1]), 30, 0)
        else:
            DISPLAYSURFACE.fill((200, 200, 200))
            board.render(DISPLAYSURFACE)
            for keys, content in board.starting_board.items():
                board.current_board[keys].render(DISPLAYSURFACE)


        pygame.display.update()
        FramePerSec.tick(FPS)
