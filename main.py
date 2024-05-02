import pygame
from meteor_protector import MeteorProtector
from meteor_protector import GameIntro

def main():
    pygame.init()
    game = MeteorProtector(1400, 800)
    game.main()

if __name__ == '__main__':
    main()
