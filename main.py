import pygame
from constants import *
from player import Player 

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

fps = pygame.time.Clock()
dt = 0


def main():
    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    player = Player(player_x, player_y)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        screen.fill("BLACK")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
