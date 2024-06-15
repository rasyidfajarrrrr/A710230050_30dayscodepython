class RemoteTv:
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    # Extra method for debugging
    def show(self):
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

# Main code
remoteSatu = RemoteTv()

# Turn switch on, and raise the level 5 times
remoteSatu.turnOn()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.raiseLevel()
remoteSatu.show()

# Lower the level 2 times, and turn switch off
remoteSatu.lowerLevel()
remoteSatu.lowerLevel()
remoteSatu.turnOff()
remoteSatu.show()
