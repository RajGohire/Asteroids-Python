from Pixels import draw
import pygame as pg
from Constants import *

font = {'©':[[0,15],[10,10],[20,15],[20,25],[10,30],[0,25],[0,15],[15,15],[5,15],[5,25],[15,25]],#[[15,0],[0,5],[15,0],[30,5],[0,5],[0,35],[30,5],[30,35],[30,35],[15,40],[0,35],[15,40],[5,10],[25,10],[5,30],[25,30],[5,10],[5,30]],
		'0':[[0,30],[0,0],[20,0],[20,30],[0,30],[20,0]],
		'1':[[10,0],[10,30]],
		'2':[[0,0],[20,0],[20,15],[0,15],[0,30],[20,30]],
		'3':[[0,0],[20,0],[20,15],[0,15],[20,15],[20,30],[0,30]],
		'4':[[0,0],[0,15],[20,15],[20,0],[20,30]],
		'5':[[20,0],[0,0],[0,15],[20,15],[20,30],[0,30]],
		'6':[[0,0],[0,30],[20,30],[20,15],[0,15]],
		'7':[[0,0],[20,0],[20,30]],
		'8':[[0,30],[0,0],[20,0],[20,30],[0,30],[0,15],[20,15]],
		'9':[[20,30],[20,0],[0,0],[0,15],[20,15]],
		
		'A':[[0,30],[0,10],[10,0],[20,10],[20,30],[20,20],[0,20]],
		'B':[[0,30],[0,0],[15,0],[20,5],[20,10],[15,15],[0,15],[15,15],[20,20],[20,25],[15,30],[0,30]],
		'C':[[20,0],[0,0],[0,30],[20,30]],
		'D':[[0,30],[0,0],[10,0],[20,10],[20,20],[10,30],[0,30]],
		'E':[[20,30],[0,30],[0,15],[15,15],[0,15],[0,0],[20,0]],
		'F':[[0,30],[0,15],[15,15],[0,15],[0,0],[20,0]],
		'G':[[20,10],[20,0],[0,0],[0,30],[20,30],[20,20],[10,20]],
		'H':[[0,30],[0,0],[0,15],[20,15],[20,30],[20,0]],
		'I':[[0,0],[20,0],[10,0],[10,30],[0,30],[20,30]],
		'J':[[20,0],[20,30],[15,30],[0,25]],
		'K':[[0,30],[0,0],[0,15],[20,0],[0,15],[20,30]],
		'L':[[0,0],[0,30],[20,30]],
		'M':[[0,30],[0,0],[10,10],[20,0],[20,30]],
		'N':[[0,30],[0,0],[20,30],[20,0]],
		'O':[[0,30],[0,0],[20,0],[20,30],[0,30]],
		'P':[[0,30],[0,0],[20,0],[20,15],[0,15]],
		'Q':[[0,30],[0,0],[20,0],[20,20],[10,30],[0,30],[10,30],[15,25],[10,20],[20,30]],
		'R':[[0,30],[0,0],[20,0],[20,15],[0,15],[5,15],[20,30]],
		'S':[[20,0],[0,0],[0,15],[20,15],[20,30],[0,30]],
		'T':[[0,0],[20,0],[10,0],[10,30]],
		'U':[[0,0],[0,30],[20,30],[20,0]],
		'V':[[0,0],[10,30],[20,0]],
		'W':[[0,0],[0,30],[10,10],[20,30],[20,0]],
		'X':[[0,0],[20,30],[10,15],[20,0],[0,30]],
		'Y':[[0,0],[10,10],[20,0],[10,10],[10,30]],
		'Z':[[0,0],[20,0],[0,30],[20,30]]}

'''def align(text, scale, opt):
	match (opt):
		case ('LEFT'):
			return 0
		case ('CENTER'):
			# print(scale*(len('©1979 ATARI INC')*(CHAR_WIDTH+CHAR_SPACE) - '©1979 ATARI INC'.count(' ')*CHAR_SPACE))
			return (SCREENWIDTH-scale*(len(text)*(CHAR_WIDTH+CHAR_SPACE) - text.count(' ')*CHAR_SPACE))/2
		case ('RIGHT'):
			# print(SCREENWIDTH-scale*(len(text)*(CHAR_WIDTH+CHAR_SPACE) - text.count(' ')*CHAR_SPACE))
			return (SCREENWIDTH-scale*(len(text)*(CHAR_WIDTH+CHAR_SPACE) - text.count(' ')*CHAR_SPACE))
		case (_):
			print("Align Error! -->", text, scale, opt)'''

def write(win, scale, text, off, align):
	match (align.upper()):
		case ('LEFT'):
			pass
		case ('CENTER'):
			# print(scale*(len('©1979 ATARI INC')*(CHAR_WIDTH+CHAR_SPACE) - '©1979 ATARI INC'.count(' ')*CHAR_SPACE))
			off[0] -= (scale*(len(text)*(CHAR_WIDTH+CHAR_SPACE) - text.count(' ')*CHAR_SPACE))/2
		case ('RIGHT'):
			# print(SCREENWIDTH-scale*(len(text)*(CHAR_WIDTH+CHAR_SPACE) - text.count(' ')*CHAR_SPACE))
			off[0] -= scale*(len(text)*(CHAR_WIDTH+CHAR_SPACE) - text.count(' ')*CHAR_SPACE)
		case (_):
			print("Align Error! -->", text, scale, align)
	
	for _,char in enumerate(text.upper()):
		# if _ == 0:
		# 	print(off)
		# if _ == len(text) - 1:
		# 	print([off[0]+(scale*(CHAR_WIDTH + CHAR_SPACE)),off[1]])
		if (char in font.keys()):
			out = [[off[0]+scale*x, off[1]+scale*y] for x,y in font[char]]
			off[0] += scale*(CHAR_WIDTH + CHAR_SPACE)
		elif (char == ' '):
			off[0] += scale*WORD_SPACE
		pg.draw.aalines(win, WHITE, False, out, 1)
