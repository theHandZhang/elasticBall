import random
import sys

import pygame
from game_unit.ball import Ball
import socket

from game_unit.text_box import TextBox


def check_button_events(mouse_pos, buttons):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.isPushed = True
                    button.run_event(None)
                    button.play_pushed_sound()
                    return True


def check_login_events(mouse_pos, buttons, input_box):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.isPushed = True
                    button.play_pushed_sound()
                    if button.run_event(input_box):
                        return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_box.text = input_box.text[0:len(input_box.text) - 1]
            if event.key in input_box.key_characters:
                input_box.text += input_box.key_characters[event.key]


def check_game_events(settings, screen, mouse_pos, buttons, balls, player_brick, vector, status, play_back):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.isPushed = True
                    button.run_event(None)
                    button.play_pushed_sound()
                    return True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if status.ball_num > 0:
                    status.ball_num -= 1
                    # 生成一个随机数 用于产生不同的球的颜色
                    ball_color_type = int(random.random() * 2 + 1)
                    balls.add(Ball(settings, screen, ball_color_type, vector.angle, player_brick, play_back))

            elif event.key == pygame.K_RIGHT:
                player_brick.moving_right = True
            elif event.key == pygame.K_LEFT:
                player_brick.moving_left = True
            elif event.key == pygame.K_d:
                vector.moving_right = True
            elif event.key == pygame.K_a:
                vector.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player_brick.moving_right = False
            elif event.key == pygame.K_LEFT:
                player_brick.moving_left = False
            elif event.key == pygame.K_d:
                vector.moving_right = False
            elif event.key == pygame.K_a:
                vector.moving_left = False


def write_account_file(account_name):
    account_file = open('account_information/account.txt', 'a')
    account_file.write(account_name)
    account_file.close()


def read_account_file():
    account_file = open('account_information/account.txt', 'r')
    accounts = account_file.readlines()
    account_file.close()
    return accounts


def get_ranking_info(settings, screen):
    msg = 'RANK@'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("cn-zj-bgp-2.sakurafrp.com", 23413))

    client.send(msg.encode())
    data_info = client.recv(1024).decode().replace('#', '       ')
    datas = data_info.split('@')
    text = ['name               time             score']
    text.extend(datas)
    text_box = TextBox(settings, screen, text, 30, 100, (127, 255, 212), screen.get_rect().centerx)
    client.close()
    print("socket close")

    return text_box

