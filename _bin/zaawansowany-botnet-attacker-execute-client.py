import socket
import json
import logging
from pprint import pprint


HOST = "localhost"
PORT = 1337
XML_CMD_FILE = '../../../_tmp/botnet-commands.xml'


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname)s (%(name)s) %(message)s')
log = logging.getLogger('botnet.atacker.client')


with open(XML_CMD_FILE) as file:
    commands = file.read()


log.debug('Create a socket (SOCK_STREAM means a TCP socket)')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

    log.debug('Connect to server and send data')
    addr = (HOST, PORT)
    sock.connect(addr)
    sock.sendall(bytes(commands + "\n", "utf-8"))

    log.debug('Receive data from the server and shut down')
    received = str(sock.recv(1024), "utf-8")
    output = json.loads(received)


print("Sent:     {}".format(commands))
print("Received: {}".format(output))
print('\n\n')

for executed in output:
    pprint(executed)
