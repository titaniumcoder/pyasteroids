import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, drawable, updatable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroidfield = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    for thing in updatable:
      thing.update(dt)

    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collision(shot):
          shot.kill()
          asteroid.split()

    for asteroid in asteroids:
      if asteroid.collision(player):
        print("Game over!")
        exit(1)

    screen.fill((0, 0, 0))

    for thing in drawable:
      thing.draw(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
