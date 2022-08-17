import pygame
from const import Const
from playingfield import PlayingField


def main():
    pygame.init()
    vi = pygame.display.Info()
    flags = pygame.HWSURFACE
    const = Const()
    winWidth = const.BASEWIDTH
    winHeight = const.BASEHEIGHT
    if not const.DEBUG:
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
        display.fill(const.BGCOLOR)
        playingField.update()

        # -------- Update display ----------------
        pygame.display.update()
        clock.tick(const.FPS)


if __name__ == '__main__':
    main()
