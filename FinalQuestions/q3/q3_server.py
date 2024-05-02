"""Student code for Question 3 of Part 2 of the 275 final exam.

Author: TODO put your name here
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

import socket, json, zlib, _thread

HOST = 'localhost'      # IP of server
PORT = 7780             # Port of server


def handler(client_socket, addr):
    """Handler function to server thread.

    Compares the compressed and uncompressed lengths of the
    provided data, and replies whether it should have been
    compressed or not.

    """
    while 1:
        compressed = client_socket.recv(8192)

        if len(compressed) < 1:
            client_socket.close()
            break

        # TODO Decompress data
        decompressed = zlib.decompress(compressed)
        # TODO Compare length of compressed and uncompressed data
        if len(compressed) < len(decompressed):
            # TODO If compressed is smaller, return the string "Yes"
            return_string = "Yes"
        else:
            return_string = "No"
        # TODO If decompressed is smaller, return the string "No"
        # (no need to turn the return string into JSON)

        client_socket.sendall(return_string.encode("utf-8"))


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(20)

    while 1:
        client_sock, addr = sock.accept()
        _thread.start_new_thread(handler, (client_sock, addr))