import time

import pygame
from pygame.sprite import Group

from account import Account
from game_page import Page, ExitPage, GamePage, LoginPage
from game_settings.settings import Settings
from functions import game_functions as gf, init_buttons as ibu, init_bricks as ibr, init_text_box as it
from game_status import Status
from game_unit.PlayBack import PlayBack
from game_unit.Vector import Vector
from game_unit.brick import PlayBrick
from game_unit.text_box import InputBox


def run_game():

    # 游戏的初始化和加载设置
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.display.set_caption("elasticBall")
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    screen.fill(settings.screen_color)
    pygame.display.flip()

    # 载入音频类
    play_back = PlayBack()
    play_back.set_volume(0.3)

    # 游戏状态和账户
    status = Status(settings, screen)
    account = Account(settings)

    # 球和砖块编组
    balls = Group()
    bricks = Group()

    # 加载游戏的砖块和玩家的砖块
    ibr.get_bricks(settings, bricks, screen)
    player_brick = PlayBrick(settings, screen)

    # 显示小球发射方向的箭头
    vector = Vector(settings, screen, (0, 0))

    # 加载所有的文本框和输入框
    input_box = InputBox(settings, screen)
    login_page_text = it.init_login_page_text_box(settings, screen)
    menu_page_text = it.init_menu_page_text_box(settings, screen)
    game_page_text = it.init_game_page_text_box(settings, screen, account)
    ranking_page_text = it.init_ranking_page_text_box(settings, screen)

    # 加载所有的按钮
    menu_buttons = ibu.init_menu_buttons(settings, screen, play_back)
    back_buttons = ibu.init_back_buttons(settings, screen, play_back)
    settings_buttons = ibu.init_settings_buttons(settings, screen, play_back)
    game_page_back_buttons = ibu.init_game_page_back_buttons(settings, screen, play_back)
    login_page_buttons = ibu.init_login_buttons(settings, screen, play_back)

    # 加载所有的游戏页面
    menu_page = Page(settings, screen, menu_buttons, menu_page_text)
    ranking_page = Page(settings, screen, back_buttons, ranking_page_text)
    author_page = Page(settings, screen, back_buttons, None)
    settings_page = Page(settings, screen, settings_buttons, None)
    exit_page = ExitPage(settings, screen, None, None)
    game_page = GamePage(settings, screen, game_page_back_buttons, game_page_text, balls,
                         player_brick, bricks, vector, account, status, play_back)
    login_page = LoginPage(settings, screen, login_page_buttons, login_page_text, input_box, account)

    all_buttons = []
    all_buttons.extend(menu_buttons)
    all_buttons.extend(back_buttons)
    all_buttons.extend(settings_buttons)
    all_buttons.extend(game_page_back_buttons)
    all_buttons.extend(login_page_buttons)

    all_page = {
        'Login': menu_page,
        'Register': None,
        'Back': menu_page,
        'Start': game_page,
        'Ranking': ranking_page,
        'Settings': settings_page,
        'Author': author_page,
        'Exit': exit_page,
        'Save': None,
    }

    login_page.run()
    while True:
        time.sleep(0.1)
        for button in all_buttons:
            if button.isPushed:
                button.isPushed = False
                all_page[button.msg].run()


if __name__ == '__main__':
    run_game()
