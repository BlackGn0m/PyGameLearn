import pygame

BASE_WIDTH = 800
BASE_HEIGHT = 600
FPS = 60
COLOR_WHITE = (200, 200, 200)
COLOR_RED = (255, 100, 100)
COLOR_GREEN = (100, 255, 100)

# Direction constant
DIRECT_LEFT = 0
DIRECT_RIGHT = 1
DIRECT_UP = 2
DIRECT_DOWN = 3


class Chain:
    def __init__(self, display, speed=1):
        self._display = display
        self._width = display.get_width()
        self._height = display.get_height()
        self._length = 1
        self._elems = []
        self._radius = 5
        self._speed = speed
        x = self._width // 2
        y = self._height // 2
        self._elems.append((x, y))
        self._direct = DIRECT_UP

    def showchain(self):
        for i in range(self._length):
            if i == self._length - 1:
                color = COLOR_GREEN
            else:
                color = COLOR_RED
            x, y = self._elems[i]
            pygame.draw.circle(self._display, color, (x, y), self._radius)

    def _changeCoord(self, x, y, change):
        if self._direct == DIRECT_LEFT:
            x -= change
        elif self._direct == DIRECT_RIGHT:
            x += change
        elif self._direct == DIRECT_UP:
            y -= change
        elif self._direct == DIRECT_DOWN:
            y += change
        return x, y

    def addElem(self):
        x, y = self._elems[-1]
        x, y = self._changeCoord(x, y, self._radius)
        self._elems.append((x, y))
        self._length += 1

    def changeDirect(self, newDirect):
        if newDirect == self._direct:
            return
        if newDirect not in [DIRECT_LEFT, DIRECT_RIGHT, DIRECT_UP,
                             DIRECT_DOWN]:
            return
        self._direct = newDirect

    def _checkCollision(self):
        headx, heady = self._elems[-1]
        headx, heady = self._changeCoord(headx, heady,
                                         self._speed + self._radius)
        if headx < 0 or headx > self._width:
            return True
        if heady < 0 or heady > self._height:
            return True
        return False

    def update(self):
        if self._checkCollision():
            return False
        for i in range(self._length - 1):
            self._elems[i] = self._elems[i + 1]
        x, y = self._elems[-1]
        x, y = self._changeCoord(x, y, self._speed)
        self._elems[-1] = (x, y)
        return True


def main():
    pygame.init()
    display = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT))
    clock = pygame.time.Clock()
    chain = Chain(display, 1)
    isEnd = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_LEFT:
                    chain.changeDirect(DIRECT_LEFT)
                if event.key == pygame.K_RIGHT:
                    chain.changeDirect(DIRECT_RIGHT)
                if event.key == pygame.K_UP:
                    chain.changeDirect(DIRECT_UP)
                if event.key == pygame.K_DOWN:
                    chain.changeDirect(DIRECT_DOWN)
                if event.key == pygame.K_KP_PLUS:
                    chain.addElem()
        # ---------- Paint scene --------------
        display.fill(COLOR_WHITE)
        if not isEnd:
            isEnd = not chain.update()
        chain.showchain()

        # --------- Update display ------------
        pygame.display.update()
        clock.tick(FPS)
    pass


if __name__ == '__main__':
    main()
