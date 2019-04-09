#code = utf-8
import pygame

# 导入按键的检测
from pygame.locals  import *

if __name__ == '__main__':
	#1. 创建一个窗口， 用来显示内容
	screen = pygame.display.set_mode((480, 890), 0, 32) # 创建屏幕 （（屏幕大小）, 0, 32）

	#2. 创建一个和窗口大小的图片，用来充当
	bgImgeFile = './image/background.png'

	# 创建一个玩家飞机的图片

	hero = pygame.image.load('./image/hero.gif').convert()
	
	print()
	return 
	background = pygame.image.load(bgImgeFile).convert()

	# 显示背景 
	# screen.blit(background, (0,0))
	# pygame.display.update()
	# 2. 步骤1 显示背景  一闪而过 

	#3. 把背景图片放到窗口中显示
	x,y = 420,0
	while True:
		screen.blit(background, (0,0))
		screen.blit(hero, (x,y))

		for event in pygame.event.get():
			if event.type == QUIT:
				print('exit')
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					print('left')
					x -= 10
				
				elif event.key == K_d or event.key == K_RIGHT:
					x += 10
					print('right')

				elif event.key == K_s or event.key == K_DOWN:
					print('down')

				elif event.key == K_w or event.key == K_UP:
					print('up')

				elif event.key == K_SPACE:
					print('space')
		pygame.display.update()