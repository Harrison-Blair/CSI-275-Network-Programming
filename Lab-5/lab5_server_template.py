"""Short description of code goes here.

Author: Harrison Blair
Class: CSI-275-01
Assignment: Lab 5: Sorting Server

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
PORT = 20000


class SortServer:
    s = socket.socket()

    def __init__(self, host, port):
        """Initializes the server by calling bind on the port and localhost"""
        self.s.bind((host, port))
        pass

    def run_server(self):
        """Don't forget your docstring!"""
        self.s.listen()
        conn, addr = self.s.accept()
        with conn:
            print(f"Connection accepted at: {addr}")
            while True:
                data = conn.recv(1024)

                if not data:
                    break
                else:
                    # Split string and sort it
                    try:
                        string = data.decode('ascii')
                        chars = string.split()

                        if chars[0] != "LIST":
                            conn.sendall(str("ERROR").encode('ascii'))
                            break
                        else:
                            #SEND INFO TO CLIENT
                    except:
                        conn.send(str("Error").encode('ascii'))


if __name__ == "__main__":
    server = SortServer(HOST, PORT)
    server.run_server()
