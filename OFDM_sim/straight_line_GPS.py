

Car= "03:24:30, 42.35120512, -71.10583313"
f = open("car_straight_line.txt","w")
f.write(Car)
f.write("/n")
f.close()
#bike: 03:24:30, 42.35117712, -71.10571013



from decimal import *
bike_time="03:24:30, "
bike_lat="42.35135512, "
bike_lon= -71.10571013

#making the bike data
runs=[1,2]
outF = open("straight_line.txt", "w")
outF.close()
for trip in runs:
	index=[1,2,3,4,5,6,7,8,9,10]
	outF = open("straight_line.txt","a")
	for val in index:

		bike_lon= Decimal(bike_lon) - Decimal(0.00001)
		bike_lon_str=str(bike_lon)[0:11]
		GPS_line=bike_time+bike_lat+bike_lon_str
		outF.write(GPS_line)
		outF.write(", \n")

	
	for val in index:

		bike_lon= Decimal(bike_lon) + Decimal(.00005)

		bike_lon = Decimal(bike_lon) + Decimal(0.00000001)

		bike_lon_str=str(bike_lon)[0:11]
		GPS_line=bike_time+bike_lat+bike_lon_str
		outF.write(GPS_line)
		outF.write(", \n")
	outF.close()
