import socket

sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client.connect(('127.0.0.1', 9999))
	
while True:
    try:
        message = raw_input('ketik perhitungan yang anda inginkan dan gunakan spasi di setiap selesai ketik nomor atau pun perhitungan. contoh : (1 + 1) ')
        sock_client.send(message)
        print(sock_client.recv(1024))
    except Exception as e:
        break
    except KeyboardInterrupt as k:
        break
