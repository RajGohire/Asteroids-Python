from Constants import *
# from numpy import add
from time import time
from Bullets import *

class Ship():
	def __init__(self):
		self.nlines = 6
		# self.lines = malloc(sizeof(vec2f_t) * 2 * ship->nlines) // Two coords per line
		self.lines = [[0, -15], [10, 10], [2, 4], [-2, 4], [-10, 10], [0, -15]]
		self.bullets = []
		# self.bullets_order = [-1] * MAX_BULLETS
		self.offset = [SCREENWIDTH/2,SCREENHEIGHT/2]
		self.theta = 0
		self.velocity = [0,0]
		self.lives = NUM_LIVES
		self.score = 0
		
		# self.lines.append([0,-15])
		# self.lines.append([10,10])
		# self.lines.append([2,4])
		# self.lines.append([-2,4])
		# self.lines.append([-10,10])
		# self.lines.append([0,-15])

		'''# self.lines.append(add(self.offset, [0,15]))
		# self.lines.append(add(self.offset, [-10,10]))
		self.lines.append([a+b for a,b in zip(self.offset, [0,-15])])
		self.lines.append([a+b for a,b in zip(self.offset, [10,10])])
		# self.lines.append(add(self.offset, [10,10]))
		self.lines.append([a+b for a,b in zip(self.offset, [2,4])])
		self.lines.append([a+b for a,b in zip(self.offset, [-2,4])])
		self.lines.append([a+b for a,b in zip(self.offset, [-10,10])])
		self.lines.append([a+b for a,b in zip(self.offset, [0,-15])])
		# self.lines.append(add(self.offset, [2,4]))
		# self.lines.append(add(self.offset, [-2,4]))
		# self.lines.append(add(self.offset, [-4,5]))
		# self.lines.append(add(self.offset, [4,5]))'''
	
	def move(self, deltaTime):
		costheta = cos(self.theta)
		sintheta = sin(self.theta)
		
		dx = sintheta * deltaTime * SHIP_SPEED
		dy = -costheta * deltaTime * SHIP_SPEED

		self.velocity[0] += dx
		self.velocity[1] += dy
		# ship->lines[11] = (vec2f_t){0,13};
    	# ship->lines[13] = (vec2f_t){0,13};

	def rotate(self, deltaTime, dir):
		self.theta += dir * deltaTime/300
	
	def update(self):
		self.velocity[0] *= DECELERATION_VELOCITY
		self.velocity[1] *= DECELERATION_VELOCITY
		self.offset[0] += self.velocity[0]
		self.offset[1] += self.velocity[1]
		
		if (self.offset[0] > SCREENWIDTH): self.offset[0] = 0
		if (self.offset[0] < 0): self.offset[0] = SCREENWIDTH
		if (self.offset[1] > SCREENHEIGHT): self.offset[1] = 0
		if (self.offset[1] < 0): self.offset[1] = SCREENHEIGHT
	
	def hyperdrive(self):
		self.offset = [randint(0,RAND_MAX) % SCREENWIDTH, randint(0,RAND_MAX) % SCREENHEIGHT]
		# self.velocity = [0,0]
	
	def shoot(self):
		x = sin(self.theta) * BULLET_SPEED
		y = -cos(self.theta) * BULLET_SPEED
		newBullet = Bullet(self.offset, [x,y], self.theta, time())
		
		if (len(self.bullets) >= MAX_BULLETS):
			self.free_bullet(0)
		self.bullets.append(newBullet)
	
	def free_bullet(self, i):
		_ = self.bullets.pop(i)
		del (_)

	def destroy(self):
		self.lines.clear()
		self.bullets.clear()
		if (self.lives > 0):
			currentLives = self.lives
			currentScore = self.score
			self.__init__()
			self.lives = currentLives
			self.score = currentScore