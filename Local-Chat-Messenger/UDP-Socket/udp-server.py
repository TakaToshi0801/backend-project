import socket
import os
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/home/test/mydir/recursion/Local-Chat-Messenger/UDP-Socket/udp_socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message...')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        fake = Faker()
        sent = sock.sendto(fake.name().encode('utf-8'), address)
        print('sent {} bytes back to {}'.format(sent, address))