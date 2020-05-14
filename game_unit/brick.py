import pygame
from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, settings, screen, brick_pos):
        Sprite.__init__(self)
        self.screen = screen
        self.brick_pos = brick_pos
        self.settings = settings

        self.speed = settings.brick_drop_speed

        self.rect = pygame.Rect(brick_pos[0], brick_pos[1], settings.brick_width, settings.brick_height)
        self.brick_color = settings.brick_color

        self.rect.centerx = brick_pos[0]
        self.rect.centery = brick_pos[1]

        self.isAlive = True

        self.y = float(self.rect.centery)

    def update(self):
        self.speed += self.settings.brick_increase_speed
        self.y += self.speed
        self.rect.centery = self.y

    def draw_self(self):
        self.screen.fill(self.brick_color, self.rect)


class PlayBrick(Sprite):
    def __init__(self, settings, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.settings = settings

        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, settings.player_brick_width, settings.player_brick_height)
        self.brick_color = settings.player_brick_color

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerX = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right - 200:
            self.centerX += self.settings.player_brick_speed
        if self.moving_left and self.rect.left > 0:
            self.centerX -= self.settings.player_brick_speed

        self.rect.centerx = self.centerX

    def draw_self(self):
        pygame.draw.rect(self.screen, self.brick_color, self.rect)