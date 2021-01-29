import socket
import select
import errno
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234
my_token = input("token: ")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

# Set connection to non-blocking state, so .recv() call wont block
client_socket.setblocking(False)

# Prepare token and header and send them
token = my_token.encode('utf-8')
token_header = f"{len(token):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(token_header + token)

# Wait for user to input a message
message = input(f'{my_token} > ')
if message:
    message = message.encode('utf-8')
    message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
    client_socket.send(message_header + message)

while True:
    try:
        # received messages
        message = client_socket.recv(1024).decode('utf-8')
        print(f'{message}')

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()
