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
              
    def asd(self):
        pass
        pass


              
class chessPiece(pygame.sprite.Sprite):
    def __init__(self, piece):
        pygame.sprite.Sprite.__init__(self)
        self._piece = piece

        self.pieceName = piece[0] # piece comes as a tuple eg: ("wP", (0, 0))
                                  # where index 0 is the piece, and index 1 is position

        # default image size
        self._default_image = pygame.image.load(
                os.path.join(os.getcwd(), "assets", "chess_pieces", "bK.png")).convert_alpha()
        self._default_image_size = self._default_image.get_size()
        
        self.is_clicked = False
        self.pos = piece[1]   # pos is a tuple (x, y)
        if piece[0] != "--":
            self._image = pygame.image.load(
                os.path.join(os.getcwd(), "assets", "chess_pieces", f"{piece[0]}.png")).convert_alpha()
            self.rect = pygame.Rect((self.pos[0], self.pos[1]),
                (self._image.get_size()[0], self._image.get_size()[1]))
        else:
            self._image = pygame.image.load(
                os.path.join(os.getcwd(), "assets", "chess_pieces", f"empty.png")).convert_alpha()
            # Insert rect when there is no piece
            self.rect = pygame.Rect((self.pos[0], self.pos[1]),
                (self._default_image_size[0], self._default_image_size[1])) 
            

            
    def render(self, surface):
        if self.pieceName != "--":
            surface.blit(self._image, (self.pos[0], self.pos[1]))
        else:
            pass

    def clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        right_click = pygame.mouse.get_pressed()[1]

        self.is_clicked = False
        if self.rect.collidepoint(mouse_pos):
            if left_click == 1 and self.is_clicked == False:
                # yes you clicked the piece
                t = (True, (self.pieceName, self.pos))
                return t

