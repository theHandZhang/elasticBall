import pygame


class InputBox:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.text = ''
        self.font = pygame.font.SysFont(None, 48)
        self.text_image = self.font.render(self.text, True, self.settings.input_box_text_color, None)
        self.text_rect = self.text_image.get_rect()
        self.rect = pygame.Rect(0, 0, self.settings.input_box_text_width, self.text_rect.height)

        self.rect.center = self.screen.get_rect().center

        self.text_rect.centery = self.rect.centery
        self.text_rect.left = self.rect.left

        self.key_characters = {
            pygame.K_0: '0', pygame.K_1: '1', pygame.K_2: '2', pygame.K_3: '3', pygame.K_4: '4',
            pygame.K_5: '5', pygame.K_6: '6', pygame.K_7: '7', pygame.K_8: '8', pygame.K_9: '9',
            pygame.K_a: 'a', pygame.K_b: 'b', pygame.K_c: 'c', pygame.K_d: 'd', pygame.K_e: 'e',
            pygame.K_f: 'f', pygame.K_g: 'g', pygame.K_h: 'h', pygame.K_i: 'i', pygame.K_j: 'j',
            pygame.K_k: 'k', pygame.K_l: 'l', pygame.K_m: 'm', pygame.K_n: 'n', pygame.K_o: 'o',
            pygame.K_p: 'p', pygame.K_q: 'q', pygame.K_r: 'r', pygame.K_s: 's', pygame.K_t: 't',
            pygame.K_u: 'u', pygame.K_v: 'v', pygame.K_w: 'w', pygame.K_x: 'x', pygame.K_y: 'y',
            pygame.K_z: 'z',
        }

    def draw_self(self):
        self.text_image = self.font.render(self.text, True, self.settings.input_box_text_color, None)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)
        self.screen.blit(self.text_image, self.text_rect)


class TextBox:
    def __init__(self, settings, screen, str_list, font_size, box_top, text_color, centerx):
        self.settings = settings
        self.screen = screen

        self.image_list = []
        self.rect_list = []
        self.font = pygame.font.SysFont(None, font_size)
        i = 0
        for string in str_list:
            text_image = self.font.render(string, False, text_color, None)
            text_rect = text_image.get_rect()
            text_rect.centerx = centerx
            text_rect.centery = box_top + i * (text_rect.height + 10)
            self.image_list.append(text_image)
            self.rect_list.append(text_rect)
            i += 1

    def draw_self(self):

        for i in range(len(self.image_list)):
            self.screen.blit(self.image_list[i], self.rect_list[i])