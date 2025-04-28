import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (51,255,255), self.position, self.radius, 2)

  def update(self, dt):
    movement = self.velocity * dt
    self.position += movement

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(20, 50)
    velocity1 = self.velocity.rotate(angle)
    velocity2 = self.velocity.rotate(-angle)
    small_radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid1 = Asteroid(self.position.x, self.position.y, small_radius)
    asteroid1.velocity = velocity1 * 1.2
    asteroid2 = Asteroid(self.position.x, self.position.y, small_radius)
    asteroid2.velocity = velocity2 * 1.2
