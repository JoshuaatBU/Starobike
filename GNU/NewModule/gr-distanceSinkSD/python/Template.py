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


from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

class Template(gr.hier_block2, Qt.QWidget):
    """
    docstring for block Template
    """
    def __init__(self):
        gr.hier_block2.__init__(self,
            "Template",
            gr.io_signature(1, 1, gr.sizeof_float*1),  # Input signature
            gr.io_signature(0, 0, 0)) # Output signature
        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        #self.setLayout(self.top_layout)
            # Define blocks and connect them
        veclen = (self,0)[:]
        print(veclen)
        x_len = (self,1)[0][:]
        print(x_len)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            veclen,
            0,
            1.0/x_len[:],
            "x-Axis",
            "y-Axis",
            "A noisy line",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0, 512)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [10, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        #self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.blocks_vector_source_x_0 = blocks.vector_source_f(range(veclen), True, veclen, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*veclen, samp_rate,True)
        

        self.connect((self.blocks_stream_to_vector_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self, 0), (self.blocks_stream_to_vector_0, 0))
