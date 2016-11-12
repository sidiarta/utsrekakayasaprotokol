# utsrekakayasaprotokol
Kelompok 5 : Perintah yang dikirim client adalah “cpu” dengan balikan server adalah cpu usage pada server saat itu

import socket

s=  socket.socket()
host =socket.gethostname()
port = 12345
s.connect((host,port))
s.send('cpu')
print s.recv(1024)
s.close()
