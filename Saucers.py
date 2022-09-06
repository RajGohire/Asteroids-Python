from Constants import *
from time import time
from Bullets import *

class Saucer():
	def __init__(self, size):
		self.nlines = 20
		self.lines = []
		self.extremes = []
		self.offset = [(randint(0,RAND_MAX) % SCREENWIDTH) - SCREENWIDTH,
					(randint(0,RAND_MAX) % SCREENHEIGHT) - SCREENHEIGHT]	# Spawns on the sides of the screen
		self.size = size
		self.theta = 0
		self.bullets = []
		# self.bulletsOrder = [-1] * MAX_SAUCER_BULLETS

		match (size):
			case ('SAUCER_SMALL'):
				self.velocity = [(SAUCER_SPEED*randint(0,RAND_MAX)/RAND_MAX)-SAUCER_SPEED_SMALL, 0]
				self.lines.append([8,-4])
				self.lines.append([-8,-4])
				self.lines.append([-8,-4])
				self.lines.append([-20,4])
				self.lines.append([-20,4])
				self.lines.append([20,4])
				self.lines.append([20,4])
				self.lines.append([8,12])
				self.lines.append([8,12])
				self.lines.append([-8,12])
				self.lines.append([-8,12])
				self.lines.append([-20,4])
				self.lines.append([-8,-4])
				self.lines.append([-4,-12])
				self.lines.append([-4,-12])
				self.lines.append([4,-12])
				self.lines.append([4,-12])
				self.lines.append([8,-4])
				self.lines.append([8,-4])
				self.lines.append([20,4])
				self.extremes.append(-20) 	# Min x
				self.extremes.append(-12)	# Min y
				self.extremes.append(20)	# Max x
				self.extremes.append(12)	# Max y
			case ('SAUCER_LARGE'):
				self.velocity = [(SAUCER_SPEED*randint(0,RAND_MAX)/RAND_MAX)-SAUCER_SPEED_LARGE, 0]
				self.lines.append([-16,-8])
				self.lines.append([16,-8])
				self.lines.append([16,-8])
				self.lines.append([40,8])
				self.lines.append([40,8])
				self.lines.append([-40,8])
				self.lines.append([-40,8])
				self.lines.append([-16,24])
				self.lines.append([-16,24])
				self.lines.append([16,24])
				self.lines.append([16,24])
				self.lines.append([40,8])
				self.lines.append([16,-8])
				self.lines.append([8,-24])
				self.lines.append([8,-24])
				self.lines.append([-8,-24])
				self.lines.append([-8,-24])
				self.lines.append([-16,-8])
				self.lines.append([-16,-8])
				self.lines.append([-40,8])
				self.extremes.append(-40) 	# Min x
				self.extremes.append(-24)	# Min y
				self.extremes.append(40)	# Max x
				self.extremes.append(24)	# Max y
	
	def check_collision(self, saucerList, ship):
		pass
	
	def update(self, saucerList, ship, scene):
		self.offset[0] += self.velocity[0]
		self.offset[1] += self.velocity[1]

		if (self.offset[0] > SCREENWIDTH):	self.offset[0] = 0
		if (self.offset[0] < 0):			self.offset[0] = SCREENWIDTH
		if (self.offset[1] > SCREENHEIGHT):	self.offset[1] = 0
		if (self.offset[1] < 0):			self.offset[1] = SCREENHEIGHT
		
		if (scene == 'INGAME'):
			self.check_collision(saucerList, ship)
	
	'''def find_free_bullet_index(self):
		for _ in range(MAX_SAUCER_BULLETS):
			if (self.bullets[i] == True):
				pass'''

	'''def get_oldest_bullet(self):
		return self.bullets[0]'''

	def shoot(self, ship):
		pos = ship.offset
		x = self.offset[0] - pos[0]
		y = pos[1] - self.offset[1]
		
		if (self.size == 'SAUCER_SMALL'):
			val = atan2(y, x)
		else:
			val = (2 * PI * (randint(0,RAND_MAX))/RAND_MAX) - PI

		x = -cos(val) * SAUCER_BULLET_SPEED
		y = sin(val) * SAUCER_BULLET_SPEED
		newBullet = Bullet(self.offset, [x,y], self.theta, time())

		if (len(self.bullets) < MAX_SAUCER_BULLETS):
			self.bullets.append(newBullet)

	def free_bullet(self, i):
		_ = self.bullets.pop(i)
		del (_)

	def destroy(self, saucerList):
		# self.lines.clear()
		_ = saucerList.pop(saucerList.index(self))
		del (_)
	
def spawn_saucers(saucerList, ship):
	saucerList.clear()
	while (len(saucerList) < MAX_SAUCERS):
		if (ship.score < 10000):
			newSaucer = Saucer('SAUCER_LARGE')
		elif (ship.score >= 40000):
			newSaucer = Saucer('SAUCER_SMALL')
		else:
			match (randint(0,RAND_MAX) % 2 + 1):
				case (1):
					newSaucer = Saucer('SAUCER_SMALL')
				case (2):
					newSaucer = Saucer('Saucer_LARGE')
				case (_):
					break
		saucerList.append(newSaucer)
	return saucerList
