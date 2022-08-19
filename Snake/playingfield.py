import pygame
from const import Const


class PlayingField:
    def __init__(self, display):
        if not isinstance(display, pygame.Surface):
            err = f'PLAYING FIELD: "display" should have class pygame.Surface,'
            err += f' but it is {type(display)}'
            raise TypeError(err)
        self._const = Const()
        self._display = display
        self._width = 0
        self._height = 0
        self._margin = 0
        self._fieldrect = ()
        self._score = 0
        self._level = 1
        # self._menurect = ()
        self._font = pygame.font.Font('res/a_lcdnova.ttf',
                                      self._const.SCOREFONTSIZE)
        self._fieldrect = pygame.rect.Rect(self._margin, self._margin,
                                           self._width - self._margin * 2,
                                           self._height - self._margin * 2)
        self.changeDisplay(display)
        pass

    def changeDisplay(self, display):
        if not isinstance(display, pygame.Surface):
            err = f'PLAYING FIELD: "display" should have class pygame.Surface,'
            err += f' but it is {type(display)}'
            raise TypeError(err)
        self._display = display
        self._width = display.get_width()
        self._height = display.get_height()
        self._margin = min(int(self._width * self._const.MARGINRATIO),
                           int(self._height * self._const.MARGINRATIO))
        self._fieldrect = pygame.rect.Rect(self._margin, self._margin,
                                           self._width - self._margin * 2,
                                           self._height - self._margin * 2)

    def update(self):
        pygame.draw.rect(self._display, self._const.BORDERCOLOR,
                         (0, 0, self._width, self._height),
                         self._margin)

        gameInfoHeight = self._showGameInfo()
        self._fieldrect = pygame.rect.Rect(self._margin, gameInfoHeight,
                                           self._width - self._margin * 2,
                                           self._height - self._margin -
                                           gameInfoHeight)
        pass

    def _showGameInfo(self):
        if self._display is None:
            return
        x = self._margin
        y = self._margin

        infoStr = f'Уровень {self.level:05d}'
        tmpSurf = self._font.render(infoStr, True, self._const.SCORECOLOR)
        infoHeight = tmpSurf.get_height()
        pygame.draw.rect(self._display, self._const.BORDERCOLOR,
                         (0, 0, self._width, self._margin * 2 + infoHeight))
        self._display.blit(tmpSurf, (x, y))

        infoStr = f'Очки {self._score:010d}'
        tmpSurf = self._font.render(infoStr, True, self._const.SCORECOLOR)
        x = self._width - self._margin - tmpSurf.get_width()
        self._display.blit(tmpSurf, (x, y))
        return infoHeight

    @property
    def score(self):
        return self._score

    @property
    def level(self):
        return self._level

    def updateScore(self, addpoints):
        if addpoints > 0:
            self._score += addpoints

    def nextLevel(self):
        self._level += 1
