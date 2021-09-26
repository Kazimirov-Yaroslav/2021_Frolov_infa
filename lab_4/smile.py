import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((200, 200, 200))
pygame.display.update()

dr.circle(screen, (255, 255, 0), (200, 200), 100)
dr.circle(screen, (0, 0, 0), (200, 200), 100, 1)

dr.circle(screen, (255, 0, 0), (150, 175), 20)
dr.circle(screen, (0, 0, 0), (150, 175), 20, 1)
dr.circle(screen, (0, 0, 0), (150, 175), 8)

dr.circle(screen, (255, 0, 0), (250, 175), 16)
dr.circle(screen, (0, 0, 0), (250, 175), 16, 1)
dr.circle(screen, (0, 0, 0), (250, 175), 8)

dr.rect(screen, (0, 0, 0), (145, 240, 110, 20))

dr.polygon(screen, (0, 0, 0), [(96, 112), (180, 158), (176, 166), (92, 120)])
dr.polygon(screen, (0, 0, 0), [(294, 129), (220, 160), (224, 168), (298, 136)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
