import pygame


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
