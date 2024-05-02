"""Server code for Question #1 of Part 2 of the CSI-275 final exam.

Author: Duane Dunston (original author)
Author: Jason Reeves (modified code for CSI-275)
Class: CSI-275-01/02

"""

from socket import *
import _thread
import time, datetime

HOST = 'localhost'      # IP of server
PORT = 7778             # Port of server


def handler(client_socket, addr):
    """Handler function to server thread.

    Replies "Polo" to "Marco", otherwise returns "ERROR: Does not compute!"

    """
    while 1:
        data = client_socket.recv(4096)
        from_client = data.decode("ascii")

        if from_client == "Marco":
            return_data = "Polo"
        else:
            return_data = "ERROR: Does Not Compute!"

        client_socket.sendall(return_data.encode("ascii"))


if __name__ == "__main__":
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(20)

    while 1:
        client_sock, addr = sock.accept()
        _thread.start_new_thread(handler, (client_sock, addr))