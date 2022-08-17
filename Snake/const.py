class Const:
    def __init__(self):
        self._debug = True
        self._basewidth = 1024
        self._baseheight = 600
        self._fps = 60

        # Colors
        self._bgcolor = (100, 200, 100)
        self._bordercolor = (50, 100, 50)

        # Ratios
        self._marginratio = 0.017
        self._menuratio = 0.25
        self._fieldratio = 0.75
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
    def BORDERCOLOR(self):
        return self._bordercolor

    @property
    def BASEWIDTH(self):
        return self._basewidth

    @property
    def BASEHEIGHT(self):
        return self._baseheight

    @property
    def MARGINRATIO(self):
        return self._marginratio

    @property
    def MENURATIO(self):
        return self._menuratio

    @property
    def FIELDRATIO(self):
        return self._fieldratio
