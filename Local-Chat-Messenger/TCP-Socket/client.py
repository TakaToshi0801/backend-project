import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/home/test/mydir/recursion/Local-Chat-Messenger/TCP-Socket/socket_file'
print('connectinng to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = sys.argv[1].encode('utf-8')
    sock.sendall(message)

    sock.settimeout(2)
    try:
        while True:
            data = str(sock.recv(32))
            if data:
                print('Server response: ' + data)
            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()