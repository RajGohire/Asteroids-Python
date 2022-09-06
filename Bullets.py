from Constants import *
from copy import deepcopy

class Bullet():
	def __init__(self, offset, velocity, theta, bulletTime):
		self.offset = offset
		self.velocity = velocity
		self.bulletTime = bulletTime
		self.nlines = 5
		self.lines = [(0, 0), (-2, -3), (0, -6), (2, -3), (0, 0)]
		self.theta = theta
	
	def passbyval(func):
		def new(*args):
			cargs = [deepcopy(arg) for arg in args]
			return func(*cargs)
		return new

	@passbyval
	def update(self, deltaTime):
		self.offset[0] += self.velocity[0] * deltaTime
		self.offset[1] += self.velocity[1] * deltaTime
		
		if (self.offset[0] > SCREENWIDTH): self.offset[0] = 0
		if (self.offset[0] < 0): self.offset[0] = SCREENWIDTH
		if (self.offset[1] > SCREENHEIGHT): self.offset[1] = 0
		if (self.offset[1] < 0): self.offset[1] = SCREENHEIGHT
		
		return self.offset
