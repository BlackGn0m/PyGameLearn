import pygame
import random

BASE_WIDTH = 800
BASE_HEIGHT = 600


class TestSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, text='test sprite'):
        pygame.sprite.Sprite.__init__(self)
        self._dx = dx
        self._dy = dy
        font = pygame.font.SysFont('Consolas', 20)
        self.image = font.render(text, True, (0, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        if self.rect.x + self._dx < 0 or \
                (self.rect.x + self.rect.width) + self._dx > BASE_WIDTH:
            self._dx *= -1
        if self.rect.y + self._dy < 0 or \
                (self.rect.y + self.rect.height) + self._dy > BASE_HEIGHT:
            self._dy *= -1
        self.rect.x += self._dx
        self.rect.y += self._dy

    @property
    def speed(self):
        return self._dx, self._dy

    @speed.setter
    def speed(self, newvalue):
        self._dx = newvalue[0]
        self._dy = newvalue[1]


def detectCollision(group):
    for sp in group:
        collist = pygame.sprite.spritecollide(sp, group, False)
        for cs in collist:
            if cs is sp:
                continue

    pass


def main():
    pygame.init()
    display = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT))
    pygame.display.set_caption('Sprite and Group test')
    clock = pygame.time.Clock()
    sg = pygame.sprite.Group()
    for i in range(10):
        x = random.randint(100, BASE_WIDTH - 100)
        y = random.randint(100, BASE_HEIGHT - 100)
        ts = TestSprite(x, y, 3, 3, f'TEST_{i}')
        sg.add(ts)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
        display.fill((200, 200, 200))
        sg.draw(display)
        detectCollision(sg)
        sg.update()
        pygame.display.update()
        clock.tick(60)

    pass


if __name__ == '__main__':
    main()
