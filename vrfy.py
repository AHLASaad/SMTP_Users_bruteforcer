#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
	print "Usage: vrfy.py <MailServer>"
	sys.exit((0))
	
# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect= s.connect((str(sys.argv[1]),25))

# Receive the banner
banner= s.recv(1024)
print banner
# Get users from a wordlist
Users = open('users.txt', 'r')
User = Users.readlines()
# VRFY a user
s.send('VRFY ' + User + '\r\n')
result= s.recv(1024)
print result

# Close the socket and file
Users.close()
s.close()
