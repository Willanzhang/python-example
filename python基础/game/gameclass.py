#code = utf-8
import pygame
import random
import time
# 导入按键的检测
from pygame.locals  import *

class HeroPlane(object):

	def __init__(self,screen):
		# 设置飞机的默认位置
		self.x = 230
		self.y = 600
		self.screen = screen
		self.imagePath = './image/hero.gif'
		self.image = pygame.image.load(self.imagePath).convert()
		self.bullet = []

	def display(self):
		self.screen.blit(self.image,(self.x, self.y))
		for bullet in self.bullet[:]:
			if bullet.judgeOut():
				self.bullet.remove(bullet)
			bullet.display()
			bullet.run()
	
	def moveLeft(self):
		self.x -= 10

	def moveRight(self):
		self.x += 10
	# 设计
	def shoot(self):
		# b = Bullt(self.screen, self.x, self.y)
		newBullet = Bullt(self.screen, self.x, self.y)
		newBullet.display()
		self.bullet.append(newBullet)
		# if len(self.bullet) > 0:
		# 	pass

class Bullt(object):
	def __init__(self, screen, x, y):
		self.x = x + 37
		self.y = y - 20
		self.screen = screen
		self.imagePath = './image/bullet-3.gif'
		self.image = pygame.image.load(self.imagePath).convert()

	def judgeOut(self):
		return self.y < 0

	def display(self):
		# self.y -= 10
		self.screen.blit(self.image,(self.x, self.y))
	
	def run(self):
		self.y -= 1
		# self.screen.blit(self.image,(self.x, self.y))

class EnemyBullt(object):
	def __init__(self, screen, x, y):
		self.x = x + 25
		self.y = y + 30
		self.screen = screen
		self.imagePath = './image/bullet-1.gif'
		self.image = pygame.image.load(self.imagePath).convert()

	def judgeOut(self):
		return self.y > 890

	def display(self):
		# self.y -= 10
		# print('shoot')
		self.screen.blit(self.image,(self.x, self.y))
	
	def run(self):
		self.y += 1
		# self.screen.blit(self.image,(self.x, self.y))
			
class CreateGround(object):
	def  __init__(self, screen):
		self.x = 0
		self.y = 0
		self.screen = screen
		self.imagePath = './image/background.png'
		self.image = pygame.image.load(self.imagePath).convert()

	def display(self):
		screen.blit(self.image, (self.x, self.y))

class EnemyPlane(object):

	def __init__(self,screen):
		self.x = random.randint(0, 480)
		self.y = 0
		self.bullet = []
		self.direction = 'right'
		self.screen = screen
		self.imagePath = './image/enemy-1.gif'
		self.image = pygame.image.load(self.imagePath).convert()
	

	def display(self):
		self.screen.blit(self.image,(self.x, self.y))
		for bullet in self.bullet[:]:
			if bullet.judgeOut():
				self.bullet.remove(bullet)
			bullet.display()
			bullet.run()
	
	# 设计
	def shoot(self):
		# b = Bullt(self.screen, self.x, self.y)
		num = random.randint(1,800)
		if num == 8:
			newBullet = EnemyBullt(self.screen, self.x, self.y)
			newBullet.display()
			self.bullet.append(newBullet)
		# if len(self.bullet) > 0:
		# 	pass
	
	def move(self):
		print('move')
		if self.direction == 'left':
			self.x -= 0.1
		elif self.direction == 'right':
			self.x += 0.1

		if self.x <= 0:
			self.direction = 'right'
		elif self.x >= 480 - 50:
			self.direction = 'left'

	def judgeOut(self):
		return self.y >= 890

if __name__ == '__main__':
	#1. 创建一个窗口， 用来显示内容
	screen = pygame.display.set_mode((480, 890), 0, 32) # 创建屏幕 （（屏幕大小）, 0, 32）

	#2. 创建一个和窗口大小的图片，用来充当
	background = CreateGround(screen)
	# background = pygame.image.load(bgImgeFile).convert()

	# 创建一个玩家飞机的对象
	heroPlane = HeroPlane(screen)

	# 创建一个敌人飞机
	enemyPlaneList = []
	enemyPlane = EnemyPlane(screen)
	# b = Bullt(screen, 400, 300)
	# 显示背景
	# screen.blit(background, (0,0))
	# pygame.display.update()
	# 2. 步骤1 显示背景  一闪而过

	#3. 把背景图片放到窗口中显示
	while True:
		background.display()
		heroPlane.display()

		enemyPlane.display()
		enemyPlane.move()
		enemyPlane.shoot()
		# if len(enemyPlaneList) <= 4:
		# 	time.sleep(1)
		# 	enemyPlane = EnemyPlane(screen)
		# 	enemyPlaneList.append(enemyPlane)
		# # 移除飞机
		# for plane in enemyPlaneList[:]:
		# 	plane.display()
		# 	plane.move()
		# 	if plane.judgeOut:
		# 		enemyPlaneList.remove(plane)
		# b.display()

		for event in pygame.event.get():
			if event.type == QUIT:
				print('exit')
				exit()
			elif event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					heroPlane.moveLeft()
					print('left')
				
				elif event.key == K_d or event.key == K_RIGHT:
					heroPlane.moveRight()
					print('right')

				elif event.key == K_s or event.key == K_DOWN:
					print('down')

				elif event.key == K_w or event.key == K_UP:
					print('up')

				elif event.key == K_SPACE:
					heroPlane.shoot()
					print('space')
		pygame.display.update()