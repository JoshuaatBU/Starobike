#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 Starobike.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
from gnuradio import gr
import math
from matplotlib import pyplot as plt
from matplotlib import animation
import serial
import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pmt

#####################################
# File
#filepath = 'fake_GPS_data.txt'
#fp = open(filepath)
#line = fp.readline()
#coordinates = [0.0, 0.0, 0.0, 0.0]
#####################################

##################################### NEED AXES? I THINK DONE
# Figure
#fig = plt.figure()
#fig.set_dpi(100)
#fig.set_size_inches(7, 6.5)
#ax = plt.axes(xlim=(-20,20), ylim=(-20, 20))
#ax.set_facecolor((0, 0, 0))
#####################################

##################################### COULD BE DONE
# Patches
#bike = plt.Rectangle((-1, -1), 1, 1)
#car = plt.Rectangle((-1.5, -4), 3, 8)
#ax.add_patch(car)
#ax.add_patch(bike)
#bike.set_color('yellow')
#warning = plt.text(-15, 15, ' ')
#warning.set_fontsize('x-large')
#####################################

#####################################
# Cardinal Direction
x_coords = [0, 0]
y_coords = [0, 1]
theta = [0, 0]

dx = x_coords[1] - x_coords[0]
dy = y_coords[1] - y_coords[0]

if (dx != 0):
    theta[1] = (math.atan2(dy,dx))*180/3.1415926535897932384626
else:
	theta[1] = 90

#####################################
#
#def init():
#    ax.add_patch(bike)
#    return bike, warning

#def animate(i, line):
#    if (len(line) > 0):       
#        coordinates[0] = float(line[0])
#        coordinates[1] = float(line[1])
#        coordinates[2] = float(line[2])
#        coordinates[3] = float(line[3])
#        x_coords[0] = x_coords[1]
#        y_coords[0] = y_coords[1]
#        x_coords[1] = coordinates[1]
#        y_coords[1] = coordinates[0]
#
#
#        print(y_coords)
#
#        dx = 100000*(x_coords[1] - x_coords[0])
#        dy = 100000*(y_coords[1] - y_coords[0])
#
#        if ((dx == 0) and (dy == 0)):
#        	theta[1] = theta[0]
#        elif (dx != 0):
#            theta[1] = (math.atan2(dy,dx))
#        elif (dy > 0):
#            theta[1] = 3.1415926535897932384626/2
#        elif (dy < 0):
#        	theta[1] = -3.1415926535897932384626/2
#        else:
#        	theta[1] = 0
#
#        theta[0] = theta[1]
#
#
#
#
#        x = 364629.27676 * (coordinates[3] - coordinates[1])
#        y = 364629.27676 * (coordinates[2] - coordinates[0])
#        dist = ((x**2)+(y**2))**0.5
#        bike_theta = -math.atan2(y,x) + theta[1]
#
#        #print((theta*180/3.14159))
#
#
#        xf = dist * math.sin(bike_theta)
#        yf = dist * math.cos(bike_theta)
#
#
#        if (dist < 15):
#            bike.set_color('red')
#            warning.set_color('red')
#        else:
#            bike.set_color('yellow')
#            warning.set_color('yellow')
#
#        bike.xy = (xf, yf)
#        warning_text = "     Warning: \n " + str(round(dist)) + " feet away"
#        warning.set_text(warning_text)
#        if (xf > 0):
#            warning.set_position([(xf+2),(yf+2)])
#        else:
#        	warning.set_position([(xf-10),(yf+2)])
#            #print(round(dist))
#    else:
#        bike.xy = (200, 200)
#        warning.set_text(' ')
    #return bike, warning



