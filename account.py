from datetime import datetime

import pygame
import socket


class Account:
    def __init__(self, settings):
        self.settings = settings
        self.account_name = 'null'
        self.score = 0
        self.play_time = 0
        self.current_time = None
        self.font = pygame.font.SysFont(None, 30)

    def draw_score(self, screen):
        score_image = self.font.render('score : ' + str(self.score), False, (255, 0, 0), None)
        score_image_rect = score_image.get_rect()
        score_image_rect.top = 100
        score_image_rect.left = 1040
        pygame.draw.rect(screen, self.settings.screen_color, score_image_rect)
        screen.blit(score_image, score_image_rect)

    def set_name(self, account_name):
        if account_name == 'account':
            raise Exception("account name can not be 'account'!", account_name)
        self.account_name = account_name

    def time_start(self):
        self.current_time = datetime.now()
        print(self.current_time)

    def time_end(self):
        self.play_time = datetime.now() - self.current_time
        print(self.play_time)

    def store_info(self):
        file_path = 'account_information/' + self.account_name + '.txt'
        file = open(file_path, 'a')
        file.write(str(self.play_time) + '##' + str(self.score) + '\n')
        file.close()
        self.store_info_remote()

    def store_info_remote(self):
        msg = 'SAVE@' + self.account_name + '#' + str(self.play_time) + '#' + str(self.score)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("cn-zj-bgp-2.sakurafrp.com", 23413))
        client.send(msg.encode())
        print("send info OK")

        client.close()
        print("socket close")

