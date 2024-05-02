"""Server code for Question #2 of Part 2 of the CSI-275 final exam.

Author: Duane Dunston (original author)
Author: Jason Reeves (modified code for CSI-275)
Class: CSI-275-01/02

"""

from socket import *
import _thread
import time, datetime

HOST = 'localhost'      # IP of server
PORT = 7779             # Port of server


def handler(client_socket, addr):
    """Handler function to server thread.

    Returns the number of "cat" words sent to the server.

    """
    while 1:
        # Get the length of the data
        data_length_field = client_socket.recv(8)
        data_length = int.from_bytes(data_length_field, "little")

        # Read the rest of the data
        data_string = client_socket.recv(data_length)

        data_string = data_string.decode("ascii")

        # Count how many cats were sent
        num_cats = int(len(data_string) / 3)

        # Return the cat count to the server
        # (no length field here)
        client_socket.sendall(str(num_cats).encode("ascii"))


if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(20)

    while 1:
        client_sock, addr = sock.accept()
        _thread.start_new_thread(handler, (client_sock, addr))