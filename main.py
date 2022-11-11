import pygame
from pygame.locals import*

pygame.init()
# set screen width and height
X=600
Y=600
# width of each cube
diff=X/9

# initialise the screeen
screen = pygame.display.set_mode((X,Y))

# set the caption
pygame.display.set_caption(" SUDOKU SOLVER ")

# Draw the sudoku board
def Drawgrid():
    for i in range(10):
        
        if i%3==0:
            thick=8
        else:
            thick=1
        pygame.draw.line(screen,(1,1,1),(0,i*diff),(600,i*diff),thick)
        pygame.draw.line(screen,(1,1,1),(i*diff,0),(i*diff,600),thick)




running=True

font= pygame.font.Font("freesansbold.ttf",32)

text = font.render("Hello world",True,(240,0,233),(0,0,0))

text_rect= text.get_rect()
text_rect.center=(400,300)

while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                running=False
        elif event.type == QUIT:
            running=False
    Drawgrid()
    pygame.display.flip()


