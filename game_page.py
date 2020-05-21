import sys
import time

import pygame

from functions import game_functions as gf


class Page:
    def __init__(self, settings, screen, buttons, content):
        self.settings = settings
        self.screen = screen
        self.buttons = buttons
        self.content = content

    def run(self):
        self.screen.fill(self.settings.screen_color)
        while True:
            time.sleep(0.01)
            self.content.draw_self()
            mouse_pos = pygame.mouse.get_pos()
            if gf.check_button_events(mouse_pos, self.buttons):
                print('Pushed')
                return
            for button in self.buttons:
                button.draw_self(mouse_pos)
                pygame.display.flip()


class LoginPage(Page):
    def __init__(self, settings, screen, buttons, content, input_box, account):
        super().__init__(settings, screen, buttons, content)
        self.input_box = input_box
        self.account = account

    def run(self):
        self.screen.fill(self.settings.screen_color)
        while True:
            time.sleep(0.01)
            self.content.draw_self()
            pygame.draw.rect(self.screen, self.settings.screen_color, self.input_box.rect, 0)
            mouse_pos = pygame.mouse.get_pos()
            self.input_box.draw_self()
            if gf.check_login_events(mouse_pos, self.buttons, self.input_box):
                self.account.set_name(self.input_box.text)
                print('Pushed')
                return
            for button in self.buttons:
                button.draw_self(mouse_pos)
                pygame.display.flip()


class ExitPage(Page):
    def __init__(self, settings, screen, buttons, content):
        super().__init__(settings, screen, buttons, content)

    def run(self):
        sys.exit()


class GamePage(Page):
    def __init__(self, settings, screen, buttons, content, balls, player_brick, bricks, vector, account, status):
        super().__init__(settings, screen, buttons, content)
        self.balls = balls
        self.player_brick = player_brick
        self.bricks = bricks
        self.vector = vector
        self.account = account
        self.status = status
        self.game_rect = pygame.Rect(0, 0, self.screen.get_rect().width - 200, self.screen.get_rect().height)

    def run(self):
        self.account.time_start()
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen.get_rect().width - 199, 0),
                         (self.screen.get_rect().width - 200, self.screen.get_rect().height), 1)

        while True:
            pygame.draw.rect(self.screen, self.settings.screen_color, self.game_rect)

            mouse_pos = pygame.mouse.get_pos()

            self.content.draw_self()
            self.account.draw_score(self.screen)

            self.status.draw_ball_num()

            self.player_brick.draw_self()
            self.player_brick.update()

            self.vector.update(self.player_brick)
            self.vector.draw_self()

            for brick in self.bricks:
                brick.draw_self()
                brick.update()
                if brick.isAlive is False:
                    self.account.score += 1
                    self.bricks.remove(brick)

            for ball in self.balls:
                ball.draw_self()
                ball.update(self.bricks, self.player_brick)
                if ball.rect.top > self.screen.get_rect().bottom:
                    print("a ball dead")
                    self.balls.remove(ball)

            for button in self.buttons:
                button.draw_self(mouse_pos)
                pygame.display.flip()

            if gf.check_game_events(self.settings, self.screen, mouse_pos, self.buttons,
                                    self.balls, self.player_brick, self.vector, self.status):
                self.account.time_end()
                self.account.store_info()
                self.bricks.empty()
                self.balls.empty()
                print('Pushed')
                return
