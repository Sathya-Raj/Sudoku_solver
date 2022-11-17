import pygame
import math
from pygame.locals import*

pygame.init()
# set screen width and height
X=600
Y=600
# width of each cube
diff=X/9
# co-ordinates of the selected box
x=0
y=0
# initialise the screeen
screen = pygame.display.set_mode((X,700))

# set the caption
pygame.display.set_caption(" SUDOKU SOLVER ")

# The default board 
grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

font_sm2 =pygame.font.SysFont("comicsans",16)
font_sm =pygame.font.SysFont("comicsans",20)

# Draw the sudoku board
def Drawgrid():
    for  i in range(9):
        for j in range(9):
            if not grid[i][j]==0:
                pygame.draw.rect(screen,(0,153,153),(j*diff,i*diff,diff+1,diff+1))
                # render the text in the grid 
                text= font_sm.render(str(grid[i][j]),1,(0,0,0))
                screen.blit(text,(j*diff+18,i*diff+18))

    for i in range(10):
        if i%3==0:
            thick=5
        else:
            thick=1
        pygame.draw.line(screen,(0,0,0),(0,i*diff),(600,i*diff),thick)
        pygame.draw.line(screen,(0,0,0),(i*diff,0),(i*diff,600),thick)

# get the click position
def get_cord(pos):
    global x,y

    if pos[1]<=Y:
        x=math.floor(pos[1]/diff)
        y=math.floor(pos[0]/diff)


# Higlight the selected box
def Select_box(x,y):
    for i in range(2):
        pygame.draw.line(screen,(255,0,0),((i+y)*diff,x*diff),((i+y)*diff,(x*diff)+diff),5)
        pygame.draw.line(screen,(255,0,0),(y*diff,(i+x)*diff),((y*diff)+diff,(i+x)*diff),5)
        
# putting the selected val
def putVal(val,row,col,delay):
    text1 = font_sm2.render("INVALID ENTRY !! ", 1, (255, 0, 0))
    text= font_sm.render(str(val),1,(255,0,0))
    screen.blit(text1, (20, 620))       
    screen.blit(text,(row*diff+18,col*diff+18))
    Drawgrid()
    pygame.display.update()
    pygame.time.delay(delay)
    

# check if the entered value is valid
def isValid(val,grid,row,col):
    for i in range(9):
        if grid[row][i]==val:
            return False
        if grid[i][col]==val:
            return False
        if grid[(row//3)*3+(i//3)][(col//3)*3+(i%3)]==val:
            return False
    return True

# solve the grid
def solve():
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                Select_box(row,col)
                
                for num in range(1,10):
                    if isValid(num,grid,row,col):
                        grid[row][col]=num
                        screen.fill((255,255,255))
                        Drawgrid()
                        Select_box(row,col)
                        pygame.display.update()
                        pygame.time.delay(80)
                        if solve():
                            return True
                        else:
                            grid[row][col]=0
                            Drawgrid()
                    
                return False
    return True

# Display instruction for the game
def instruction():
    text1 = font_sm2.render("CONTROLS : D - DEFAULT GRID / R - RESET / 1-9 - VALUES / C- CLEAR", 1, (0, 0, 255))
    text2 = font_sm2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE :)", 1, (0, 0, 255))
    screen.blit(text1, (20, 620))       
    screen.blit(text2, (20, 650))

running=True

font= pygame.font.Font("freesansbold.ttf",32)

text = font.render("Hello world",True,(240,0,233),(0,0,0))

text_rect= text.get_rect()
text_rect.center=(400,300)

box_selected=False

val=0


while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if event.key == K_LEFT:
                if y>0 :
                    y-=1
                box_selected=True
            if event.key == K_RIGHT:
                if  y<8:
                    y+=1
                box_selected=True
            if event.key == K_DOWN:
                if  x<8:
                    x+=1
                box_selected=True
            if event.key == K_UP:
                if x>0:
                    x-=1
                box_selected=True
            if event.key == K_c:
                grid[int(x)][int(y)]=0
            if event.key == K_1:
                val=1
            if event.key == K_2:
                val=2
            if event.key == K_3:
                val=3
            if event.key == K_4:
                val=4
            if event.key == K_5:
                val=5
            if event.key == K_6:
                val=6
            if event.key == K_7:
                val=7
            if event.key == K_8:
                val=8
            if event.key == K_9:
                val=9
            if event.key ==K_r:
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
                box_selected=False
            if event.key ==K_d:
                grid =[
                [7, 8, 0, 4, 0, 0, 1, 2, 0],
                [6, 0, 0, 0, 7, 5, 0, 0, 9],
                [0, 0, 0, 6, 0, 1, 0, 7, 8],
                [0, 0, 7, 0, 4, 0, 2, 6, 0],
                [0, 0, 1, 0, 5, 0, 9, 3, 0],
                [9, 0, 4, 0, 6, 0, 0, 0, 5],
                [0, 7, 0, 3, 0, 0, 0, 1, 2],
                [1, 2, 0, 0, 0, 7, 4, 0, 0],
                [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
                box_selected=False
            if event.key == K_RETURN:
                solve()
        
        if not val==0 :
            if isValid(val,grid,int(x),int(y)):
                grid[int(x)][int(y)]=val
            else :
                putVal(val,y,x,800)
            
            val=0
        if event.type == pygame.MOUSEBUTTONDOWN:
            box_selected=True
            pos=pygame.mouse.get_pos()
            get_cord(pos)            
            
            
        if event.type == QUIT:
            running=False
    Drawgrid()
    if box_selected:
        Select_box(x,y)
        
    instruction()
    pygame.display.update()

pygame.quit()


