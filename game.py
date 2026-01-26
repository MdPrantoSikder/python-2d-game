import pygame
pygame.init()

screen= pygame.display.set_mode((800,600))
clock= pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  .tick(60)
pygame.display.update()
clock