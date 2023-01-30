import pygame, sys
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理飞船发射子弹的类"""
    def __init__(self, ai_game):
        """在当前位置创建一个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60, 60, 60)
        
        # 在(0, 0)处创建一个子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_game.rocket.rect.midright
        
        # 存储用小数表示的子弹位置
        self.x = float(self.rect.x)
        
    def update(self):
        """向右移动子弹"""
        # 更新表示子弹位置的小数值
        self.x += 1.25
        # 更新表示子弹rect的值
        self.rect.x = self.x
        
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
class Rocket:
    """管理火箭类"""
    def __init__(self, mainwindow):
        """初始化火箭并设置其初始位置"""
        self.screen = mainwindow.screen
        self.screen_rect = self.screen.get_rect()
        
        # 加载火箭并获取其外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        # 设置火箭显示在屏幕左中央
        self.rect.midleft = self.screen_rect.midleft
        pygame.display.set_caption('A rocket')
        
        # 移动标志
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        
        # 飞船速度
        self.ship_speed = 2
        
        # 飞船坐标
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def blitme(self):
        """绘制火箭"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """更新火箭位置"""
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

class MainWindow:
    """主窗口类"""
    def __init__(self):
        """初始化"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800)) 
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.screen_rect = self.screen.get_rect()
        
    def run_game(self):
        """开始游戏主循环"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
            
            self.screen.fill((0, 255, 255))
            self.rocket.update()
            self.rocket.blitme()
            self._update_bullets()
            pygame.display.flip()
            
    def _check_keydown_events(self, event):
        """按键按下"""
        print(event.key)
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        """按键松开"""
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
            
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
            else:
                bullet.draw_bullet()
        # print(len(self.bullets))
        
mainwindown = MainWindow()
mainwindown.run_game()