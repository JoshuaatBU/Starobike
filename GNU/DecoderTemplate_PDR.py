import sys
import os
import time
import random
import zlib
import struct

import argparse

parser = argparse.ArgumentParser(description='Decode the messages for EC415 Lab6.')
parser.add_argument('filepath',
                    help='File path to decode.')
# parser.add_argument('grc_file', help='GRC file path that the program will compile and run.')
args = parser.parse_args()
filepath = args.filepath


# Given a filepath, returns the binary content of the file
def get_binary_file_data(filepath):
	try:
		f = open(args.filepath, 'rb')
		bits = f.read()
		f.close()
	except IOError as e:
	    print("Couldn't open or read file (%s)." % e)

	# convert bytes into bits
	bin_str = ''.join(format(ord(x), 'b').zfill(8) for x in bits)
	return bin_str

def bytes_to_hex(byte_str):
	hex_str = ""
	for c in byte_str:
		hex_str += hex(ord(c))[2:] + " "
	return hex_str

# Given a binary string, a start index, and number of bytes to read, returns a set of bytes/chars.
def get_bytes(bin_str, start, num_bytes, pdr):
	if not start+8*num_bytes <= len(bin_str):
		message = "Packet delivery Ratio: " + str(pdr*100) + "%"
		print(message)
		#print("Not enough bytes to consume.")
		exit(0)
	msg = ""
	for i in range(start, start+8*num_bytes, 8):
		msg += chr(int(bin_str[i:i+8], 2))
	return start+8*num_bytes, msg

# Searches a binary string for a preamble and returns the index where it is located
# Returns -1 if no preamble found
def search_for_preamble(bin_str, preamble, start):
	if not preamble or not isinstance(preamble, str):
		print("No valid preamble given. Enter the preamble as a string with the hex digits you want to search for.")
		exit(1)
	preamble = bin(int(preamble,16))[2:]
	idx = bin_str[start:].find(preamble)
	if idx == -1:
		
		return len(bin_str), False
	return idx+start, True

# Will decode a hex encoded string, but replaces any characters that were
# unable to be decoded with a '*' character.
def decode_hex(s):
    msg = ''
    for i in range(0, len(s), 2):
        try:
            msg += s[i:i+2].decode('hex')
        except:
            msg += '*'
    return msg


def check_crc(msg, crc):
    crc, = struct.unpack('>I', crc)
    calc_crc = zlib.crc32(msg.encode('hex')) & 0xFFFFFFFF
#    print("The CRC is: " + str(hex(calc_crc)))
    return crc == calc_crc


""" ******************************************************* """
"""			Your Implementation Goes Below This Line		"""
""" ******************************************************* """

"""
You have access to some useful variables and functions:
	filepath
		This variable contains the path of the file you entered as a command line argument

	get_binary_file_data(filepath)
		This function will take a filepath and return a binary string with all the information in that file.

	search_for_preamble(bin_str, preamble, start)
		This function will find a preamble within a binary string starting from the index "start". It returns 2
		items, the index of where a preamble was found and a boolean of whether a preamble was found. If no preamble
		is found, it returns the last index of the binary string.

	get_bytes(bin_str, start, num_bytes)
		This function will take a starting index, a number of bytes to process, and a binary string and return
		the index after consuming the bytes and a string containing the bytes (chars)

	bytes_to_hex(byte_str)
		This function takes a string of chars/bytes and will return a hex string of the ascii values of each char. For
		example, the ascii string "hello" would return "68 65 6c 6c 6f 0a".

	decode_hex(s)
		This function takes a hex encoded string and decodes it into ASCII. If a character has an
		error, it will be replaced by a '*' character.

    check_crc(msg, crc):
        This function will generate a CRC from the ASCII string 'msg' and return True if
        it is equal to the received CRC code.
"""

preamble='0xAABBCCDD'

bin_out=get_binary_file_data(filepath)	



index,boolean=search_for_preamble(bin_out,preamble, 0)

num_true = 0
num_total = 0
pdr = 0




while boolean == True:

	index,msg=get_bytes(bin_out,index,4,pdr)	

	msg=bytes_to_hex(msg)

	index,msg=get_bytes(bin_out,index,1,pdr)	

	msg=bytes_to_hex(msg)

	payload_length_decimal= int(msg, 16)

	index,msg=get_bytes(bin_out, index, payload_length_decimal, pdr)

	msg=decode_hex(msg)

	index,crc=get_bytes(bin_out,index,4,pdr)	

	crc=check_crc(msg, crc)

	print(msg + ": " + str(crc) )

	index,boolean=search_for_preamble(bin_out,preamble, index)

	if crc == True:
		num_true = num_true + 1
	num_total = num_total + 1
	pdr = float(num_true) / float(num_total)



	






