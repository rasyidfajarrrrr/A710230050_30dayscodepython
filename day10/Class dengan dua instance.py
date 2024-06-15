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
oLightSwitch1 = LightSwitch()
oLightSwitch2 = LightSwitch()

# Test code
oLightSwitch1.show()  # Initially off, should print False
oLightSwitch2.show()  # Initially off, should print False

oLightSwitch1.turnOn()  # Turn switch 1 on
oLightSwitch2.turnOff()  # Ensure switch 2 is off

oLightSwitch1.show()  # Should print True
oLightSwitch2.show()  # Should print False
