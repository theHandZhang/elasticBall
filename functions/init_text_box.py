import socket

from game_unit.text_box import TextBox


def init_login_page_text_box(settings, screen):
    text_box = TextBox(settings, screen, ['Welcome to the elastic ball game', 'Please log in to the game'],
                       30, 300, (0, 0, 0), screen.get_rect().centerx)
    return text_box


def init_menu_page_text_box(settings, screen):
    text_box = TextBox(settings, screen, ['ELASTIC BALL'], 120, 200, (0, 0, 0), screen.get_rect().centerx)
    return text_box


def init_game_page_text_box(settings, screen, account):
    text_box = TextBox(settings, screen, ['Press W & D to control ',
                                          'the direction of ball',
                                          'Press left arrow and ',
                                          'right arrow to control ',
                                          'the movement of your ',
                                          'brick'],
                       25, 800, (0, 0, 0), 1100)
    return text_box


def init_ranking_page_text_box(settings, screen):
    msg = 'RANK@'
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("cn-zj-bgp-2.sakurafrp.com", 23413))
    client.send(msg.encode())
    data_info = client.recv(1024).decode().replace('#', '     ')
    datas = data_info.split('@')

    text_box = TextBox(settings, screen, datas, 30, 100, (0, 0, 0), screen.get_rect().centerx)
    client.close()
    return text_box

