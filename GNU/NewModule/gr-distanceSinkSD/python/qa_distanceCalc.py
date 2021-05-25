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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from distanceCalc import distanceCalc
from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import pmt
class qa_distanceCalc(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
        # set up fg
        text = [[]]
        file_source = blocks.file_source(gr.sizeof_char*1, '/home/josh/Documents/SD/21-29-Starobike/GNU/received.txt', False, 0, 0)
        file_source.set_begin_tag(pmt.PMT_NIL)
        file_source2 = blocks.file_source(gr.sizeof_char*1, '/home/josh/Documents/SD/21-29-Starobike/GNU/received2.txt', False, 0, 0)
        file_source2.set_begin_tag(pmt.PMT_NIL)
        #proc = distanceCalc.work(self,(file_source,0),out)
        proc = distanceCalc()
        blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 32000,True)
        blocks_float_to_complex_0 = blocks.float_to_complex(1)
        dst = blocks.vector_sink_c()
 #       self.tb.connect(src,throt)
        #self.tb.connect(src,dst)
#        self.tb.connect(throt,dst)
        self.tb.connect(file_source,(proc,0))
        self.tb.connect(file_source2,(proc,1))
        self.tb.connect((proc,0),(blocks_float_to_complex_0,0))
        self.tb.connect((proc,1),(blocks_float_to_complex_0,1))
        self.tb.connect(blocks_float_to_complex_0,blocks_throttle_0)
        self.tb.connect(blocks_throttle_0,dst)
        self.tb.run()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_distanceCalc)
