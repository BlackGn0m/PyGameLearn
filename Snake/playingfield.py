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
        # self._menurect = ()
        self._font = pygame.font.Font('res/a_lcdnova.ttf',
                                      self._const.SCOREFONTSIZE)
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
        # self._menurect = ()

    def update(self):
        pygame.draw.rect(self._display, self._const.BORDERCOLOR,
                         (0, 0, self._width, self._height),
                         self._margin)
        x = int(self._width * self._const.MENURATIO)

        pygame.draw.line(self._display, self._const.BORDERCOLOR, (x, 0),
                         (x, self._height), self._margin)
        self._showGameInfo()
        if self._const.DEBUG:
            self._showgrid()
        pass

    def _showGameInfo(self):
        if self._display is None:
            return
        x = self._margin * 2
        y = self._margin * 2
        dy = self._font.get_height()
        dy += dy // 2
        tmpSurf = self._font.render('ОЧКИ:', True, self._const.SCORECOLOR)
        self._display.blit(tmpSurf, (x, y))
        y += dy
        scorestr = '{:010d}'.format(self._score)
        tmpSurf = self._font.render(scorestr, True, self._const.SCORECOLOR)
        self._display.blit(tmpSurf, (x, y))

    @property
    def score(self):
        return self._score

    def addScore(self, addpoints):
        if addpoints > 0:
            self._score += addpoints

    def _showgrid(self):
        if self._display is None:
            return
        x = int(self._width * self._const.MENURATIO + self._margin//2)
        y = self._margin
        dy = (self._display.get_height() - self._margin * 2) // 30
        dx = (self._display.get_width() - x - self._margin * 2) // 30
        for i in range(31):
            pygame.draw.line(self._display, (255, 0, 0),
                             (x + i * dx, self._margin),
                             (x + i * dx,
                              self._display.get_height() - self._margin), 1)
