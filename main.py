import sys
import random
import pygame
from pygame.rect import Rect

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 640, 1028
FPS = 30
NAME = "Cookie Miner"
BG_COLOR = (50, 50, 150)
COOKIE = pygame.image.load("cookie.png")
BG = pygame.image.load("bg.png")
C_WIDTH = 64
C_HEIGHT = 64
x = WIDTH / 2 - C_WIDTH
y = HEIGHT / 2 - C_HEIGHT
score = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption(NAME)
clock = pygame.time.Clock()
pixelfont = pygame.font.Font('PixelFont.ttf', 50)
hitsound = pygame.mixer.Sound("point.ogg")

running = True
while running:
	
	clock.tick(FPS)
	
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(event.pos, x, y)
			if event.pos[0] > x and event.pos[0] < (x + C_WIDTH) and event.pos[1] > y and event.pos[1] < (y + C_HEIGHT):
				score += 1
				x = random.randint(0, (WIDTH - C_WIDTH))
				y = random.randint(0, (HEIGHT - C_HEIGHT))
				hitsound.play()
	
	score_label = pixelfont.render(f"Score: {str(score)}", False, (255, 255, 255))
	screen.blit(BG,  (0, 0))
	screen.blit(COOKIE, (x, y))
	screen.blit(score_label, (3, 1))
	pygame.display.flip()

pygame.quit()