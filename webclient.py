import socket
import sys

if len(sys.argv) >= 3:
	host = sys.argv[1]
	port = int(sys.argv[2])
else:
	host = "www.example.com"
	port = 80

s = socket.socket()
s.connect((host, port))

get = "GET / HTTP/1.1 200 OK\r\nHost: {}\r\nConnection: close\r\n\r\n".format(host)
s.sendall(get.encode("ISO-8859-1"))

while True:
	resp = s.recv(4096)
	if not resp: break
	print(resp)
	print(resp.decode("ISO-8859-1"))

s.close()