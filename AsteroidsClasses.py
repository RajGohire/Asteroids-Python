from Constants import *

@dataclass
class asteroid_size(object):
	pass

@dataclass
class asteroid_t(object):
	def __init__(self):
		lines : Coords
		collide_lines : Coords
		nlines : int
		offset : Coords
		theta : float
		velocity : Coords
		size : asteroid_size
		extremes = [None]*4
		extremes : float	# [min x, min y, max x, max y]