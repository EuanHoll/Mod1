import pygame
import sys
import sanitize
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def main():
	if len(sys.argv) != 2:
		print("Please choose a single .mod1 file")
		return
	data = san_check(sys.argv[1])
	if data is None:
		return None
	print("Finished")

def san_check(file_loc):
	if not file_loc.endswith('.mod1'):
		print("Please choose a .mod1 file")
		return None
	try:
		with open(file_loc, "r") as mod1_file:
			data = mod1_file.readlines()
	except:
		print("Please chose a valid .mod1 file")
		return None
	return sanitize.sanitize(data)

if __name__ == "__main__":
	main()