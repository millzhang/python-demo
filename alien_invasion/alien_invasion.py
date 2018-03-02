import sys
import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #  初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵啦")
    # 创建飞船
    ship = Ship(ai_settings, screen)
    bullets = Group()
    #  开始游戏的主循环
    while True:
        #  监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()