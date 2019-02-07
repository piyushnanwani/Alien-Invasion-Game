import sys

import pygame

def run_game():
	#initialise game and create a screen object.
	pygame.init()
	screen = pygame.display.set_mode((1200,700))
	pygame.display.set_caption("Alien Invasion")

	#Start the main loop of the game.
	while True:

		# Watch for the keyboarrd and mouse events.
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				sys.exit()

		# Make the recently drawn screen visible.
run_game()