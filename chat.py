import socket
import threading

client = socket.socket()
client.connect(('10.111.10.3', 7070))

server = socket.socket()
server.bind(('10.111.9.4', 7070))
server.listen(1)
conn, addr = server.accept()

print('connected:', addr)
#
# def string_color(str, col=1):


def listen():
	while True:
		data = conn.recv(1024)
		if data:
			print("valerchik: ", data)


def writer():
	global client
	while True:
		msg = input()
		print(msg)
		if "exit" in msg.split():
			conn.close()
			server.close()
			client.close()
			exit()
		if msg:
			# print("SEND")
			# client.send(str.encode(msg))
			client.send(msg)


t1 = threading.Thread(target=writer)
t2 = threading.Thread(target=listen)

t1.start()
t2.start()

t1.join()
t2.join()

