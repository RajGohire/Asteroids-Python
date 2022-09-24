from Constants import *
from Ship import *
from Asteroids import *
from Saucers import *
from time import time, perf_counter, sleep
from Pixels import *
from Bullets import *

def main():
	# Variables
	closed = False
	highScore = 0
	with open('highscore.txt','r') as fileHigh:
		highScore = fileHigh.readline()
		print(highScore)
	asteroidTime = saucerTime = None
	scene = 'INGAME'
	currentScore = 0
	asteroid_timeUpdateCounter = saucer_timeUpdateCounter = 0
	level = 1
	thrusting = False

	currentTime = perf_counter()
	prevTime = 0
	delta = 0
	clock = pg.time.Clock()

	# Initialize the pygame
	pg.init()

	ship = Ship()
	asteroidList = spawn_asteroids([], level)
	saucerList = spawn_saucers([], ship)
	'''pg.draw.aalines(surf, WHITE, True, [[0,50], [50,80], [80,90], [90,150]], 0)
	pg.draw.aalines(surf, WHITE, False, ship.lines, 0)'''

	# Load fonts

	# Create the window
	win = pg.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
	pg.display.set_caption("Asteroids")
	# surf = pg.display.get_surface()
	# print(surf.get_width(), surf.get_height(), surf.get_pitch())
	# pg.display.set_icon(pg.image.load())
	
	# Game Loop
	while (not closed):
		# Limits the while loop to a max of 10 times per second.
		delta = clock.tick(60)
		# print(delta)

		for event in pg.event.get():
			match (event.type):
				case (pg.QUIT):
					closed = True
					break
				case (pg.KEYDOWN):
					match (scene):
						case ("MAINMENU"):
							if (event.key == pg.K_SPACE):
								asteroidList.clear()
								level = 1
								spawn_asteroids(asteroidList, level)
								scene = 'INGAME'
						case ("INGAME"):
							match (event.key):
								case (pg.K_RCTRL):  ship.hyperdrive()
								case (pg.K_SPACE):	ship.shoot()
								case (pg.K_p):      scene = 'MAINMENU'
								case (pg.K_ESCAPE):
									scene = 'MAINMENU'
									del(ship)
									ship = Ship()
									level = 1
									spawn_asteroids(asteroidList, level)
						case ("GAMEOVER"):
							if (event.key == pg.K_ESCAPE):
								scene = 'MAINMENU'
								del(ship)
								ship = Ship()
								# Print Score
								level = 1
								spawn_asteroids(asteroidList, level)

					break

		keystate = pg.key.get_pressed()

		if (scene == 'INGAME'):
				if (keystate[pg.K_LEFT]):
					ship.rotate(delta, SHIP_DIR_LEFT)
				if (keystate[pg.K_RIGHT]):
					ship.rotate(delta, SHIP_DIR_RIGHT)
				if (keystate[pg.K_UP]):
					ship.move(delta)
					thrusting = True
				else:
					# ship.lines[11] = ship.lines[13] = [0,4]
					thrusting = False
				'''if (keystate[pg.K_ESCAPE]):
					scene = 'MAINMENU'
					del(ship)
					ship = Ship()
					level = 1
					# Spawn asteroids'''
				
				ship.update()
		
		for asteroid in asteroidList:
			asteroid.update(asteroidList, ship, saucerList, scene)

		for saucer in saucerList:
			saucer.update(saucerList, ship, scene)
			for bullet in saucer.bullets:
				bullet.offset = bullet.update(delta)
				draw(win, bullet)
				if (time() - saucer.bullets[0].bulletTime >= BULLET_TIMEOUT):
					saucer.free_bullet(0)

		win.fill(BLACK)
		# surf.fill(BLACK)

		for asteroid in asteroidList:
			draw(win, asteroid)

		for saucer in saucerList:
			draw(win, saucer)

		match (scene):
			case ('MAINMENU'):
				# write_ascii(surf, font_large, "ASTEROIDS", (vec2f_t){(float)SCREENWIDTH/2, (float)SCREENHEIGHT/3}, ALIGN_CENTER);
				# write_ascii(surf, font_large, "RELOADED", (vec2f_t){(float)SCREENWIDTH/2, (float)SCREENHEIGHT/2-20}, ALIGN_CENTER);
				# write_ascii(surf, font_small, ("\0011979 ATARI INC"), (vec2f_t){(float)SCREENWIDTH/2, (float)SCREENHEIGHT-30}, ALIGN_CENTER);
				pass
			case ('INGAME'):
				draw(win, ship)
				if (ship.lives <= 0):
					scene = 'GAMEOVER'
					# break
				
				if (currentScore != ship.score):
					if (ship.score >= 99990):
						ship.score = 0
					elif ((currentScore//10000) + 1 == ship.score//10000):
						ship.lives += 1
					currentScore = ship.score
					print("Score:", currentScore)
					'''You can change the format string to:
						- "%05d", to make it pad the string up to 5 characters with '0's
						- "%5d", to right-align the number'''
					# sprintf(score_buf, "%d", ship.score);
				
				# write_ascii(surf, font_small, score_buf, (vec2f_t){10,10}, ALIGN_LEFT);
				# write_ascii(surf, font_small, score_high, (vec2f_t){SCREENWIDTH/2,10}, ALIGN_CENTER);
				# Draw Ship Lives Icons

				for bullet in ship.bullets:
					bullet.offset = bullet.update(delta)
					draw(win, bullet)
					if (time() - ship.bullets[0].bulletTime >= BULLET_TIMEOUT):
						ship.free_bullet(0)

				if (not asteroidList):
					if (not asteroid_timeUpdateCounter):
						asteroidTime = time()
						asteroid_timeUpdateCounter = 1
					elif (time() - asteroidTime >= SPAWN_TIME_GAP):
						level += 1
						spawn_asteroids(asteroidList, level)
						asteroid_timeUpdateCounter = 0
				
				if (not saucerList):
					if (not saucer_timeUpdateCounter):
						saucer_tempTime = time()
						saucer_timeUpdateCounter = 1
					elif (time() - saucer_tempTime >= SAUCER_SPAWN_TIME_GAP):
						spawn_saucers(saucerList,  ship)
						saucer_timeUpdateCounter = 0

			case ('GAMEOVER'):
				# sprintf(score_buf, "%d", ship.score);
				# write_ascii(surf, font_large, "GAME OVER", (vec2f_t){(float)SCREENWIDTH/2, (float)SCREENHEIGHT/2-100}, ALIGN_CENTER);
				# write_ascii(surf, font_normal, score_buf, (vec2f_t){(float)SCREENWIDTH/2, (float)SCREENHEIGHT/2+70}, ALIGN_CENTER);
				if (ship.score == highScore):
					# write_ascii(surf, font_normal, "NEW HIGHSCORE", (vec2f_t){(float)SCREENWIDTH/2, (float)SCREENHEIGHT/2+170}, ALIGN_CENTER);
					pass
				if (ship.score > highScore):
					with open('highscore.txt', 'w') as fileHigh:
						fileHigh.write(str(currentScore))
					highScore = currentScore
		
		# draw(win, ship)
		
		pg.display.flip()
		# pg.display.update()
	
	pg.display.quit()
	
	# Free ship
	# Free asteroid list
	# Free asteroidList var
	# Free saucer list
	# Free font

if __name__ == '__main__':
	main()
