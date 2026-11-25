import socket

addr = ("example.com", 443)
connection_one = socket.create_connection(addr, timeout=3)
print ("UP")
connection_one.close()