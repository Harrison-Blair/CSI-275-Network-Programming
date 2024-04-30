""" Client code for the final messaging service project

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
import threading, socket, random, json

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

class MessagingClient:
    """ A simple messaging client that allows communication with the messaging server

    """

    def __init__(self, host, send_port, recv_port):
        """ Creates initial sending and receiving sockets and starts threads

        """
        self.name = self.getScreenName()
        self.send_sock = self.create_client_socket(host, send_port)
        self.recv_sock = self.create_client_socket(host, recv_port)

        self.start_threads(self.name, self.send_sock, self.recv_sock)

    def create_client_socket(self, host, port):
        """ Creates new client socket and attempts to connect to the server"""
        sock = socket.socket()
        sock.connect((host, port))

        return sock

    def getScreenName(self):
        """ Prompts the user to enter a 3-16 character alphanumerical name"""
        while True:
            name = input("Select a 3-16 character alphanumerical screen-name: ")
            if 3 < len(name) < 16 and name.isalnum():
                return name
            else:
                print("Invalid screen name. Please try again.")

    def print_msg_to_console(self, message):
        print(f"{message['type']} {message['name']} : {message['body']}")

    def send_messages(self, sock, name):
        """ Handles sending messages to the server"""
        print(f"Welcome to the super awesome chatting place {name}!")
        print("    - To send a message to all users connected, simply enter")
        print("      the message you wish to broadcast.")
        print("    - To send a PRIVATE message, simply enter an [@] followed")
        print("      by the display name of the user you wish you send it to,")
        print("      followed by the message you want to send.")
        print("    - To exit, enter !exit")
        print("Happy chatting!")
        try:
            done = False
            while not done:
                while True:
                    txt = input(f"{name} : ")
                    if txt:
                        break

                command = txt.split(' ', 1)[0]
                command = command[1:]
                if txt[0] == "@":
                    target = txt.split(' ', 1)[0]
                    target = target[1:]
                    msg = {"name": name, "type": "PRIVATE", "target": target, "body": txt}
                elif command == "exit":
                    msg = {"name": name, "type": "EXIT", "body": ""}
                    done = True
                else:
                    msg = {"name": name, "type": "BROADCAST", "body": txt}

                json_msg = json.dumps(msg)
                sock.send(len(json_msg).to_bytes(4, 'big') + json_msg.encode('utf-8'))
                self.print_msg_to_console(msg)
        except EOFError:
            print('Client socket has closed')
        except ConnectionResetError as e:
            print('Connection reset')

    def recv_messages(self, sock, name):
        """"""
        # Basic Start Mssage
        start_msg = {"name": name, "type": "START", "body": ""}

        # json conversion for code readability
        start_json = json.dumps(start_msg)

        # Send start message
        sock.send(len(start_json).to_bytes(4, 'big') + start_json.encode("utf-8"))
        # Forever recieve messages
        while True:
            length = int.from_bytes(sock.recv(4), 'big')

            if length == 0:
                break

            message = recvall(sock, length).decode("utf-8")

            message = json.loads(message)

            print()
            self.print_msg_to_console(message)

    def start_threads(self, screen_name, send_sock, recv_sock):
        """ Starts the threads for the send and recv sockets"""
        send_thread = threading.Thread(target=self.send_messages, args=(send_sock, screen_name))
        recv_thread = threading.Thread(target=self.recv_messages, args=(recv_sock, screen_name))

        send_thread.start()
        recv_thread.start()

        send_thread.join()
        recv_thread.join()


if __name__ == '__main__':
    messaging_client = MessagingClient(HOST, SEND_PORT, RECV_PORT)
