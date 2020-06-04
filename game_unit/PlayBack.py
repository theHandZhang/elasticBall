import pygame


class PlayBack:
    def __init__(self):
        # 设置音频管道
        self.button_channel = pygame.mixer.Channel(0)
        self.brick_channel = pygame.mixer.Channel(1)
        self.ball_channel = pygame.mixer.Channel(2)

        self.on_button_sound = pygame.mixer.Sound('sound/on_button.wav')
        self.push_button_sound = pygame.mixer.Sound('sound/push_button.wav')
        self.brick_break_sound = pygame.mixer.Sound('sound/brick_break.wav')
        self.ball_collision = pygame.mixer.Sound('sound/ball_collision.wav')

    def set_volume(self, volume):
        self.brick_channel.set_volume(volume)
        self.button_channel.set_volume(volume)
        self.ball_channel.set_volume(volume)

    def play_brick_break(self):
        self.brick_channel.play(self.brick_break_sound)

    def play_on_button(self):
        self.button_channel.play(self.on_button_sound)

    def play_push_button(self):
        self.button_channel.play(self.push_button_sound)

    def play_ball_collision(self):
        self.ball_channel.play(self.ball_collision)