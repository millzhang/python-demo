import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        # 初始化飞船并设置初始位置
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')  #返回一个pygame.Surface对象
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #rect 将只存储这个值的整数部分。为准确地存储飞船的位置，我们定义了一个可存储小数值的新属性 self.center
        self.center = float(self.rect.centerx)

        #移动标识
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标识调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
