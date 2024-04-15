"""Short description of code goes here.

Author: Harrison Blair
Class: CSI-275
Assignment: Lab 4

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)

Student code for Lab/HW 2.

Champlain College CSI-235, Spring 2019
The following code was written by Joshua Auerbach (jauerbach@champlain.edu)
"""
import socket
import constants
import random

class UDPClient:
    """Creates a client that is able to send messages one character at a time to a server

        Now with exponential backoff and request ID's!
    """

    def __init__(self, host, port, rid=False):
        self.rid = rid
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message_by_character(self, string):
        """Sends a message to the server one by one, waiting for a response each time"""

        for char in string:
            trying = True
            timeout_time = constants.INITIAL_TIMEOUT
            req_id = random.randint(0, constants.MAX_ID)

            message = char

            if self.rid:
                message = str(req_id) + "|" + message

            while trying:
                try:
                    if constants.MAX_TIMEOUT <= timeout_time:
                        raise TimeoutError("Timeout exceeded")
                    self.socket.settimeout(timeout_time)

                    print(f"Sending {char}... (req_id: {req_id})")
                    self.socket.sendto(message.encode("ascii"), self.address)

                    recv = self.socket.recv(1024).decode("ascii")
                    print(f"Received {recv}!")

                    trying = False

                    if self.rid and len(recv) > 0:
                        if req_id == int(recv[1]):
                            trying = True

                except socket.timeout:
                    timeout_time = timeout_time * 2.0
                    trying = True

                except OSError:
                    raise OSError("Could not")


class TimeOutError(Exception):
    pass


def main():
    """Run some basic tests on the required functionality.

    for more extensive tests run the autograder!
    """
    client = UDPClient(constants.HOST, constants.ECHO_PORT)
    print(client.send_message_by_character("hello world"))

    client = UDPClient(constants.HOST, constants.REQUEST_ID_PORT, True)
    print(client.send_message_by_character("hello world"))


if __name__ == "__main__":
    main()
