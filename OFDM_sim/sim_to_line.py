#takes as argument, the simulated gps file
import os
import time
import io
import sys

def main():
	sim_file = open(sys.argv[1], "r")
	sim_lines = sim_file.readlines()
	for line in sim_lines:
		gps_file = open("gps_data.txt", "w")
		gps_file.write(line)
		gps_file.close()
		time.sleep(3)


if __name__ == "__main__":
    main()
