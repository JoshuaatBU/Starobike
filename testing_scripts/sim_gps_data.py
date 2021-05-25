import time
from decimal import *


def write_bike_gps():
	
	getcontext().prec = 10
	latitude_bike = 42.34882736
	longitude_bike = -71.10541540
	while(1):
		bike_gps_file = open("bike_gps_data.txt", "w") #make sure to later only read from the file. and close after reading.
		bike_gps_file.write("18:55:05, " + str(latitude_bike) +" ," + str(longitude_bike) + ",\n")
		bike_gps_file.close()
		longitude_bike = Decimal(longitude_bike) + Decimal(0.00000001)
		latitude_bike = Decimal(latitude_bike) + Decimal(0.00000001)
		print("bike: " + str(longitude_bike))
		time.sleep(0.5)
		
		
write_bike_gps()
