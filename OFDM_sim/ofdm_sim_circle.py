# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:09:12 2021

@author: josh
"""

import time
from decimal import *
import math
pi = math.pi

getcontext().prec = 10

def PointsInCircum(r,x,n):
    return [math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r]
	
	#getcontext().prec = 10
	#latitude_bike = 42.34882736
	#longitude_bike = -71.10541540
	#while(1):
	#	bike_gps_file = open("bike_gps_data.txt", "w") #make sure to later only read from the file. and close after reading.
	#	text = "18:55:05, " + str(latitude_bike) +" ," + str(longitude_bike) + "\n"
	#	textgroup = text
	#	for i in range(1000):
	#		textgroup+=text
	#	bike_gps_file.write(textgroup)
	#	bike_gps_file.close()
	#	longitude_bike = Decimal(longitude_bike) + Decimal(0.00000001)
	#	print("bike: " + str(longitude_bike))
	#	time.sleep(0.5)
t = []
times = []
for x in range(0,30):
    t.append(PointsInCircum(5e-05,x,29))
    temp = time.localtime()
    current_time = time.strftime("%H:%M:%S", temp)
    times.append(current_time)
for x in range(0,30):
    t.append(PointsInCircum(5e-05,x,29))
    temp = time.localtime()
    current_time = time.strftime("%H:%M:%S", temp)
    times.append(current_time)

base_lat = 42.00000000
base_long = -71.00000000
data_list = []
for ii in range(0,len(times)):
    temp = [times[0], base_lat + t[ii][0], base_long + t[ii][1]]
    data_list.append(temp)
f = open("circle_gps_data.txt","w")
f.close()
f = open("circle_gps_data.txt","a")

for ii in range(0,len(data_list)):
    data_list_small = data_list[ii]
    data = str(data_list_small[0]) +", " + str(Decimal(data_list_small[1]) + Decimal(0.00000001)) + ", " + str(Decimal(data_list_small[2]) + Decimal(0.00000001)) + ",\n"
    f.write(data)
f.close()


f2 = open("car_gps_data.txt","w")
data = str(data_list_small[0]) +", " + str(Decimal(base_lat) + Decimal(0.00000001)) + ", " + str(Decimal(base_long) + Decimal(0.00000001)) + ",\n"
f2.write(data)
f2.close()
