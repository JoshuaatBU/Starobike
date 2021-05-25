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
from gnuradio import qtgui
from gnuradio import blocks
class distanceSinkSD(gr.sync_block):
    """
    docstring for block distanceSinkSD
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="distanceSinkSD",
            in_sig=[numpy.float32, ],
            out_sig=None)


    def work(self, input_items, output_items):
        in0 = round(input_items[0])
        veclen = in0
        x_max = in0
        # <+signal processing here+>
        src = blocks.vector_source_f(range(in0), True, in0, [])
        throt = blocks.throttle(gr.sizeof_float*in0, 32000, True)
        dst = qtgui.vector_sink_f(
            veclen,
            0,
            1.0/x_max,
            "x-Axis",
            "y-Axis",
            "A noisy line",
            1 # Number of inputs
        )
        dst.set_update_time(0.10)
        dst.set_y_axis(0, 512)
        dst.enable_autoscale(False)
        dst.enable_grid(True)
        dst.set_x_axis_units("")
        dst.set_y_axis_units("")
        dst.set_ref_level(0)
        self.connect((throt,0), (dst,0))
        self.connect((src,0),(throt,0))
        return len(input_items[0])

