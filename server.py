import socket

sock = socket.socket()
sock.bind(('10.111.9.4', 7070))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

# while True:
data = conn.recv(1024)
# if not data:
#     break
print(data)
    # conn.send(data.upper())

conn.close()
