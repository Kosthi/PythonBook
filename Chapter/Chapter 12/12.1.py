#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame, sys


# In[ ]:


class MyFavorChar:
    """最喜欢的角色的类"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800)) 
        self.screen_rect = self.screen.get_rect()
        # 加载角色并获取其外接矩形
        self.image = pygame.image.load('person.png')
        self.rect = self.image.get_rect()
        # 设置角色显示在屏幕中央
        self.rect.center = self.screen_rect.center
        pygame.display.set_caption('Show yourself')
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 255, 255))
            self.screen.blit(self.image, self.rect)
            pygame.display.flip()
            
myfavorchar = MyFavorChar()
myfavorchar.run_game()


# In[1]:


get_ipython().system('jupyter nbconvert --to script 12.1.ipynb')


# In[ ]:




