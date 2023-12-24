from gpiozero import OutputDevice
import datetime
import os

class Relay(OutputDevice):
	def __init__(self, pin, active_high):
		super(Relay, self).__init__(pin, active_high)
		
class MockedRelay:
    def __init__(self, pin, active_high):
        self.pin = pin
        self.active_high = active_high
        self.active = False
        self.logName = "pin" + str(self.pin) + ".txt"
    def on(self):
        print("RelayOn")
        self.setActive(True)
    def off(self):
        print("RelayOff")
        self.setActive(False)
    def toggle(self):
        print("RelayToggle")
        self.asetActive(not self.active)
        
    def setActive(self, value):
        self.active = value
        self.write("Relay set " + ("ON" if self.active else "OFF"))
        
    def write(self, message):
        f = open(self.logName, "a")
        f.write(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S") + ": " + message + "\n")
        f.close()
    def read(self):
        if (not os.path.exists(self.logName)):
            return ""
        f = open(self.logName, "r")
        res = f.read()
        f.close()
        return res;
        

        

