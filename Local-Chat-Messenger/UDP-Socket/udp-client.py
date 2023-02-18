import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/home/test/mydir/recursion/Local-Chat-Messenger/UDP-Socket/udp_socket_file'
address = '/home/test/mydir/recursion/Local-Chat-Messenger/UDP-Socket/udp_client_socket_file'
message = sys.argv[1].encode('utf-8')

sock.bind(address)

try:
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    print('waiting to receive...')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()