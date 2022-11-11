import pygame
from pygame.locals import*

class Square(pygame.sprite.Sprite):
	def __init__(self):
		super(Square, self).__init__()
		self.surf = pygame.Surface((25, 25))
		self.surf.fill((0, 200, 255))
		self.rect = self.surf.get_rect()


pygame.init()
screen = pygame.display.set_mode((800,600))

square1= Square()

running=True

font= pygame.font.Font("freesansbold.ttf",32)

text = font.render("Hello world",True,(240,0,233),(0,0,0))

text_rect= text.get_rect()
text_rect.center=(400,300)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                running=False
        elif event.type == QUIT:
            running=False
    screen.blit(square1.surf,(250,240))
    screen.blit(text,text_rect)

    pygame.display.flip()


