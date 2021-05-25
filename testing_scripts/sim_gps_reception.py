#This test bench simulates gps coordinates being written to two data files (one for the car, one for the bike), that are interpreted by the script running the driver display. It is meant to appear as if the bike is being passed by the car.

import time
import threading
from decimal import *


def write_bike_gps():
	
	getcontext().prec = 10
	latitude_bike = 42.34872736
	longitude_bike = -71.10541010
	while(1):
		bike_gps_file = open("bike_gps_data.txt", "w") #make sure to later only read from the file. and close after reading.
		bike_gps_file.write("18:55:05, " + str(latitude_bike) + ", " + str(longitude_bike))
		bike_gps_file.close()
		latitude_bike = Decimal(latitude_bike) + Decimal(0.00001111)
		print("bike: " + str(latitude_bike) + ", " + str(longitude_bike))
		time.sleep(2)

		

def write_car_gps():
	getcontext().prec = 10
	latitude = 42.34882736
	longitude = -71.10541534
	while(1):
		car_gps_file = open("car_gps_data.txt", "w")
		car_gps_file.write("18:55:05, "+ str(latitude) +", " + str(longitude))
		car_gps_file.close()
		longitude = Decimal(longitude) + Decimal(0.00000001)
		print("car: " + str(latitude) +", " + str(longitude))
		time.sleep(1.8)


t1 = threading.Thread(target=write_bike_gps)
t2 = threading.Thread(target=write_car_gps)
	
t1.start()
t2.start()
