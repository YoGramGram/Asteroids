import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)

	def draw(self, screen: pygame.Surface) -> None:
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

	def update(self, dt: float) -> None:
		self.position += self.velocity * dt

	def split(self) -> None:
		self.kill()
		if self.radius == ASTEROID_MIN_RADIUS:
			log_event("asteroid_killed")
			return
		else:
			log_event("asteroid_split")
			launch_angle = random.uniform(20, 50)
			spawn_1_angle = self.velocity.rotate(launch_angle)
			spawn_2_angle = self.velocity.rotate(-launch_angle)
			spawn_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid_spawn_1 = Asteroid(self.position.x, self.position.y, spawn_radius)
			asteroid_spawn_1.velocity = spawn_1_angle * 1.2
			asteroid_spawn_2 = Asteroid(self.position.x, self.position.y, spawn_radius)
			asteroid_spawn_2.velocity = spawn_2_angle * 1.2
			self.kill()
