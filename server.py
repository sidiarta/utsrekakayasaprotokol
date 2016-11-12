# utsrekakayasaprotokol
Kelompok 5,6 : Perintah yang dikirim client adalah “cpu” dengan balikan server adalah cpu usage pada server saat itu

import socket
import psutil
s= socket.socket()
host = ""
port=12345
s.bind((host,port))
s.listen(5)
cpu_use = psutil.cpu_times()
print "Menunggu Koneksi..."
while True:
	c, addr= s.accept()
	perintah = str(c.recv(1024))
	print ('diperintahkan untuk') ,perintah
	print ('oleh') , addr

	if perintah == 'cpu':
		message_str = 'user :' + str(cpu_use.user) \
		+ '\nSystem :' + str(cpu_use.system) \
		+ '\nIdle :' + str(cpu_use.idle) \
		+ '\nInterrupt :' + str(cpu_use.interrupt) \
		+ '\nDpc :' + str(cpu_use.dpc) 
		c.send(message_str)
	
	
c.close()
