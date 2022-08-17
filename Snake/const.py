class Const:
    def __init__(self):
        self._debug = True
        self._basewidth = 1024
        self._baseheight = 768
        self._fps = 60
        self._bgcolor = (100, 200, 100)
        pass

    @property
    def FPS(self):
        return self._fps

    @property
    def DEBUG(self):
        return self._debug

    @property
    def BGCOLOR(self):
        return self._bgcolor

    @property
    def BASEWIDTH(self):
        return self._basewidth

    @property
    def BASEHEIGHT(self):
        return self._baseheight
