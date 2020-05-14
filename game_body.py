import time

import pygame
from pygame.sprite import Group
from game_page import Page, ExitPage, GamePage, LoginPage
from game_settings.settings import Settings
from functions import game_functions as gf, init_buttons as ib, init_bricks as ii, init_text_box as it
from game_unit.Vector import Vector
from game_unit.brick import PlayBrick
from game_unit.text_box import InputBox


def run_game():
    pygame.init()
    pygame.display.set_caption("elasticBall")
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    screen.fill(settings.screen_color)
    pygame.display.flip()

    balls = Group()
    bricks = Group()

    ii.get_bricks(settings, bricks, screen)
    player_brick = PlayBrick(settings, screen)

    vector = Vector(settings, screen, (0, 0))

    input_box = InputBox(settings, screen)
    login_page_text = it.init_login_page_text_box(settings, screen)
    menu_page_text = it.init_menu_page_text_box(settings, screen)

    menu_buttons = ib.init_menu_buttons(settings, screen)
    back_buttons = ib.init_back_buttons(settings, screen)
    settings_buttons = ib.init_settings_buttons(settings, screen)
    game_page_back_buttons = ib.init_game_page_back_buttons(settings, screen)
    login_page_buttons = ib.init_login_buttons(settings, screen)

    menu_page = Page(settings, screen, menu_buttons, menu_page_text)
    ranking_page = Page(settings, screen, back_buttons, None)
    author_page = Page(settings, screen, back_buttons, None)
    settings_page = Page(settings, screen, settings_buttons, None)
    exit_page = ExitPage(settings, screen, None, None)
    game_page = GamePage(settings, screen, game_page_back_buttons, None, balls, player_brick, bricks, vector)
    login_page = LoginPage(settings, screen, login_page_buttons, login_page_text, input_box)

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





run_game()
