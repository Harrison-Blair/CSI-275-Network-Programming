"""Student code for Question 1 of Part 2 of the 275 final exam.

Author: Harrison Blair
Class: CSI-275-01

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

HOST = 'localhost'      # IP of server
PORT = 7778             # Port of server


def connect_to_server():
    # TODO Make "sock" a TCP socket that connects to the server
    sock = socket.socket()
    sock.connect((HOST, PORT))

    # TODO Send the string "Marco" to the server
    sock.send("Marco".encode("ascii"))

    # Get and print the server response
    response = sock.recv(4096)
    print(response.decode("ascii"))


if __name__ == "__main__":
    connect_to_server()
