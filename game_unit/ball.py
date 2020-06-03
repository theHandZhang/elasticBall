import math
import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    def __init__(self, settings, screen, color_type, moving_angle, player_brick, play_back):
        Sprite.__init__(self)
        self.settings = settings
        self.screen = screen
        self.color_type = color_type
        self.moving_angle = moving_angle
        self.player_brick = player_brick
        self.play_back = play_back

        self.rect = pygame.Rect(0, 0, 16, 16)
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.player_brick.rect.centerx
        self.rect.centery = self.screen_rect.height - 32

        self.x = float(self.player_brick.rect.centerx)
        self.y = float(self.screen_rect.height - 32)

        self.speed = self.settings.ball_moving_speed
        self.decrease_speed = self.settings.ball_decrease_speed

        self.isMoving = False

    def update(self, bricks, player_brick):

        self.x += self.speed * math.cos(self.moving_angle)
        self.y -= self.speed * math.sin(self.moving_angle)

        # 碰到屏幕右边
        if abs(self.x + self.rect.width / 2 - self.screen_rect.width + 200) < 1.0 and (
                0 < self.y < self.screen_rect.height):
            self.moving_angle = math.pi - self.moving_angle
            self.play_back.play_ball_collision()
            print("yesR")

        # 碰到屏幕左边
        if abs(self.x - self.rect.width / 2) < 1.0 and (
                0 < self.y < self.screen_rect.height):
            self.moving_angle = math.pi - self.moving_angle
            self.play_back.play_ball_collision()
            print("yesL")

        # 碰到屏幕上边
        if abs(self.y - self.rect.height / 2) < 1.0 and (0 < self.x < self.screen_rect.width - 200):
            self.moving_angle = math.pi * 2 - self.moving_angle
            self.play_back.play_ball_collision()
            print("yesT")

        # 碰到玩家的砖块
        if (player_brick.rect.left - self.rect.width / 2 < self.x < player_brick.rect.right +
                self.rect.width / 2) and abs(self.y - player_brick.rect.top + self.rect.height / 2) < 1:
            self.moving_angle = math.pi * 2 - self.moving_angle
            self.speed = self.settings.ball_moving_speed
            self.play_back.play_ball_collision()
            print("player")

        for brick in bricks:
            # 砖块左边
            if abs(self.x + self.rect.width / 2 - brick.rect.left) < 1.0 and (
                    brick.rect.top - self.rect.height / 2 < self.y < brick.rect.bottom + self.rect.height / 2):
                self.moving_angle = math.pi - self.moving_angle
                brick.isAlive = False
                self.play_back.play_brick_break()
                print("OK Left")
            # 砖块右边
            if abs(self.x - self.rect.width / 2 - brick.rect.right) < 1.0 and (
                    brick.rect.top - self.rect.height / 2 < self.y < brick.rect.bottom + self.rect.height / 2):
                self.moving_angle = math.pi - self.moving_angle
                brick.isAlive = False
                self.play_back.play_brick_break()
                print("OK Right")
            # 砖块上边
            if brick.rect.left - self.rect.width / 2 < self.x < brick.rect.right + self.rect.width / 2 and (
                    abs(self.y + self.rect.height / 2 - brick.rect.top) < 1.0):
                self.moving_angle = math.pi * 2 - self.moving_angle
                brick.isAlive = False
                self.play_back.play_brick_break()
                print("OK Top")
            # 砖块下边
            if brick.rect.left - self.rect.width / 2 < self.x < brick.rect.right + self.rect.width / 2 and (
                    abs(self.y - self.rect.height / 2 - brick.rect.bottom) < 1.0):
                self.moving_angle = math.pi * 2 - self.moving_angle
                brick.isAlive = False
                self.play_back.play_brick_break()
                print("OK Bottom")

        if self.speed >= 0:
            self.speed -= self.decrease_speed
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def draw_self(self):
        if self.color_type == 1:
            pygame.draw.circle(self.screen, (255, 0, 0), self.rect.center, 8)
        if self.color_type == 2:
            pygame.draw.circle(self.screen, (0, 0, 255), self.rect.center, 8)
