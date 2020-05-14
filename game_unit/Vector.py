import math

import pygame


class Vector:
    def __init__(self, settings, screen, pos):
        self.settings = settings
        self.pos = pos
        self.screen = screen

        self.angle = math.pi / 2
        self.size = self.settings.vector_size
        self.end_pos = (0, 0)
        self.wing_size = settings.vector_wing_size
        self.moving_right = False
        self.moving_left = False

    def update(self, player_brick):
        self.pos = (player_brick.rect.centerx, player_brick.rect.top)
        if self.moving_left and self.angle < math.pi:
            self.angle += 0.005
        if self.moving_right and self.angle > 0:
            self.angle -= 0.005

    def draw_self(self):
        self.end_pos = (float(self.pos[0] + self.size * math.cos(self.angle)),
                        float(self.pos[1] - self.size * math.sin(self.angle)))
        right_wing_start_pos = (float(self.end_pos[0] - self.wing_size * math.cos(self.angle + math.pi / 4)),
                                float(self.end_pos[1] + self.wing_size * math.sin(self.angle + math.pi / 4)))
        left_wing_start_pos = (float(self.end_pos[0] - self.wing_size * math.cos(self.angle - math.pi / 4)),
                               float(self.end_pos[1] + self.wing_size * math.sin(self.angle - math.pi / 4)))
        pygame.draw.line(self.screen, (0, 0, 0), self.pos, self.end_pos, 2)
        pygame.draw.line(self.screen, (0, 0, 0), right_wing_start_pos, self.end_pos, 2)
        pygame.draw.line(self.screen, (0, 0, 0), left_wing_start_pos, self.end_pos, 2)
