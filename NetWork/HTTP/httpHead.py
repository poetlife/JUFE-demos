import socket

# this file was aimed to test the HEAD method of HTTP

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = (socket.gethostbyname("www.baidu.com"), 80)

client.connect(addr)

client.send(b"GET /index HTTP/1.1\r\n")

response = client.recv(1024)

print(response)

client.close()