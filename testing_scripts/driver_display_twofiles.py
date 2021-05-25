import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation


#####################################
# File
bike_path = 'bike_gps_data.txt'
car_path = 'car_gps_data.txt'

# fp = open(filepath)
# line = fp.readline()

coordinates = [0.0, 0.0, 0.0, 0.0]

car_coords = [0.0, 0.0]
bike_coords = [0.0, 0.0]
#####################################

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(-20,20), ylim=(-20, 20))

bike = plt.Rectangle((-1.5, -4), 1, 4)
car = plt.Rectangle((-1.5, -4), 3, 8)
ax.add_patch(car)
warning = plt.text(-15, 15, ' yeet')

def init():
    ax.add_patch(bike)
    bike.set_color('yellow')
    return bike,

def animate(i):

	bp = open(bike_path)
	b_line = bp.readline()

	cp = open(car_path)
	c_line = cp.readline()

	bike_coords_str = []
	car_coords_str = []

	if (len(b_line) > 0 and len(c_line) > 0):
		bike_coords_str = b_line.split(", ")
		bike_coords[0] = float(bike_coords_str[1])
		bike_coords[1] = float(bike_coords_str[2])

		car_coords_str = c_line.split(", ")
		car_coords[0] = float(car_coords_str[1])
		car_coords[1] = float(car_coords_str[2])

		print("car coords: " + str(car_coords[0]) + ", " + str(car_coords[1]))
		print("bike coords: " + str(bike_coords[0]) + ", " + str(bike_coords[1]))


		x = math.floor(364629.27676 * (bike_coords[1] - car_coords[1]))
		y = math.floor(364629.27676 * (bike_coords[0] - car_coords[0]))
		dist = ((x**2)+(y**2))**0.5

		if (dist < 15):
		    bike.set_color('red')
		else:
		    bike.set_color('yellow')
		    
		bike.xy = (x, y)
		print("dist: " + str(dist))
		warning.set_text= 'Warning'
	else:
		bike.xy = (200, 200)
		print(bike.xy)

	warning.set_text= 'Warning'


	return bike, warning


anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=100,
                               blit=True)

plt.show()



