"""Student code for Question 2 of Part 2 of the 275 final exam.

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
import socket, random

HOST = 'localhost'      # IP of server
PORT = 7779             # Port of server


def connect_to_server():
    # TODO Make "sock" a TCP socket that connects to the server
    sock = socket.socket()
    sock.connect((HOST, PORT))

    # Create a random string of cats
    num_cats = random.randint(200, 500)
    cat_string = "cat" * num_cats

    # TODO Add an 8 byte, little-endian length field for the cat string
    length_bytes = len(cat_string).to_bytes(8, 'little')

    # TODO Send the length field with the string (length field first)
    sock.send(length_bytes + cat_string.encode("ascii"))

    # Get the data back from the server
    response = sock.recv(4096)
    num_cats_server = response.decode("ascii")

    # See if the values are equal
    print(f"Cats sent: {num_cats}")
    print(f"Cats received: {num_cats_server}")
    if num_cats == int(num_cats_server):
        print("You did it!")
    else:
        print("Something's wrong...")


if __name__ == "__main__":
    connect_to_server()