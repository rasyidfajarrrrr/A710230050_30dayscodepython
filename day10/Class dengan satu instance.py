class LightSwitch:
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)

# Main code
oLightSwitch = LightSwitch()

# Calls to methods
oLightSwitch.show()          # Initially off, should print False

oLightSwitch.turnOn()        # Turn on the switch
oLightSwitch.show()          # Should print True

oLightSwitch.turnOff()       # Turn off the switch
oLightSwitch.show()          # Should print False

oLightSwitch.turnOn()        # Turn on the switch again
oLightSwitch.show()          # Should print True
