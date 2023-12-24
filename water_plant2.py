from classes import Hardware
from classes import TimeKeeper as TK
import smtplib
import time
import ssl

# WATERING_TIME must be in "00:00:00 PM" format
WATERING_TIME = '08:24:30 PM'
SECONDS_TO_WATER = 10
#pin15
hub = PolivHub.Hub()

def main():
    time_keeper = TK.TimeKeeper(TK.TimeKeeper.get_current_time())
    print("Start!", time_keeper.current_time)
    if(time_keeper.current_time == WATERING_TIME):
        hub.water_plant('aloe', SECONDS_TO_WATER)
        time_keeper.set_time_last_watered(TK.TimeKeeper.get_current_time())
        print("\nPlant was last watered at {}".format(time_keeper.time_last_watered))
       
while True:
    time.sleep(1)
    main()
