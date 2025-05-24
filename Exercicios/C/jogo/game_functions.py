import pygame
import sys
from time import sleep
from bullet import Bullet
from alien import Alien

def check_events(bullets,screen,ship):

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.moving_left = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen,ship)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.moving_left = False

def update_screen(screen,ship,bullets,aliens):
    bg_color = (230,230,230)
    screen.fill(bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    aliens.draw(screen)
    pygame.display.flip()


def create_fleet(screen,aliens, ship):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    available_space_x = screen.get_rect().width - alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    ship_height = ship.rect.height
    available_space_y = screen.get_rect().height - 3*alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien = Alien(screen)
            alien.x = alien_width + 2*alien_width*alien_number
            alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
            alien.rect.x = alien.x
            aliens.add(alien)


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break

def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.fleet_drop_speed
        alien.fleet_direction *=-1
    
def update_aliens(stats,screen,ship,aliens,bullets):
    check_fleet_edges(aliens)
    aliens.update()
    check_aliens_bottom(stats,screen,ship,aliens,bullets)
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,screen,ship,aliens,bullets)


def update_bullets(screen,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if len(aliens)==0:
        bullets.empty()
        create_fleet(screen,aliens, ship)
        
            
def ship_hit(stats,screen,ship,aliens,bullets):
    if stats.ships_left >0:
        stats.ships_left -=1
        aliens.empty()
        bullets.empty()
        create_fleet(screen,aliens,ship)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active=False

def check_aliens_bottom(stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,screen,ship,aliens,bullets)
            break
        
        
