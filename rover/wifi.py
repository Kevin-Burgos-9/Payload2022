import socket

UDP_IP = "192.168.0.100" # IP address of the ESP-01s module
UDP_PORT = 12345

def send_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
    sock.close()

def receive_message():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", UDP_PORT))
    data, address = sock.recvfrom(1024)
    sock.close()
    return data.decode(), address

# Example usage:
send_message("Hello ESP-01s!")
data, address = receive_message()
print("Received message:", data, "from", address)
