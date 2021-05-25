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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from serialsource_b import serialsource_b
class qa_serialsource_b(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
        string = "Python is interesting."
        arr = bytes(string, 'utf-8')
        out = []
        src = serialsource_b().work(None,out)
        veclen = 512
        out2 = [[]]
        #t = blocks.vector_source_f(range(veclen), True, veclen, [])
        
        #print(out)
        #dst = blocks.vector_sink_b ()
        #print(arr)
        #print('ok')
        #print(src)
        #print(out)
        #print(out[0][:])
        #t2 = bytes(out[:])
        #print(t2)
        #print(type(t2))
        #print("".join((t2)))
        #finalOut = "".join((t2))
        #print(type(finalOut))
        #self.tb.connect((src,0),(dst,0))
        self.tb.run()
        #result = dst.data()
        #print(result)
        self.assertAlmostEqual(5,5)
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_serialsource_b)
