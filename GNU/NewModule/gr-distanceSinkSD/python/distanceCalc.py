#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2021 gr-distanceSinkSD author.
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
class distanceCalc(gr.sync_block):
    """
    docstring for block distanceCalc
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="distanceCalc",
            in_sig=[numpy.byte, numpy.byte, ],
            out_sig=[numpy.float32,numpy.float32, ])


    def work(self, input_items, output_items):
        out = output_items
        in0 = "".join([chr(item) for item in input_items[0]])
        in1 = "".join([chr(item) for item in input_items[1]])

        # <+signal processing here+>
        print(in0)
        try:        
            coordinates_str = str(in0)
            coordinates_str_strip = coordinates_str.strip(" ").split(",")
            coordinates_str2 = str(in1)
            coordinates_str2_strip = coordinates_str2.strip(" ").split(",")
            coordinates = []
            coordinates.append(float(coordinates_str_strip[1]))
            print(coordinates_str_strip[2])
            coordinates.append(float(coordinates_str_strip[2]))
            coordinates.append(float(coordinates_str2_strip[1]) - 0.000001)
            coordinates.append(float(coordinates_str2_strip[2]) - 0.000001)
            x = 364629.27676 * (coordinates[3] - coordinates[1])
            y = 364629.27676 * (coordinates[2] - coordinates[0])
            out[0] = x
            out[1] = y
            early_state_x = x
            early_state_y = y
        except:
            out[0] = 0
            out[1] = 0

        return len(output_items)

