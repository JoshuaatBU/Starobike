import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation

#####################################
# File
filepath = 'fake_GPS_data_loop.txt'
fp = open(filepath)
line = fp.readline()
coordinates = [0.0, 0.0, 0.0, 0.0]
#####################################


#####################################
# Figure
fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)
ax = plt.axes(xlim=(-20,20), ylim=(-20, 20))
ax.set_facecolor((0, 0, 0))
#####################################


#####################################
# Patches
bike = plt.Rectangle((-1, -1), 1, 1)
car = plt.Rectangle((-1.5, -4), 3, 8)
ax.add_patch(car)
bike.set_color('yellow')
warning = plt.text(-15, 15, ' ')
warning.set_fontsize('x-large')
#####################################


#####################################
# Cardinal Direction
x_coords = [0, 1]
y_coords = [0, 1]

dx = x_coords[1] - x_coords[0]
dy = y_coords[1] - y_coords[0]

if (dx != 0):
    theta = (math.atan2(dy,dx))*180/3.1415926535897932384626
else:
	theta = 90
#####################################

print(theta)

def init():
    ax.add_patch(bike)
    return bike, warning

def animate(i):
    line = fp.readline()
    if (len(line) > 0):

	    coordinates_str = line.split(", ")
	    coordinates[0] = float(coordinates_str[0])
	    coordinates[1] = float(coordinates_str[1])
	    coordinates[2] = float(coordinates_str[2])
	    coordinates[3] = float(coordinates_str[3])

        
	    x_coords[0] = x_coords[1]
	    y_coords[0] = y_coords[1]
	    x_coords[1] = coordinates[1]
	    y_coords[1] = coordinates[0]

	    dx = 100000*(x_coords[1] - x_coords[0])
	    dy = 100000*(y_coords[1] - y_coords[0])

	    if (dx != 0):
	        theta = (math.atan2(dy,dx))
	    elif (dy > 0):
	        theta = 3.1415926535897932384626/2
	    elif (dy < 0):
	    	theta = -3.1415926535897932384626/2
	    else:
	    	theta = 0




	    x = 364629.27676 * (coordinates[3] - coordinates[1])
	    y = 364629.27676 * (coordinates[2] - coordinates[0])
	    dist = ((x**2)+(y**2))**0.5
	    bike_theta = -math.atan2(y,x) + theta

	    print((theta*180/3.14159))


	    xf = dist * math.sin(bike_theta)
	    yf = dist * math.cos(bike_theta)


	    if (dist < 15):
	        bike.set_color('red')
	        warning.set_color('red')
	    else:
	        bike.set_color('yellow')
	        warning.set_color('yellow')

	    bike.xy = (xf, yf)
	    warning_text = "     Warning: \n " + str(round(dist)) + " feet away"
	    warning.set_text(warning_text)
	    if (x > 0):
	        warning.set_position([(x+2),(y+1)])
	    else:
	    	warning.set_position([(x-2),(y+1)])
	    #print(round(dist))
    else:
	    bike.xy = (200, 200)
	    warning.set_text(' ')
    return bike, warning

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=36, interval=1000, blit=True)

plt.show()