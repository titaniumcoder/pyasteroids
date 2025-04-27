import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
  def __init__(self, x, y, velocity):
    super().__init__(x, y, SHOT_RADIUS)
    self.velocity = velocity

  def draw(self, screen):
    pygame.draw.circle(screen, (255,0,0), self.position, self.radius, 2)

  def update(self, dt):
    movement = self.velocity * dt
    self.position += movement
