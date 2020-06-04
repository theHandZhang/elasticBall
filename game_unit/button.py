import pygame

import functions.game_functions as gf
from game_unit.text_box import TextBox


class Button:
    def __init__(self, settings, screen, button_pos, msg, play_back):  # buttons_pos 分别是对应的left 和top
        self.isPushed = False
        self.mouse_on = False

        self.settings = settings
        self.screen = screen
        self.pos = button_pos
        self.msg = msg
        self.play_back = play_back

        self.font = pygame.font.SysFont(None, 36)
        self.image = pygame.image.load('texture/button.png')
        self.rect = self.image.get_rect()
        self.rect.left = button_pos[0]
        self.rect.top = button_pos[1]

        self.msg_image = self.font.render(msg, True, self.settings.button_text_color)
        self.msg_selected_image = self.font.render(msg, True, self.settings.button_text_selected_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_self(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.mouse_on is False:
                self.play_back.play_on_button()
            self.mouse_on = True
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.msg_selected_image, self.msg_image_rect)
        else:
            self.mouse_on = False
            self.screen.blit(self.image, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)

    def play_pushed_sound(self):
        self.play_back.play_push_button()

    def run_event(self, input_box):
        pass


class RegisterButton(Button):
    def __init__(self, settings, screen, button_pos, msg, play_back):
        super().__init__(settings, screen, button_pos, msg, play_back)

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
    def __init__(self, settings, screen, button_pos, msg, play_back):
        super().__init__(settings, screen, button_pos, msg, play_back)

    def run_event(self, input_box):
        accounts = gf.read_account_file()
        account_name = input_box.text + '\n'
        if account_name in accounts:
            return True
        else:
            pygame.draw.rect(self.screen, self.settings.screen_color, pygame.Rect(446, 386, 400, 28), 0)
            TextBox(self.settings, self.screen, ['Account does not exist'], 40, 400, (255, 0, 0),
                    self.screen.get_rect().centerx).draw_self()
            return False

