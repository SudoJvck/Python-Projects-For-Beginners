# follow me @SudoJvck
# First, import all libraries.
# use pip install if libraries unavailable on system
import pyfiglet
import sys
import socket
from datetime import datetime

#create & print custom banner (optional)
ascii_banner = pyfiglet.figlet_format("JvckScan")
print(ascii_banner)

#create target variable to store input for target IP
#make a string for easier formatting
target = input(str("Input Target IP: "))

#create information banner
#include time stamp
print("_" * 50)
print(f"Scanning Target: ({target})")
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

#scan every port on target ip
#ip address range 1 - 65535

try:
    for port in range (1,65535):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(0.5)
      
    
    #return open ports
      result = s.connect_ex((target,port))
      if result == 0:
        print("[*] Port {} is open".format(port))
        s.close()
    
    #Catch keyboard interrupts
except KeyboardInterrupt:
        print("\n Exiting JvckScan :(")
        sys.exit()
    
    #catch socket errors
except socket.error:
        print ("\ Host not responding :(")
        sys.exit()
      
