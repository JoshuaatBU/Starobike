#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:54:03 2020

@author: Jonathan
This file generates multiple parallel clients
"""
import sys
import socket
import random
import time

print(time.time_ns())
print(time.time_ns())
print(time.time_ns())
print(time.time_ns())
print(time.time_ns())
l = time.time_ns()
for ii in range(20):
    print(l - time.time_ns())
