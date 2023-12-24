from classes import Hardware
import time

class Hub():
    relays = {
        "bazil": Hardware.MockedRelay(12, False),
        "aloe": Hardware.MockedRelay(15, False),
    }
    
    def readHistory(self, relayId):
        if (relayId not in self.relays):
            return False
        return self.relays[relayId].read()

    def water_plant(self, relayId, seconds):
        if (relayId not in self.relays):
            return False
        self.relays[relayId].on()
        print("Plant is being watered!")
        time.sleep(seconds)
        print("Watering is finished!")
        self.relays[relayId].off()
        return True
