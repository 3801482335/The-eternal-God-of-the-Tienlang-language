import pygame
pygame.init()
# 设定游戏窗口的大小
screen = pygame.display.set_mode((800, 600))
# 游戏的主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 在这里添加你的游戏逻辑，例如绘制图像，移动角色等。
    
pygame.quit()
