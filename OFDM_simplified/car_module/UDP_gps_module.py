#UDP send that gives data to transmitter
import socket
import time
import io


def UDP_write():
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005

	while(1):
		bs_file = open("/data/gps_data.txt", "r")
		loc = bs_file.read()
		loc_encoded = loc.encode('utf-8')
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(loc_encoded, (UDP_IP, UDP_PORT))
		bs_file.close()
		time.sleep(0.0005)
		
def UDP_read():	
	UDP_IP = "127.0.0.1"
	UDP_PORT = 7007

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	sock.bind((UDP_IP, UDP_PORT))

	while True:
		data, addr = sock.recvfrom(37)
		SDR_sink_file = open("/data/bike_gps_data.txt", "w")
		data = data.decode('utf-8')
		SDR_sink_file.truncate()
		SDR_sink_file.write(data)
		SDR_sink_file.close()
