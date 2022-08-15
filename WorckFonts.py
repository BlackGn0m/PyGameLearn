import pygame
from sys import exit

WHITE = (255, 255, 255)
GREEN = (100,200,100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60


def main():
    pygame.init()
    print(pygame.image.get_extended())
    vi = pygame.display.Info()
    flags = pygame.FULLSCREEN | pygame.HWSURFACE
    display = pygame.display.set_mode((vi.current_w, vi.current_h), flags)
    clock = pygame.time.Clock()

    x = display.get_width() // 2
    y = display.get_height() // 2
    dx = 1
    dy = 1

    fpsFont = pygame.font.SysFont('Consolas', 20, True)

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
        display.fill(GREEN)
        pygame.draw.circle(display, RED, (x, y), 10)
        fpsStr = f'FPS: {int(clock.get_fps())} TICK: {clock.tick()}'
        fpsSurf = fpsFont.render(fpsStr, True, RED)
        display.blit(fpsSurf, (10, 10))
        if x < 5 or x > display.get_width() - 5:
            dx *= -1
        if y < 5 or y > display.get_height() - 5:
            dy *= -1
        x += dx
        y += dy
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(FPS)
        #pygame.time.wait(1)


if __name__ == '__main__':
    main()
