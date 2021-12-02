import socket
import arg_parse

argv = arg_parse.to_dict()

if '-H' in argv:
    HOST = argv["-H"]
else:
    HOST = input("please input the HOST IP address: ")

if '-P' in argv:
    PORT = argv["-P"]
else:
    PORT = input("please input the PORT(int): ")

#HOST = "172.21.202.160"
#PORT = 8001

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
skt.bind((HOST, PORT))
skt.listen(5)

print(f'Socket Server HOST: {HOST}')
print(f'Socket Server PORT: {PORT}')
print("Wait for client to connect...")

while True:
	conn, addr = skt.accept()
	print(f"connected by {addr}")
	
	while True:
		data = conn.recv(1024)
        print(f"received: {data}")
        conn.send("Server received: '{data}' ".encode())
