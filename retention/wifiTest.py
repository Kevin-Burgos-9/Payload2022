import socket


IP_ADDRESS = '192.168.4.1' 
PORT = 80  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDRESS, PORT))


data = '^_^Arrived^_^'

sock.sendall(data.encode())
	

sock.close()
