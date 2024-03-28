import pygame, sys, os, copy
from pygame.locals import *
from menu_gui import Button
from engine import *
  
global rec, surf
global pressed_keys, pressed_mouse, mouse_pos
 
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
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

DISPLAYSURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chess Game")

FONT = pygame.font.SysFont(None, 48)

TILE_DIMENSION = 32 # 32x32 pixels

rec = pygame.Rect(100, 100, 20, 20) # mouse collision detection
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
        pass
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

    
    print(dir(board.current_board["A1"]))
    # print(board.current_board["A1"].image.collide)
    while True:
        
        for event in pygame.event.get():
            on_event(event)            
        
        
        if gameState == False: # When the game is paused, i.e.: in the start menu
            DISPLAYSURFACE.blit(img, (0, 0))
            btn1.render()
            if btn1.click_button() == True:
                gameState = True
            f = title_font.render("pyChess", True, WHITE)
            DISPLAYSURFACE.blit(f, (SCREEN_WIDTH/2 - f.get_width()/2, SCREEN_HEIGHT/4))
            
        elif gameState == True:
            DISPLAYSURFACE.fill((200, 200, 200))
            board.render(DISPLAYSURFACE)
            for keys, content in board.starting_board.items():
                board.current_board[keys].render(DISPLAYSURFACE)
                _rec = board.current_board['A1'].rect

                # if _rec.collidepoint(mouse_pos[0], mouse_pos[1] and pressed_mouse[0] == 1:
                # if pressed_mouse[0] == 1:
                    # print("yes")                                    
    

            # if i want to test collision with mouse position
            # print( _rec.collidepoint(mouse_pos[0], mouse_pos[1]))
            

        rec.x = mouse_pos[0] - 10
        rec.y = mouse_pos[1] - 10
        DISPLAYSURFACE.blit(surf, (rec.x, rec.y))
        
        pygame.display.update()
        FramePerSec.tick(FPS)
