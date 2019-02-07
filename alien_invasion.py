import sys

import pygame

from ship import Ship
from settings import Settings

def run_game():
	#initialise game and create a screen object.
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	# screen = pygame.display.set_mode((1200,700))
	
	pygame.display.set_caption("Alien Invasion")

	# Make a ship.
	ship = Ship(screen)

	# Set the background color.
	bg_color = (230,230,230)

	#Start the main loop of the game.
	while True:

		# Watch for the keyboarrd and mouse events.
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				sys.exit()
		# Redraw the screen during wach pass through the loop.
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		# Make the recently drawn screen visible.
		pygame.display.flip()

run_game()