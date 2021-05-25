#simulates a bike and car crossing paths.
#starts at 00:00:00, 42.3497395, -71.1063577,
from decimal import *

getcontext().prec = 10

bike_lat = 42.34976050
car_lat = 42.34974050

bike_long = -71.10633080
car_long = -71.10637580

car_gps_file = open("sim_cross_car.txt", "w")
bike_gps_file = open("sim_cross_bike.txt", "w")

for x in range(60):
	bike_long = Decimal(bike_long) - Decimal(0.000002)
	car_long = Decimal(car_long) + Decimal(0.000002)
	bike_lat = Decimal(bike_lat) + Decimal(0.000002)
	car_lat = Decimal(car_lat) + Decimal(0.000002)
	
	bike_gps_file.write("00:00:00, " + str(bike_lat) + ", " + str(bike_long) + ",\n")
	car_gps_file.write("00:00:00, " + str(car_lat) + ", " + str(car_long) + ",\n")
