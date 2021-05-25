#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-seniordesign author.
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
import serial
class serialsource_b(gr.sync_block):
    """
    docstring for block serialsource_b
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="serialsource_b",
            in_sig=None,
            out_sig=[numpy.byte, ])


    def work(self, input_items, output_items):
        #string = "Python is interesting."
        arduino_port = "/dev/ttyACM0" #serial port of Arduino
        baud = 9600 #arduino uno runs at 9600 baud
        ser = serial.Serial(arduino_port, baud)
        # string with encoding 'utf-8'
        #arr = bytes(string, 'utf-8')
        getData = (ser.readline())
        #print(type(getData))
        #print(getData)
        #data = getData[2:][:-5]
        data = getData[:-5]
        #print(data)
        out = output_items
        # <+signal processing here+>
        #out.append(data)
        out[:] = bytes(data)
        #out[:] = bytes(data)
        #print(out)
        return len(output_items)

