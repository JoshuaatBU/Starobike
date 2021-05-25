#UDP send that gives data to transmitter
import socket
import time
import io

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

while(1):
	bs_file = open("gps_data.txt", "r")
	loc = bs_file.read()
	loc_encoded = loc.encode('utf-8')
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(loc_encoded, (UDP_IP, UDP_PORT))
	bs_file.close()
	time.sleep(0.001)
