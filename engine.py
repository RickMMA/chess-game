from main import *

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
          numbers = ['8', '7', '6', '5', '4', '3', '2', '1']
          for i in range(len(letters)):
              font_l = FONT.render(letters[i], False, WHITE)
              font_n = FONT.render(numbers[i], False, WHITE)
              surface.blit(font_l, (self.position[0] + 20 + x, self.position[1] - 50))
              surface.blit(font_n, (self.position[0] - 50, self.position[1] + 15 + y))
              x += 64
              y += 64

              class chessPiece(pygame.sprite.Sprite):
    
    def __init__(self, pieceName):
        pygame.sprite.Sprite.__init__(self)

        self.piece = pieceName[0] # piece comes as a tuple eg: ("wP", (0, 0))
                                  # where index 0 is the piece, and index 1 is position

        self.pos = pieceName[1]   # pos is a tuple (x, y)
        if pieceName[0] != "--":
            self._image = pygame.image.load(
                os.path.join(os.getcwd(), "assets", "chess_pieces", f"{pieceName[0]}.png")).convert_alpha()
            self.image = pygame.transform.scale_by(self._image, 2)
            self.rect = pygame.Rect((self.pos[0], self.pos[1]), (self.image.get_size()[0], self.image.get_size()[1]))
            
    def render(self, surface):
        if self.piece != "--":
            surface.blit(self.image, (self.pos[0], self.pos[1]))
        else:
            pass


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

