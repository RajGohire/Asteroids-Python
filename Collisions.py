from Constants import *

def point_inside_poly(p, poly, polyOffset, nlines):
	crossings = False									# Crossings counter for checking parity
	checkVec = [2000 - p[0], 0]							# Our line beaming rightward
	
	for i in range(nlines-1):							# Check each poly pair
		dv = [poly[i+1][0] - poly[i][0], poly[i+1][1] - poly[i][1]]
		polyPos = [poly[i][0] + polyOffset[0], poly[i][1] + polyOffset[1]]
		if (lines_intersect(p, checkVec, polyPos, dv)):	# Do they cross
			crossings = not crossings					# Flip
	
	return crossings

def lines_intersect(a1, a2, b1, b2):
	denom = a2[1] * b2[0] - a2[0] * b2[1]
	if (not denom):	return False	# No collision or infinite collisions
	
	# Calculating lambda
	num = b2[1] * (a1[0] - b1[0]) - b2[0] * (a1[1] - b1[1])
	lmd = num / denom

	# Calculating new
	num = a2[1] * (b1[0] - a1[0]) - a2[0] * (b1[1] - a1[1])
	new = num / -denom

	return (lmd >= 0 and lmd <= 1 and new >= 0 and new <= 1)					# Checking if they are within the segment. Collision/No Collision

def poly_inside_poly(poly0, poly1, polyOffset0, polyOffset1, nlines0, nlines1):
	for i in range(nlines0-1):													# For every line in poly0
		dv0 = [poly0[i+1][0] - poly0[i][0], poly0[i+1][1] - poly0[i][1]]		# Calculate line equation
		polyPos0 = [poly0[i][0] + polyOffset0[0], poly0[i][1] + polyOffset0[1]]
		for j in range(nlines1-1):												# For every line in poly1
			dv1 = [poly1[j+1][0] - poly1[j][0], poly1[j+1][1] - poly1[j][1]]	# Calculate line equation
			polyPos1 = [poly1[j][0] + polyOffset1[0], poly1[j][1] + polyOffset1[1]]
			
			if (lines_intersect(polyPos0, dv0, polyPos1, dv1)): return True		# Do they cross
	return False