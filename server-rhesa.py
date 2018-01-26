import socket
import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def checkNumber(karakter):
    try:
        val = int(karakter)
        return val
    except ValueError:
        return "FALSE"

def checkOperation(operation, str1, str2):
    try:
        val1 = int(str1)
        val2 = int(str2)
    except ValueError:
        return "anda tidak masukan angka"
    
    if(operation == "+"):
        return int(val1 + val2)
    elif(operation == "-"):
        return int(val1 - val2)
    elif(operation == "*"):
        return int(val1 * val2)
    elif(operation == ":"):
        return float(val1 / val2)
    else:
        return "Maaf bilangan operation yang anda masukan tidak kami ketahui"

def handle_client(sock_client, addr):
    logging.debug('client connection accepted: {}'.format(addr))
    message = ''
    while message.find('bye') == -1:
        message = sock_client.recv(1024)
        check = message.split(' ')
        val1 = check[0]
        val2 = check[2]
        op = check[1]
        hasil = checkOperation(op, val1, val2)
        hasil = 'saya menjawab : {}'.format(hasil)
        sock_client.send(str(hasil))
    sock_client.close()

sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_server.bind(('127.0.0.1',9999))
sock_server.listen(5)
clients = []
while True:
    try:
        s, a = sock_server.accept()
        t_client = threading.Thread(target=handle_client, args=(s,a))
        t_client.start()
        t_client.join(1)
        clients.append(t_client)
    except Exception as e:
        logging.debug(e)
        break
    except KeyboardInterrupt as k:
        break
