import serial

def get_arduino_serial():
	arduino_port = "/dev/ttyACM0" #serial port of Arduino
	baud = 9600 #arduino uno runs at 9600 baud
	fileName="/data/gps_data.txt" #name of the CSV file generated


	try:
		ser = serial.Serial(arduino_port, baud)
	except:
		print("I don't think the arduino is connected! Serial Read Failed.")
		return -1;
	print("Connected to Arduino port:" + arduino_port)
	file = open(fileName, "a")
	print("Created file")


	samples = 1000 #how many samples to collect
	print_labels = False
	line = 0 #start at 0 because our header is 0 (not real data)
	while True:
	    if print_labels:
	        if line == 0:
	            print("Printing Column Headers")
	        else:
	            print("Line " + str(line) + ": writing...")


	    getData=str(ser.readline())
	    data=getData[2:][:-5]
	    print(data)
	    if(len(data) > 15):
	        file = open(fileName, "w")
	        file.write(data + "\n") #write data with a newline
	        line = line+1
	print("Data collection complete!")
	file.close()
