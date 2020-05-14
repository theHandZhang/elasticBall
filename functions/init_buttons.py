from game_unit.button import Button, LoginButton, RegisterButton


def init_menu_buttons(settings, screen):
    button_y = screen.get_rect().centery
    button_x = screen.get_rect().centerx - (settings.button_width / 2)
    buttons = [Button(settings, screen, (button_x, button_y + 60 * 0), 'Start'),
               Button(settings, screen, (button_x, button_y + 60 * 1), 'Ranking'),
               Button(settings, screen, (button_x, button_y + 60 * 2), 'Settings'),
               Button(settings, screen, (button_x, button_y + 60 * 3), 'Author'),
               Button(settings, screen, (button_x, button_y + 60 * 4), 'Exit')]
    return buttons


def init_back_buttons(settings, screen):
    button_y = screen.get_rect().centery
    button_x = screen.get_rect().centerx - (settings.button_width / 2)
    buttons = [Button(settings, screen, (button_x, button_y + 60 * 5), 'Back')]
    return buttons


def init_settings_buttons(settings, screen):
    button_y = screen.get_rect().centery
    button_x = screen.get_rect().centerx - (settings.button_width / 2)
    buttons = [Button(settings, screen, (button_x - 100, button_y + 60 * 5), 'Save'),
               Button(settings, screen, (button_x + 100, button_y + 60 * 5), 'Back')]
    return buttons


def init_game_page_back_buttons(settings, screen):
    button_x = screen.get_rect().width
    buttons = [Button(settings, screen, (button_x - 175, 20), 'Back')]
    return buttons


def init_login_buttons(settings, screen):
    button_x = screen.get_rect().centerx
    buttons = [RegisterButton(settings, screen, (button_x - 200, screen.get_rect().height * 0.7), 'Register'),
               LoginButton(settings, screen, (button_x + 50, screen.get_rect().height * 0.7), 'Login')]
    return buttons
