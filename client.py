#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('10.111.10.3', 7070))
# while True:
sock.send('hello, world!')
# sock.sendto("feewwe", ('10.111.10.3', 7070))
# data = sock.recv(1024)
sock.close()

# print(data)
