class CalcBtn:

    def getText(self):
        return self.text

    def getButton(self):
        return self.button

    def setButton(self, btn):
        self.button = btn

    def __init__(self, text, command=None, bg="gray94"):
        self.text = text
        self.button = None
        self.command = command
        self.bg = bg
