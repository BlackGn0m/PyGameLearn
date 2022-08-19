import pygame
import random

BASE_WIDTH = 800
BASE_HEIGHT = 600


def isPositiv(x):
    if x >= 0:
        return 1
    else:
        return 0


class TestSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, text='test sprite'):
        pygame.sprite.Sprite.__init__(self)
        self._dx = dx
        self._dy = dy
        self._text = text
        self._buildTxt(x, y)

    def _buildTxt(self, x, y):
        font = pygame.font.SysFont('Consolas', 20)
        txt = f'{self._text} ({isPositiv(self._dx)},{isPositiv(self._dy)})'
        self.image = font.render(txt, True, (0, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        rbt = False
        if self.rect.x + self._dx < 0 or \
                (self.rect.x + self.rect.width) + self._dx > BASE_WIDTH:
            self._dx *= -1
            rbt = True
        if self.rect.y + self._dy < 0 or \
                (self.rect.y + self.rect.height) + self._dy > BASE_HEIGHT:
            self._dy *= -1
            rbt = True
        if rbt:
            self._buildTxt(self.rect.x, self.rect.y)
        self.rect.x += self._dx
        self.rect.y += self._dy

    @property
    def speed(self):
        return self._dx, self._dy

    @speed.setter
    def speed(self, newvalue):
        self._dx = newvalue[0]
        self._dy = newvalue[1]
        self._buildTxt(self.rect.x, self.rect.y)

    def invertDx(self):
        self._dx = -self._dx
        self._buildTxt(self.rect.x, self.rect.y)

    def invertDy(self):
        self._dy = -self._dy
        self._buildTxt(self.rect.x, self.rect.y)

    def invertSpeed(self):
        self._dx *= -1
        self._dy *= -1
        self._buildTxt(self.rect.x, self.rect.y)


def detectCollision(group):
    processed = []
    for sp in group:
        collist = pygame.sprite.spritecollide(sp, group, False)
        for cs in collist:
            if cs is sp:
                continue
            if (sp, cs) in processed:
                continue
            processed.append((sp, cs))
            processed.append((cs, sp))
            # RightBottom (LeftToRight or TopToBottom)
            if cs.rect.collidepoint(sp.rect.right, sp.rect.bottom):
                if abs(cs.rect.left - sp.rect.right) > abs(
                        cs.rect.top - sp.rect.bottom):  # LeftToRight
                    sp.invertDx()
                    cs.invertDx()
                    continue
                else:  # TopToBottom
                    sp.invertDy()
                    cs.invertDy()
                    continue
            # RightTop (LeftToRight or BottomToTop)
            if cs.rect.collidepoint(sp.rect.right, sp.rect.top):
                if abs(cs.rect.left - sp.rect.right) > abs(
                        cs.rect.bottom - sp.rect.top):  # LeftToRight
                    sp.invertDx()
                    cs.invertDx()
                    continue
                else:  # BottomToTop
                    sp.invertDy()
                    cs.invertDy()
                    continue
            # LeftTop (RightToLeft or BottomToTop)
            if cs.rect.collidepoint(sp.rect.left, sp.rect.top):
                if abs(cs.rect.right - sp.rect.left) > abs(
                        cs.rect.bottom - sp.rect.top):  # RightToLeft
                    sp.invertDx()
                    cs.invertDx()
                    continue
                else:  # BottomToTop
                    sp.invertDy()
                    cs.invertDy()
                    continue
            # LeftBottom (RightToLeft or TopToBottom)
            if cs.rect.collidepoint(sp.rect.left, sp.rect.bottom):
                if abs(cs.rect.right - sp.rect.left) > abs(
                        cs.rect.top - sp.rect.bottom):  # RightToLeft
                    sp.invertDx()
                    cs.invertDx()
                    continue
                else:  # TopToBottom
                    sp.invertDy()
                    cs.invertDy()
                    continue

    pass


def detectCollision2(group):
    processed = []
    for sp in group:
        collist = pygame.sprite.spritecollide(sp, group, False)
        for cs in collist:
            if cs is sp:
                continue
            if (sp, cs) not in processed:
                processed.append((sp, cs))
                processed.append((cs, sp))
                sp.invertSpeed()
                cs.invertSpeed()


def main():
    pygame.init()
    display = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT))
    pygame.display.set_caption('Sprite and Group test')
    clock = pygame.time.Clock()
    sg = pygame.sprite.Group()
    for i in range(10):
        x = random.randint(150, BASE_WIDTH - 150)
        y = random.randint(150, BASE_HEIGHT - 150)
        ts = TestSprite(x, y, 3, 3, f'TEST_{i}')
        sg.add(ts)

    isStep = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    # sg.update()
                    detectCollision2(sg)
                    sg.update()
                if event.key == pygame.K_s:
                    isStep = not isStep

        display.fill((200, 200, 200))
        sg.draw(display)
        if not isStep:
            detectCollision2(sg)
            sg.update()
        pygame.display.update()
        clock.tick(60)

    pass


if __name__ == '__main__':
    main()
