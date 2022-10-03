import socket
import sys

# if the user inputs a port, use it
if len(sys.argv) >= 2:
	port = int(sys.argv[1])
else:
	port = 28333     # if not, use this one

s = socket.socket()

# bind to the port & listen
s.bind(('', port))
s.listen()

# create connection
while True:
	new_connection = s.accept()
	new_sock = new_connection[0]

	# as long as we don't hit the double end of line, keep waiting to recv data
	while True:
		if "\r\n\r\n" in new_sock.recv(4096).decode():
			break

	# sending and closing response and request
	get = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n"
	new_sock.sendall(get.encode())
	new_sock.close()