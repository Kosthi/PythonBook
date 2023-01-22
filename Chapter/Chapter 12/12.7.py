import pygame, sys

class Rocket:
    """火箭类"""
    def __init__(self, mainwindow):
        self.screen = mainwindow.screen
        self.screen_rect = self.screen.get_rect()
        
        # 加载火箭并获取其外接矩形
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        
        # 设置火箭显示在屏幕中央
        self.rect.center = self.screen_rect.center
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
        self.screen.blit(self.image, self.rect)
    
    def update(self):
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
        # print(self.rect.x, self.rect.y)

class MainWindow:
    """主窗口类"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800)) 
        self.rocket = Rocket(self)
        self.screen_rect = self.screen.get_rect()
        
    def run_game(self):
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
            pygame.display.flip()
            
    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        
mainwindown = MainWindow()
mainwindown.run_game()