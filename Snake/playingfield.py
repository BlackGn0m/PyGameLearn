import pygame
from const import Const


class PlayingField:
    def __init__(self, display):
        if not isinstance(display, pygame.Surface):
            err = f'PLAYING FIELD: "display" should have class pygame.Surface,'
            err += f' but it is {type(display)}'
            raise TypeError(err)
        self._const = Const()
        self._display = None
        self._width = 0
        self._height = 0
        self._margin = 0
        self._fieldrect = ()
        # self._menurect = ()
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
        pass
