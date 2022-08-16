import pygame

# ------ Global variable -----------------
FPS = 60
WHITE = (255, 255, 255)
GREEN = (100, 200, 100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DEBUG = True
BASE_WIDTH = 1024
BASE_HEIGHT = 768


class PlayingField:
    def __init__(self, display):
        if not isinstance(display, pygame.Surface):
            err = f'PLAYING FIELD: "display" should have class pygame.Surface,'
            err += f' but it is {type(display)}'
            raise TypeError(err)
        self._display = display
        pass

    def update(self):
        pass


def main():
    pygame.init()
    vi = pygame.display.Info()
    flags = pygame.HWSURFACE
    winWidth = BASE_WIDTH
    winHeight = BASE_HEIGHT
    if not DEBUG:
        flags |= pygame.FULLSCREEN
        winWidth = vi.current_w
        winHeight = vi.current_h
    display = pygame.display.set_mode((winWidth, winHeight), flags)
    clock = pygame.time.Clock()
    playingField = PlayingField(display)

    gameStop = False
    gamePause = False
    while not gameStop:
        # ------- Process event --------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                gameStop = True
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    gameStop = True
                    continue
                if event.key == pygame.K_UP:
                    # Move up
                    pass
                if event.key == pygame.K_DOWN:
                    # Move down
                    pass
                if event.key == pygame.K_LEFT:
                    # Move left
                    pass
                if event.key == pygame.K_RIGHT:
                    # Move right
                    pass
                if event.key == pygame.K_p:
                    gamePause = not gamePause

        if gameStop:
            continue
        # -------- Paint playing field -----------
        display.fill(GREEN)
        playingField.update()

        # -------- Update display ----------------
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
