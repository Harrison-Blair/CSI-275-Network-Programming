"""Server code for Lab 6_2

Author: Harrison Blair
Class: CSI-275-01
Assignment: Lab 6_2

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

import socket

HOST = "localhost"
PORT = 45000


def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            break
        data += more
    return data


class LengthServer:
    """Create a server that return the length of received strings."""
    sock = socket.socket()

    def __init__(self, host, port):
        """Creates the TCP socket, then binds to the socket and address specified"""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))

    def calc_length(self):
        """Don't forget your docstring!"""
        self.sock.listen(1)
        print("Waiting for a connection... @ ", self.sock.getsockname())
        while True:
            sc, sockname = self.sock.accept()
            print("Connection from", sockname)
            print("    Socket name:", sc.getsockname())
            print("    Socket peer:", sc.getpeername())
            length = int.from_bytes(sc.recv(4), 'big')
            message = recvall(sc, length)
            print("    Bytes expected: ", length)
            print("    I received ", len(message), " bytes.")
            print("    ", message)
            if length != len(message):
                reply_string = "Length Error"
                reply_to_send = len(reply_string).to_bytes(4, 'big') + reply_string.encode("ascii")
                sc.sendall(reply_to_send)
            else:
                reply_string = f"I received {len(message)} bytes."
                reply_to_send = len(reply_string).to_bytes(4, 'big') + reply_string.encode("ascii")
                sc.sendall(reply_to_send)
            sc.close()
            print("    Reply sent, connection closed.")




if __name__ == "__main__":
    server = LengthServer(HOST, PORT)
    server.calc_length()
