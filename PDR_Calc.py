import sys
import os
import time
import random
import zlib
import struct

import argparse

#finding total number of false messages
false_file = open("C:\\Users\\fillin\\fillin\\PDRatio_False.txt", "r")
false_line = false_file.read()
false_line.split(",")
total_false = sum([int(num) for num in false_line.split(',')])

#finding total number of messages
all_file = open("C:\\Users\\fillin\\fillin\\PDRatio_All.txt", "r")
all_line = all_file.read()
all_line.split(",")
total_all = sum([int(num) for num in all_line.split(',')])

#Calculating PDR
total_true=total_all - total_false

PDR= total_true / total_all
print("The Packet Delivery Ratio is: ")
print(PDR)

#clearing the files for the next run
clear_file1 = open("PDRatio_False.txt","r+")
clear_file1.truncate(0)
clear_file1.close()

clear_file2 = open("PDRatio_All.txt","r+")
clear_file2.truncate(0)
clear_file2.close()
