"""Server code for Question #3 of Part 2 of the CSI-275 final exam.

Author: Jason Reeves
Class: CSI-275-01/02

"""
import socket, json, zlib

HOST = 'localhost'      # IP of server
PORT = 7780             # Port of server


def connect_to_server():
    # TODO Make "sock" a TCP socket that connects to the server
    sock = socket.socket()
    sock.connect((HOST, PORT))

    # Send lists of size 5, 50, and 500 to the server
    # These lists are serialized as JSON, encoded, and compressed
    for i in [5, 50, 500]:
        list_to_send = [j for j in range(1, i)]
        json_list = json.dumps(list_to_send)
        json_encoded = json_list.encode("utf-8")
        json_compressed = zlib.compress(json_encoded)
        sock.sendall(json_compressed)

        # Get the data back from the server
        response = sock.recv(4096)
        print(response.decode("utf-8"))


if __name__ == "__main__":
    connect_to_server()