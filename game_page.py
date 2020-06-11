import sys
import time

import pygame

from functions import game_functions as gf, init_bricks as ibr


# 游戏的一般页面
from game_unit.brick import PlayBrick


class Page:
    def __init__(self, settings, screen, buttons, content):
        self.settings = settings
        self.screen = screen
        self.buttons = buttons
        self.content = content
        self.background_image = pygame.image.load('texture/background.png')
        self.background_rect = self.background_image.get_rect()
        self.background_rect.center = self.screen.get_rect().center

    def draw_background_image(self):
        self.screen.blit(self.background_image, self.background_rect)

    def run(self):
        self.draw_background_image()
        while True:
            time.sleep(0.01)
            self.content.draw_self()
            mouse_pos = pygame.mouse.get_pos()
            # 用来处理按钮按下的信息 当按钮按下则退出页面
            if gf.check_button_events(mouse_pos, self.buttons):
                print('Pushed')
                return
            # 鼠标移动到按钮上会改变按钮的颜色
            for button in self.buttons:
                button.draw_self(mouse_pos)
                pygame.display.flip()


# 游戏登陆页面
class LoginPage(Page):
    def __init__(self, settings, screen, buttons, content, input_box, account):
        super().__init__(settings, screen, buttons, content)
        self.input_box = input_box
        self.account = account
        self.image = pygame.image.load('texture/login_page.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen.get_rect().center

    def run(self):
        self.draw_background_image()
        self.screen.blit(self.image, self.image_rect)
        while True:
            time.sleep(0.01)
            self.content.draw_self()
            # 绘制输入框的矩形
            pygame.draw.rect(self.screen, self.settings.screen_color, self.input_box.rect, 0)
            mouse_pos = pygame.mouse.get_pos()
            self.input_box.draw_self()
            # 检查登陆的相关事件
            if gf.check_login_events(mouse_pos, self.buttons, self.input_box):
                self.account.set_name(self.input_box.text)
                print('Pushed')
                return
            # 鼠标移动到按钮上会改变按钮的颜色
            for button in self.buttons:
                button.draw_self(mouse_pos)
                pygame.display.flip()


# 退出的页面 方便以后加入退出消息
class ExitPage(Page):
    def __init__(self, settings, screen, buttons, content):
        super().__init__(settings, screen, buttons, content)

    def run(self):
        # 直接退出
        sys.exit()


class GamePage(Page):
    def __init__(self, settings, screen, buttons, content, balls,
                 bricks, vector, account, status, play_back):
        super().__init__(settings, screen, buttons, content)
        # 游戏的各种组件
        self.balls = balls
        self.player_brick = None
        self.bricks = bricks
        self.vector = vector
        self.account = account
        self.status = status
        self.play_back = play_back
        # 游戏游玩界面的大小 方便刷新游玩界面
        self.game_rect = pygame.Rect(0, 0, self.screen.get_rect().width - 200, self.screen.get_rect().height)
        self.game_background_image = pygame.image.load('texture/game_page_background.png')

    def run(self):
        # 加载玩家的砖块
        self.player_brick = PlayBrick(self.settings, self.screen)
        # 加载游戏砖块
        ibr.get_bricks(self.settings, self.bricks, self.screen)
        self.account.time_start()
        # 绘制一条分割线，将游戏的实时信息与游玩界面分割开来
        pygame.draw.line(self.screen, (0, 0, 0), (self.screen.get_rect().width - 199, 0),
                         (self.screen.get_rect().width - 199, self.screen.get_rect().height), 1)
        self.status.ball_num = 3

        while True:
            time.sleep(0.001)
            # 刷新游玩界面
            self.screen.blit(self.game_background_image, self.game_rect)

            mouse_pos = pygame.mouse.get_pos()
            # 绘制游戏必要的文字信息
            self.content.draw_self()
            # 分数
            self.account.draw_score(self.screen)
            # 剩余球的个数
            self.status.draw_ball_num()
            # 绘制玩家自己的砖块与砖块信息更新
            self.player_brick.draw_self()
            self.player_brick.update()
            # 球发射的方向跟新 和 绘制方向箭头
            self.vector.update(self.player_brick)
            self.vector.draw_self()
            # 砖块的绘制与更新
            for brick in self.bricks:
                brick.draw_self()
                brick.update()
                # 移除死亡的砖块
                if brick.isAlive is False:
                    self.account.score += 1
                    self.bricks.remove(brick)
            # 球的绘制与更新
            for ball in self.balls:
                ball.draw_self()
                ball.update(self.bricks, self.player_brick)
                # 球落到程序显示框一下则移除球
                if ball.rect.top > self.screen.get_rect().bottom:
                    print("a ball dead")
                    self.balls.remove(ball)
            # 鼠标移动到按钮上会改变按钮的颜色
            for button in self.buttons:
                button.draw_self(mouse_pos)
                pygame.display.flip()

            if gf.check_game_events(self.settings, self.screen, mouse_pos, self.buttons,
                                    self.balls, self.player_brick, self.vector, self.status, self.play_back):
                # 一个游戏回合的结束 储存账户信息，并清空所有的砖块和球
                self.account.time_end()
                self.account.store_info()
                self.account.score = 0
                self.bricks.empty()
                self.balls.empty()
                print('Pushed')
                return
