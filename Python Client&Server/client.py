#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 15:54:03 2020

@author: Jonathan
This file generates multiple parallel clients
"""
import sys
import socket
import random
import time
from multiprocessing import Process

minDist = 5               #under min Distance is the "danger zone"
numDistances = 50         #number of distances we send to server

def initialize(s, ID):
    command = 'INIT' + ID
    s.sendall(command.encode('utf-8'))

def generate_distances(n):
    distances = []
    dist = random.randint(5, 15)
    distances.append(dist)
    for i in range(1, 40):
        dist = dist - 1
        distances.append(dist)
        if(dist < 2):
            break

    length = len(distances)
    for j in range(length, 100):
        dist = dist + 1
        distances.append(dist)
    return distances


#connect to remote server
def connect_server():
    HOST = '155.41.8.29'
    #HOST = 'DESKTOP-PSL89SL'
    # define server address
    PORT = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((HOST, PORT))
    return s


def client_run(ID):
    print("Client " + ID + "started")
    distances = generate_distances(numDistances)
    s = connect_server()
    #initialize(s, ID)
    for i in range(0, numDistances-1):
        print("sending distances")
        command = 'DIST' + ID + str(distances[i])
        s.sendall(command.encode('utf-8')) #encode output to bytes.
        #reply = s.recv(1024).decode('utf-8') #decode input (likely bytes)
        #if reply == 'Terminate':
        #    break
        #elif reply[5] == str(1):
        #    print("WARNING, CRASH POSSIBLE")
        #else:
        #    print(reply)

        #print(reply)
        time.sleep(1)
    s.close()

def main():
    ID1 = 'aa'
    ID2 = 'bb'
    Process(target=client_run, args=(ID1,)).start()
    time.sleep(3)
    Process(target=client_run, args=(ID2,)).start()
    #time.sleep(3)
    #Process(target=client_run, args=(,)).start()
    #p2 = Process(target=client_run, args=('bb', ))
    #p2.start()

if __name__ == '__main__':
    main()