class willSink(gr.sync_block, FigureCanvas):
    """
    docstring for block willSink
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="willSink",
            in_sig=[numpy.byte, ],
            out_sig=None)
        self.fig = Figure(figsize = (7, 6.5), dpi  =100)
        #self.fig.patch.set_facecolor(self.
        self.axes = self.fig.add_subplot(111)
        self.axes.set(xlim = (-20,20), ylim=(-20,20))
        self.axes.set_facecolor((0,0,0))
        #ax = plt.axes(xlim=(-20,20), ylim=(-20, 20))
        #ax.set_facecolor((0, 0, 0))
        # Patches
        bike = plt.Rectangle((-1, -1), 1, 1)
        car = plt.Rectangle((-1.5, -4), 3, 8)
        self.axes.add_patch(car)
        self.axes.add_patch(bike)
        bike.set_color('yellow')
        warning = plt.text(-15, 15, ' ')
        warning.set_fontsize('x-large')
        FigureCanvas.__init__(self, self.fig)
        #self.setParent(Parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def work(self, input_items, output_items):
        print("begin")        
        in0 = input_items[0][:]
        #in2 = in0[:].tostring()
        in2 = in0[:].tostring()
        coord = (in2).decode('utf8').split(", ")
#        arduino_port = "/dev/ttyACM0" #serial port of Arduino
#        baud = 9600 #arduino uno runs at 9600 baud
#        ser = serial.Serial(arduino_port, baud)
#        getData = (ser.readline())
        #print(coord)
        line = []
        line.append("42.00000000")
        line.append("-71.00000000")
        #line.append(coord[1])
        #line.append(coord[2])
        line.append("42.0000000")
        line.append("-71.00002000")
        print(line)
        #print(in2)
        print("test")
        #print(in0[:])
        #print(in0.decode('UTF-8'))
        #print(str(in0)[2:][:-2])
        if (len(line) > 0):
            coordinates = []       
            coordinates.append(float(line[0]))
            coordinates.append(float(line[1]))
            coordinates.append(float(line[2]))
            coordinates.append(float(line[3]))
            x_coords[0] = x_coords[1]
            y_coords[0] = y_coords[1]
            x_coords[1] = coordinates[1]
            y_coords[1] = coordinates[0]


            #print(y_coords)

            dx = 100000*(x_coords[1] - x_coords[0])
            dy = 100000*(y_coords[1] - y_coords[0])

            if ((dx == 0) and (dy == 0)):
            	theta[1] = theta[0]
            elif (dx != 0):
                theta[1] = (math.atan2(dy,dx))
            elif (dy > 0):
                theta[1] = 3.1415926535897932384626/2
            elif (dy < 0):
            	theta[1] = -3.1415926535897932384626/2
            else:
            	theta[1] = 0

            theta[0] = theta[1]




            x = 364629.27676 * (coordinates[3] - coordinates[1])
            y = 364629.27676 * (coordinates[2] - coordinates[0])
            dist = ((x**2)+(y**2))**0.5
            bike_theta = -math.atan2(y,x) + theta[1]

            #print((theta*180/3.14159))


            xf = dist * math.sin(bike_theta)
            yf = dist * math.cos(bike_theta)

            bike = plt.Rectangle((-1, -1), 1, 1)
            car = plt.Rectangle((-1.5, -4), 3, 8)
            warning = plt.text(-15, 15, ' ')
            self.axes.add_patch(car)
            self.axes.add_patch(bike)
            if (dist < 15):
                bike.set_color('red')
                warning.set_color('red')
            else:
                bike.set_color('yellow')
                warning.set_color('yellow')

            bike.xy = (xf, yf)
            warning_text = "     Warning: \n " + str(round(dist)) + " feet away"
            warning.set_text(warning_text)
            if (xf > 0):
                warning.set_position([(xf+2),(yf+2)])
            else:
            	warning.set_position([(xf-10),(yf+2)])
                #print(round(dist))
        else:
            bike.xy = (200, 200)
            warning.set_text(' ')
        self.draw()

        return len(input_items)
#anim = animation.FuncAnimation(fig, animate, fargs = (line,), init_func=init, frames=36, interval=100, blit=True)

#plt.show()

