from pygame.sprite import Sprite
import pygame

class Alien(Sprite):

    """
    Uma classe que representa um único alienígena da frota.
    """
    def __init__(self, ai_settings, screen):
        """
        Inicializa o alienígena e define sua posição inicial.
        """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/alien.png')
        self.image_size = (60,60)
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """
        Desenha o alienígena em sua posição atual.
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Move o alienígena para a direita.
        """
        self.x += (self.ai_settings.alien_speed_factor*
                       self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        Devolve True se o alienígena estiver na borda da tela.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False
