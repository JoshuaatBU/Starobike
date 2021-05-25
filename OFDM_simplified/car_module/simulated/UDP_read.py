#UDP receive that reads from receiver(car). writes out the bike gps data.
import socket
import os

UDP_IP = "127.0.0.1"
UDP_PORT = 7007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(37)
	SDR_sink_file = open("gps_data.txt", "w")
	data = data.decode('utf-8')
	SDR_sink_file.truncate()
	SDR_sink_file.write(data)
	SDR_sink_file.close()
