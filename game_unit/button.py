import pygame

import functions.game_functions as gf
from game_unit.text_box import TextBox


class Button:
    def __init__(self, settings, screen, button_pos, msg):
        self.isPushed = False

        self.settings = settings
        self.screen = screen
        self.pos = button_pos
        self.msg = msg

        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(button_pos[0], button_pos[1], settings.button_width, settings.button_height)
        self.button_color = settings.button_color
        self.button_selected_color = settings.button_selected_color

        self.text_color = settings.button_text_color
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_selected_image = self.font.render(msg, True, self.text_color, self.button_selected_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_self(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.screen.fill(self.button_selected_color, self.rect)
            self.screen.blit(self.msg_selected_image, self.msg_image_rect)
        else:
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)

    def run_event(self):
        pass


class RegisterButton(Button):
    def __init__(self, settings, screen, button_pos, msg):
        super().__init__(settings, screen, button_pos, msg)

    def run_event(self, input_box):
        accounts = gf.read_account_file()
        account_name = input_box.text + '\n'
        if account_name in accounts:
            pygame.draw.rect(self.screen, self.settings.screen_color, pygame.Rect(446, 386, 400, 28), 0)
            TextBox(self.settings, self.screen, ['Account already exist'], 40, 400, (255, 0, 0)).draw_self()
            self.isPushed = False
            return False
        else:
            gf.write_account_file(account_name)
            self.isPushed = False
            return False


class LoginButton(Button):
    def __init__(self, settings, screen, button_pos, msg):
        super().__init__(settings, screen, button_pos, msg)

    def run_event(self, input_box):
        accounts = gf.read_account_file()
        account_name = input_box.text + '\n'
        if account_name in accounts:
            return True
        else:
            pygame.draw.rect(self.screen, self.settings.screen_color, pygame.Rect(446, 386, 400, 28), 0)
            TextBox(self.settings, self.screen, ['Account does not exist'], 40, 400, (255, 0, 0)).draw_self()
            return False

