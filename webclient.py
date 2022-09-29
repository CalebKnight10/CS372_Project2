import socket
import sys


# look for user input for a host and a port
if len(sys.argv) >= 3:
	host = sys.argv[1]
	port = int(sys.argv[2])
else:
	host = "www.example.com"   # if no UI, use this host
	port = 80                  # and this port

# connections
s = socket.socket()
s.connect((host, port))

get = "GET / HTTP/1.1 200 OK\r\nHost: {}\r\nConnection: close\r\n\r\n".format(host)
s.sendall(get.encode("ISO-8859-1"))

# as long as we are recv data, print and decode the response
while True:
	resp = s.recv(4096)
	if not resp: break
	print(resp)
	print(resp.decode("ISO-8859-1"))

s.close()