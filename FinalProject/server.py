""" Server code for the final messaging service project

Author: Harrison Blair
Class: CSI-275-01
Assignment: Final Project

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
import threading, socket, json

# Server Host Info
HOST = "localhost"
SEND_PORT = 1245
RECV_PORT = 1246

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

class MessagingServer:
    """ A simple messaging server that allows for users to send public and private messages

    """
    def __init__(self, host, input_port, output_port):
        self.input_sock = self.create_server_socket(host, input_port)
        self.output_sock = self.create_server_socket(host, output_port)

        self.clients = []

        self.start_threads(self.input_sock, self.output_sock)

    def create_server_socket(self, host, port):
        """ Creates a new socket, binds to port, and listens """
        sock = socket.socket()
        sock.bind((host, port))
        sock.listen(20)

        return sock

    def handle_client(self, client_sock):
        try:
            while True:
                length = int.from_bytes(client_sock.recv(4), 'big')
                json_msg = recvall(client_sock, length).decode('utf-8')

                message = json.loads(json_msg)
                print(message)
                if message['type'] == 'BROADCAST':
                    for client in self.clients:
                        if not client[0] == message['name']:
                            client[1].send(len(json_msg).to_bytes(4, 'big') + json_msg.encode('utf-8'))
                elif message['type'] == 'PRIVATE':
                    found = False
                    for client in self.clients:
                        if client[0] == message['target']:
                            found = True
                            client[1].send(len(json_msg).to_bytes(4, 'big') + json_msg.encode('utf-8'))
                    if not found:
                        for client in self.clients:
                            if client[0] == message['name']:
                                err_msg = {"name": "!SERVER!", "type": "ERROR", "body": "User does not exist!"}
                                err_msg = json.dumps(err_msg)
                                client[1].send(len(err_msg).to_bytes(4, 'big') + err_msg.encode('utf-8'))
                elif message['type'] == 'EXIT':
                    for client in self.clients:
                        if client[0] == message['name']:
                            print(f"Ending Connection with {message['name']}")
                            client[1].close()
                            self.clients.remove((client[0], client[1]))
                    client_sock.close()
        except EOFError:
            print('Client socket has closed')
        except ConnectionResetError as e:
            print('Connection reset')
        except OSError:
            pass

    def reading_thread(self, sock):
        try:
            while True:
                client_sock, addr = sock.accept()

                print(f"Connection accepted!")
                print(f"    Socket Info: {client_sock}")

                t = threading.Thread(target=self.handle_client, args=(client_sock,))
                t.start()
        except EOFError:
            print('Client socket has closed')
        except ConnectionResetError as e:
            print('Connection reset')

    def writing_thread(self, sock):
        """Accepts new connections from client recv_sock and adds them to a list

        Added to a list as a tuple, with the name coming first for easy accession"""
        try:
            while True:
                client_sock, addr = sock.accept()

                length = int.from_bytes(client_sock.recv(4), 'big')
                json_msg = recvall(client_sock, length)

                start_msg = json.loads(json_msg)

                if start_msg["type"] == "START":
                    self.clients.append((start_msg["name"], client_sock))
                    print(f"Connection accepted!")
                    print(f"    Name: {start_msg['name']}")
                    print(f"    Socket Info: {sock}")
                else:
                    client_sock.close()
        except EOFError:
            print('Client socket has closed')
        except ConnectionResetError as e:
            print('Connection reset')


    def start_threads(self, input_sock, output_sock, workers=5):
        """ Starts new threads for the input and output sockets"""

        threads = []
        for x in range(workers):
            t = threading.Thread(target=self.reading_thread, args=(input_sock,))
            t.start()
            threads.append(t)

        for y in range(workers):
            t = threading.Thread(target=self.writing_thread, args=(output_sock,))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

if __name__ == '__main__':
    messaging_server = MessagingServer(HOST, SEND_PORT, RECV_PORT)
