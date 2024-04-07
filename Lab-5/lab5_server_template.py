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
import numbers

HOST = "localhost"
PORT = 20000


class FormatError(Exception):
    pass


class SortServer:
    s = socket.socket()

    def __init__(self, host, port):
        """Initializes the server by calling bind on the port and localhost"""
        self.s.bind((host, port))
        self.address = (host, port)
        pass

    def run_server(self):
        """Hosts a server that listens for incoming transmissions of numbers and sorts them

        Has an optional parameter for the sorting method
        Validates that all values are floats/ints
        Makes sure that the transmissions are in proper format
        """
        self.s.listen()
        print(f"Listening @ {self.address}")

        conn, addr = self.s.accept()
        with conn:
            print(f"Connection accepted at: {addr}")
            while True:
                data = conn.recv(1024)

                if not data:
                    conn.sendall(str("ERROR").encode('ascii'))
                    break
                else:
                    # Split string and decode
                    try:
                        string = data.decode('ascii')
                        items = string.split()
                        final_item = items[len(items) - 1].split("|")
                        sorting_mode = 'a'

                        if len(final_item) == 2:
                            items.remove(items[len(items) - 1])
                            items.append(final_item[0])
                            sorting_mode = final_item[1]

                        print()
                        print(f"  Received: {string}")

                        # If the first item in the array is NOT "LIST", tell the client no
                        if items[0] != "LIST":
                            raise FormatError

                        # If there is less than 2 items and the first is LIST then there is nothing to sort
                        if len(items) < 2:
                            raise FormatError

                        # Try to float each item to see if float
                        for item in items[1:]:
                            float(item)

                        # Decides the sorting mode and sorts
                        if sorting_mode == "a":
                            nums = sorted(items[1:], key=float)
                        elif sorting_mode == "d":
                            nums = sorted(items[1:], key=float, reverse=True)
                        elif sorting_mode == "s":
                            nums = sorted(items[1:])
                        else:
                            raise FormatError

                        message_to_send = "SORTED"

                        for num in nums:
                            message_to_send += f" {num}"

                        conn.sendall(message_to_send.encode('ascii'))
                        print(f"  Sent: {message_to_send}")

                    except UnicodeDecodeError:
                        print("    ERROR: Unicode Decoding Error")
                        conn.sendall(str("ERROR").encode('ascii'))

                    except ValueError:
                        print("    ERROR: Type Error")
                        conn.sendall(str("ERROR").encode('ascii'))

                    except FormatError:
                        print("    ERROR: Formatting")
                        conn.sendall(str("ERROR").encode('ascii'))

            conn.close()


if __name__ == "__main__":
    server = SortServer(HOST, PORT)
    server.run_server()
