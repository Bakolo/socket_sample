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
skt.connect((HOST, PORT))

while True:
    cmd = input("say something(<1024): ")
    skt.send(cmd.encode())
    data = skt.recv(1024)
    print(data)

