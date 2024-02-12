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


class UDPClient:
    """Insert Description Here

    """
    rid = False
    host = ""
    port = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, host, port, rid=False):
        self.host = host
        self.port = port
        self.rid = rid

    def send_message_by_character(self, string):
        chars = []
        for char in string:
            chars.append(char)

        try:
            for char in chars:
                message = char.encode('ascii')

        except OSError:
            print("OSError")
        except TimeOutError:
            print("TimeOutError")


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
