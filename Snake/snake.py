import pygame


class Snake:
    def __init__(self, display):
        if not isinstance(display, pygame.Surface):
            err = f'SNAKE: "display" should have class pygame.Surface,'
            err += f' but it is {type(display)}'
            raise TypeError(err)
        self._length = 2
        self.body = []

        pass

    @property
    def length(self):
        return self._length
