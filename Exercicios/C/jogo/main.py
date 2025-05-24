import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
import game_functions as gf

from pygame.sprite import Group


def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Invasão Aliens")

    stats = GameStats()
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(screen,aliens,ship)

    while True:
        gf.check_events(bullets,screen,ship)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(screen,ship,aliens,bullets)
            gf.update_aliens(stats,screen,ship,aliens,bullets)
            gf.update_screen(screen,ship,bullets,aliens)

run_game()
