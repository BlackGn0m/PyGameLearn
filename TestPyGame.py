import pygame
from sys import exit
from random import randint


# Функция, возвращающая случайный оттенок зеленого цвета
def randomGreen():
    return randint(0, 100), randint(100, 255), randint(0, 100)


# Функция, возвращающая случайный оттенок красного цвета
def randomRed():
    return randint(100, 255), randint(0, 100), randint(0, 100)


def getDispInfo():
    vi = pygame.display.Info()
    ws = pygame.display.get_wm_info()
    ds = pygame.display.get_desktop_sizes()
    print(vi)
    print(ws)
    print(ds)


res = pygame.init()
# getDispInfo()
vi = pygame.display.Info()
flags = pygame.FULLSCREEN | pygame.HWSURFACE
display = pygame.display.set_mode((vi.current_w, vi.current_h), flags)
bgsurf = pygame.surface.Surface((500, 500))
clock = pygame.time.Clock()
x = 0  # начальная позиция по оси X
y = 0  # начальная позиция по оси Y
while y < 500:  # Пока мы не достигли точки с координатой y == 500
    # Вложенный цикл для рисования линии из квадратиков
    while x < 500:  # Пока мы не достигли точки с координатой x == 500
        # Рисуем квадратик с координатами x, y
        pygame.draw.rect(bgsurf, randomGreen(), (x, y, 25, 25))
        x += 25  # Смещаем позицию квадратика по оси X
    # По завершению вложенного цикла увеличиваем переменную y
    # для перехода на новую строчку
    y += 25
    x = 0  # Возвращаем позицию по оси X в начало строчки

# Рисуем "мордочку" крипера
pygame.draw.rect(bgsurf, (0, 0, 0), (150, 200, 100, 100))
pygame.draw.rect(bgsurf, (0, 0, 0), (350, 200, 100, 100))
pygame.draw.rect(bgsurf, (0, 0, 0), (250, 300, 100, 100))
pygame.draw.rect(bgsurf, (0, 0, 0), (200, 350, 50, 100))
pygame.draw.rect(bgsurf, (0, 0, 0), (350, 350, 50, 100))

x = display.get_width() // 2
y = display.get_height() // 2
dx = 1
dy = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                (x, y) = event.pos
    display.fill((255, 255, 255))
    display.blit(bgsurf, (-50, 50))
    pygame.draw.circle(display, randomRed(), (x, y), 10)
    if x < 5 or x > display.get_width() - 5:
        dx *= -1
    if y < 5 or y > display.get_height() - 5:
        dy *= -1
    x += dx
    y += dy
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(60)
