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

import serial
import numpy
from gnuradio import gr

class SerialSource_b(gr.sync_block):
    """
    docstring for block SerialSource_b
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="SerialSource_b",
            in_sig=None,
            out_sig=[numpy.bytes, ])


    def work(self, input_items, output_items):
        arduino_port = "/dev/ttyACM0" #serial port of Arduino
        baud = 9600 #arduino uno runs at 9600 baud
        ser = serial.Serial(arduino_port, baud)
        samples = 1000 #how many samples to collect
        print_labels = False
        line = 0 #start at 0 because our header is 0 (not real data)
        
        out = output_items[0]
        # <+signal processing here+>
        getData = ser.readLine()
        out[:] = getData[2:][:-5]
        return len(output_items[0])

