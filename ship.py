import pygame

class Ship():
	def __init__(self,ai_settings, screen):
		""" Initialise the ship and set its starting position. """
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.image = pygame.transform.scale(self.image,(100,100))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Start each new ship at the bottom of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
	def update(self):
		"""Update the ship's position based on the movement flag."""
		# Update the ship's center value not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += 1.5

		if self.moving_left and self.rect.left > 0:
			self.center -= 1.5

		#Update the rect object from self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

