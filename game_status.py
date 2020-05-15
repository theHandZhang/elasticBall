import pygame


class Status:
    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings
        self.ball_num = settings.ball_num
        self.font = pygame.font.SysFont(None, 30)

    def draw_ball_num(self):
        ball_num_image = self.font.render(str(self.ball_num) + ' balls left', False, (255, 0, 0), None)
        ball_num_image_rect = ball_num_image.get_rect()
        ball_num_image_rect.top = 150
        ball_num_image_rect.left = 1040
        pygame.draw.rect(self.screen, self.settings.screen_color, ball_num_image_rect)
        self.screen.blit(ball_num_image, ball_num_image_rect)