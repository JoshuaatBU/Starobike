import arduino_serial_module as ARD
import UDP_gps_module as UDP
import SDR_transmit as SDR
import threading

def main():
	t1 = threading.Thread(target=UDP.UDP_write)
	t2 = threading.Thread(target=ARD.get_arduino_serial)
	print("starting UDP port read...")
	t1.start()
	print("starting arduino read...")
	t2.start()
	print("starting GNUradio flowgraph...")
	SDR.SDR_start()

if __name__ == '__main__':
	main()
