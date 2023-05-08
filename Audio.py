from Constants import *
import os
import pygame as pg

class Soundtrack():
	def __init__(self):
		self.elapsedTime = 0
		self.targetDelay = SOUNDTRACK_MAX_DELAY
		self.playing = True
		# self.beats = [None]*2
		self.beat = 0
		self.time = 0
		self.soundSamples = []
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/beat1.wav"))
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/beat2.wav"))
		
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/bangSmall.wav"))
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/bangMedium.wav"))
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/bangLarge.wav"))

		self.soundSamples.append(pg.mixer.Sound("./soundfiles/fire.wav"))
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/thrust.wav"))

		self.soundSamples.append(pg.mixer.Sound("./soundfiles/extraShip.wav"))
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/saucerSmall.wav"))
		self.soundSamples.append(pg.mixer.Sound("./soundfiles/saucerBig.wav"))
		
		'''self.soundSamples = {}
		with os.scandir("./soundfiles/") as files:
			samples = [x.name for x in files if x.name.endswith('.wav')]
			for i, file in enumerate(samples):
				print(i,file)
				self.soundSamples[file[:-4]] = (i,pg.mixer.Sound(os.path.join("./soundfiles/",file)))
				# pg.mixer.Channel(i).play(pg.mixer.Sound(os.path.join("./soundfiles/",file)))
		print(self.soundSamples)'''

	def load_sample():
		pass

	def soundtrack_init():
		pass

	def play(self, delta):
		if (not self.playing):
			self.elapsedTime += delta
			self.time += delta
			
			if (self.elapsedTime >= self.targetDelay):
				pg.mixer.Channel(0).play(self.soundSamples[self.beat])
				self.beat = (self.beat + 1) % 2
				self.elapsedTime = 0
				self.targetDelay = SOUNDTRACK_GRADIENT * self.time + SOUNDTRACK_MAX_DELAY
				
				if (self.targetDelay < SOUNDTRACK_MIN_DELAY):
					self.targetDelay = SOUNDTRACK_MIN_DELAY

	def audio_cleanup():
		pass