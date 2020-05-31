from game_unit.button import Button, LoginButton, RegisterButton


def init_menu_buttons(settings, screen, play_back):
    button_y = screen.get_rect().centery
    button_x = screen.get_rect().centerx - (settings.button_width / 2)
    buttons = [Button(settings, screen, (button_x, button_y + 60 * 0), 'Start', play_back),
               Button(settings, screen, (button_x, button_y + 60 * 1), 'Ranking', play_back),
               Button(settings, screen, (button_x, button_y + 60 * 2), 'Settings', play_back),
               Button(settings, screen, (button_x, button_y + 60 * 3), 'Author', play_back),
               Button(settings, screen, (button_x, button_y + 60 * 4), 'Exit', play_back)]
    return buttons


def init_back_buttons(settings, screen, play_back):
    button_y = screen.get_rect().centery
    button_x = screen.get_rect().centerx - (settings.button_width / 2)
    buttons = [Button(settings, screen, (button_x, button_y + 60 * 5), 'Back', play_back)]
    return buttons


def init_settings_buttons(settings, screen, play_back):
    button_y = screen.get_rect().centery
    button_x = screen.get_rect().centerx - (settings.button_width / 2)
    buttons = [Button(settings, screen, (button_x - 100, button_y + 60 * 5), 'Save', play_back),
               Button(settings, screen, (button_x + 100, button_y + 60 * 5), 'Back', play_back)]
    return buttons


def init_game_page_back_buttons(settings, screen, play_back):
    button_x = screen.get_rect().width
    buttons = [Button(settings, screen, (button_x - 175, 20), 'Back', play_back)]
    return buttons


def init_login_buttons(settings, screen, play_back):
    button_x = screen.get_rect().centerx
    buttons = [
            RegisterButton(settings, screen, (button_x - 200, screen.get_rect().height * 0.7), 'Register', play_back),
            LoginButton(settings, screen, (button_x + 50, screen.get_rect().height * 0.7), 'Login', play_back)
    ]
    return buttons
