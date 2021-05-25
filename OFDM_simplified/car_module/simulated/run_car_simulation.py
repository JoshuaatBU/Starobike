import UDP_gps_module as UDP
import OFDM_FEC_Rx as SDR
import jh_display as DISP

import threading

def main():
	t1 = threading.Thread(target=UDP.UDP_read)
	t3 = threading.Thread(target=SDR.main)
	print("starting UDP port write...")
	t1.start()
	print("starting GNUradio flowgraph...")
	t3.start()


if __name__ == '__main__':
	main()

