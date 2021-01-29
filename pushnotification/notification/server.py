import socket
import select
import time
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.authtoken.models import Token


HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234


notifs = {}

# List of sockets for select.select()
sockets_list = []

# List of connected clients - socket as a key, user header and token as data
clients = {}


def receive_message(client_socket):

    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):    # If we received no data, client gracefully closed a connection
            return False
        message_length = int(message_header.decode('utf-8').strip())
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        return False


def server(request):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((IP, PORT))
    server_socket.listen()

    global notifs, sockets_list, clients

    sockets_list =[server_socket]
    print(f'Listening for connections on {IP}:{PORT}...')

    while True:

        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

        # Iterate over notified sockets
        for notified_socket in read_sockets:
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                user = receive_message(client_socket)

                # If False - client disconnected before he sent token
                if user is False:
                    continue
                sockets_list.append(client_socket)
                clients[client_socket] = user

                print('Accepted new connection from {}:{}, token: {}'.format(*client_address, user['data'].decode('utf-8')))

            # Else existing socket is sending a message
            else:
                user = clients[notified_socket]
                t = user['data'].decode('utf-8')

                try:
                    token_obj = Token.objects.get(key=t)
                    notifications = Notification.objects.filter(receiver=token_obj.user)
                    notif_ser = NotificationSerializer(notifications, many=True)
                    notifs = notif_ser.data

                    if notifs:
                        message = notifs
                        # if message is False:
                        #     print('Closed connection from: {}'.format(clients[notified_socket]
                        #     ['data'].decode('utf-8')))
                        #     sockets_list.remove(notified_socket)
                        #     del clients[notified_socket]
                        #     continue
                        user = clients[notified_socket]
                        print(f'Notifications send to {t}: {message}')
                        hm = (str(message))
                        notified_socket.sendall(hm.encode())
                        notifications.delete()
                        notifs = {}
                        break
                    else:
                        time.sleep(5)
                        # notifications = Notification.objects.filter(receiver__id__exact=t)
                except Exception as e:
                    # print(str(e))
                    notified_socket.sendall("You don't have permission".encode())
                    sockets_list.remove(notified_socket)

        # handle some socket exceptions just in case
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
