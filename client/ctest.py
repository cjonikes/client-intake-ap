import socket

host = "192.168.56.1"
port = 8000

s = socket.socket()
s.connect((host, port))
