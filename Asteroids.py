from Constants import *
from Collisions import *

class Asteroid():
	def __init__(self, size):
		self.nlines = 20
		self.lines = []
		self.extremes = []
		self.theta = 0
		# self.offset = [randint(0,RAND_MAX) % SCREENWIDTH, randint(0,RAND_MAX) % SCREENHEIGHT]
		self.size = size
		self.collide_lines = []

		match (randint(0,RAND_MAX) % 4):
			case 0:
				# Left Wall
				self.offset = [0, randint(0, RAND_MAX) % SCREENHEIGHT]
			case 1:
				# Right Wall
				self.offset = [SCREENWIDTH, randint(0, RAND_MAX) % SCREENHEIGHT]
			case 2:
				# Top Wall
				self.offset = [randint(0, RAND_MAX) % SCREENWIDTH, 0]
			case 3:
				# Bottom Wall
				self.offset = [randint(0, RAND_MAX) % SCREENWIDTH, SCREENHEIGHT]
		
		match (size):
			case 'ASTEROID_SMALL':
				self.velocity = [(ASTEROID_SPEED*randint(0,RAND_MAX)/RAND_MAX)-ASTEROID_SPEED_SMALL,
								(ASTEROID_SPEED*randint(0,RAND_MAX)/RAND_MAX)-ASTEROID_SPEED_SMALL]
				self.lines.append([0,-4.5])
				self.lines.append([6,-10.5])
				self.lines.append([6,-10.5])
				self.lines.append([12,-4.5])
				self.lines.append([12,-4.5])
				self.lines.append([9,0])
				self.lines.append([9,0])
				self.lines.append([12,2])
				self.lines.append([12,2])
				self.lines.append([3,10.5])
				self.lines.append([3,10.5])
				self.lines.append([-6,10.5])
				self.lines.append([-6,10.5])
				self.lines.append([-12,2])
				self.lines.append([-12,2])
				self.lines.append([-12,-4.5])
				self.lines.append([-12,-4.5])
				self.lines.append([-6,-10.5])
				self.lines.append([-6,-10.5])
				self.lines.append([0,-4.5])
				self.extremes.append(-12) 	# Min x
				self.extremes.append(-10.5)	# Min y
				self.extremes.append(12)	# Max x
				self.extremes.append(10.5)	# Max y
			case 'ASTEROID_MEDIUM':
				self.velocity = [(ASTEROID_SPEED*randint(0,RAND_MAX)/RAND_MAX)-ASTEROID_SPEED_MEDIUM,
								(ASTEROID_SPEED*randint(0,RAND_MAX)/RAND_MAX)-ASTEROID_SPEED_MEDIUM]
				self.lines.append([0,-7.5])
				self.lines.append([10,-17.5])
				self.lines.append([10,-17.5])
				self.lines.append([20,-7.5])
				self.lines.append([20,-7.5])
				self.lines.append([15,0])
				self.lines.append([15,0])
				self.lines.append([20,10])
				self.lines.append([20,10])
				self.lines.append([5,17.5])
				self.lines.append([5,17.5])
				self.lines.append([-10,17.5])
				self.lines.append([-10,17.5])
				self.lines.append([-20,10])
				self.lines.append([-20,10])
				self.lines.append([-20,-7.5])
				self.lines.append([-20,-7.5])
				self.lines.append([-10,-17])
				self.lines.append([-10,-17])
				self.lines.append([0,-7.5])
				self.extremes.append(-20) 	# Min x
				self.extremes.append(-17.5)	# Min y
				self.extremes.append(20)	# Max x
				self.extremes.append(17.5)	# Max y
			case 'ASTEROID_LARGE':
				self.velocity = [(ASTEROID_SPEED*randint(0,RAND_MAX)/RAND_MAX)-ASTEROID_SPEED_LARGE,
								(ASTEROID_SPEED*randint(0,RAND_MAX)/RAND_MAX)-ASTEROID_SPEED_LARGE]
				self.lines.append([0,-15])
				self.lines.append([20,-35])
				self.lines.append([20,-35])
				self.lines.append([40,-15])
				self.lines.append([40,-15])
				self.lines.append([30,0])
				self.lines.append([30,0])
				self.lines.append([40,20])
				self.lines.append([40,20])
				self.lines.append([10,35])
				self.lines.append([10,35])
				self.lines.append([-20,35])
				self.lines.append([-20,35])
				self.lines.append([-40,20])
				self.lines.append([-40,20])
				self.lines.append([-40,-15])
				self.lines.append([-40,-15])
				self.lines.append([-20,-35])
				self.lines.append([-20,-35])
				self.lines.append([0,-15])
				self.extremes.append(-40) 	# Min x
				self.extremes.append(-35)	# Min y
				self.extremes.append(40)	# Max x
				self.extremes.append(35)	# Max y

	def check_ship_collision(self, asteroidList, ship):
		# Collision between ship and asteroid
		if (poly_inside_poly(ship.lines, self.lines, ship.offset, self.offset, ship.nlines, self.nlines)):
			match (self.size):
				case ('ASTEROID_LARGE'):
					ship.score += 20
				case ('ASTEROID_MEDIUM'):
					ship.score += 50
				case ('ASTEROID_SMALL'):
					ship.score += 100
			ship.destroy()
			self.destroy(asteroidList)
		else:	# Collision between ship bullets and asteroid
			for i, bullet in enumerate(ship.bullets):
				if (point_inside_poly(bullet.offset, self.lines, self.offset, self.nlines)):
					match (self.size):
						case ('ASTEROID_LARGE'):
							ship.score += 20
						case ('ASTEROID_MEDIUM'):
							ship.score += 50
						case ('ASTEROID_SMALL'):
							ship.score += 100
					self.split(asteroidList)
					ship.free_bullet(i)

	def check_saucer_collision(self, asteroidList, saucer, saucerList):
		# Collision between saucer and asteroid
		if (poly_inside_poly(saucer.lines, self.lines, saucer.offset, self.offset, saucer.nlines, self.nlines)):
			saucer.destroy(saucerList)
			self.destroy(asteroidList)
		else:	# Collision between saucer bullets and asteroid
			for i, bullet in enumerate(saucer.bullets):
				if (point_inside_poly(bullet.offset, self.lines, self.offset, self.nlines)):
					self.split(asteroidList)
					saucer.free_bullet(i)

	def update(self, asteroidList, ship, saucerList, scene):
		# self.theta += 0.01
		self.offset[0] += self.velocity[0]
		self.offset[1] += self.velocity[1]

		if (self.offset[0] > SCREENWIDTH):	self.offset[0] = 0
		if (self.offset[0] < 0):			self.offset[0] = SCREENWIDTH
		if (self.offset[1] > SCREENHEIGHT):	self.offset[1] = 0
		if (self.offset[1] < 0):			self.offset[1] = SCREENHEIGHT

		if (scene == 'INGAME'):
			self.check_ship_collision(asteroidList, ship)
			for saucer in saucerList:
				self.check_saucer_collision(asteroidList, saucer, saucerList)

	def split(self, asteroidList):
		match (self.size):
			case ('ASTEROID_LARGE'):
				if (len(asteroidList) != MAX_ASTEROIDS):
					newAsteroid = Asteroid('ASTEROID_MEDIUM')
					newAsteroid.offset = [self.offset[0], self.offset[1]]
					asteroidList.append(newAsteroid)
				tempOffset = self.offset
				idx = asteroidList.index(self)
				self.lines.clear()
				self.__dict__.update(Asteroid('ASTEROID_MEDIUM').__dict__)
				self.offset = tempOffset
				asteroidList[idx] = self
			case ('ASTEROID_MEDIUM'):
				if (len(asteroidList) != MAX_ASTEROIDS):
					newAsteroid = Asteroid('ASTEROID_SMALL')
					newAsteroid.offset = [self.offset[0], self.offset[1]]
					asteroidList.append(newAsteroid)
				tempOffset = self.offset
				idx = asteroidList.index(self)
				self.lines.clear()
				self.__dict__.update(Asteroid('ASTEROID_SMALL').__dict__)
				self.offset = tempOffset
				asteroidList[idx] = self
			case (_):
				self.destroy(asteroidList)

	def destroy(self, asteroidList):
		# self.lines.clear()
		_ = asteroidList.pop(asteroidList.index(self))
		del (_)

def spawn_asteroids(asteroidList, level):
	asteroidList.clear()
	while (len(asteroidList) < 2 + (level*2)):	# (level*2) is the rate at which number of asteroids increase per level
		newAsteroid = Asteroid('ASTEROID_LARGE')
		asteroidList.append(newAsteroid)
	return asteroidList