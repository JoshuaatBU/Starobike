# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
This server file handles up to 5 parallel client connections
"""

import socket
import struct
from multiprocessing import Process
import time

"""
def add(conn, data):
	sum = 0

	while 1:
		conn.send(b"please enter next number to add.")
		data = conn.recv(1024)
		data = data.decode("utf-8")
		if(data == 'done'):
			break
		num = int(data)
		sum = sum + num

	return sum
"""

def dist(conn,data):
    #try:
    #print(data[6:len(data)+1])
    distance = float(data[6:len(data)+1])
    #print(distance)
    if distance<=5.0:
        flag = 1
    elif distance>=25.0:
        flag = -1
    else:
        flag = 0
    reply = data[0:4] + str(flag)
    conn.send(reply.encode('utf-8'))
    return flag
    #except:
        #print('data not a number')
        #conn.send(b"Measurement invalid")
    
def on_connect (conn,add):
    print('started connection')
    while True:
        data = conn.recv(1024)
        data = data.decode("utf-8")
        reply = ''
        print(data)
    	#and so on and on until...
        if data[0:4] == 'QUIT':
                conn.send(b'Terminate')
                break
        elif data[0:4] == 'DIST':
            distflag = dist(conn, data)
            if distflag == 1:
                print(data[4:6] + ' Is within accident distance')
            elif distflag == -1:
                break
        else:
            reply = 'I do not understand ' + data
        
        reply1 = reply.encode('utf-8')
    	# Sending reply
        conn.send(reply1)
	#conn.close() # Close connections
    
def main():    
        
    #HOST needs to be whatever your IP is
    HOST = '155.41.8.29'
    PORT = 12345 # Pick an open Port (1000+ recommended), must match the client sport
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')
    print(socket.gethostname())
    #managing error exception
    try:
    	s.bind((socket.gethostname(), PORT))
    except socket.error:
    	print('Bind failed ')
        
    s.listen(5)
    while True:
        print('Socket awaiting messages')
        (conn, addr) = s.accept()
        print('Connected from ' + addr[0] + ":" + str(addr[1]))
        Process(target=on_connect, args=(conn,addr,)).start()
    s.close()
    # awaiting for message

if __name__ == '__main__':
    main()
    

