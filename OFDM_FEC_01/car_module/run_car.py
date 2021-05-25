import arduino_serial_module as ARD
import UDP_gps_module as UDP
import SDR_receive as SDR
import jh_driver_display as DISP

import threading

def main():
	t1 = threading.Thread(target=UDP.UDP_read)
	t2 = threading.Thread(target=ARD.get_arduino_serial)
	t3 = threading.Thread(target=SDR.SDR_start)
	t4 = threading.Thread(target=DISP.run_display)
	print("starting UDP port write...")
	t1.start()
	print("starting arduino read...")
	t2.start()
	print("starting GNUradio flowgraph...")
	t3.start()


if __name__ == '__main__':
	main()

