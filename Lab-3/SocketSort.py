""" Description: Prompts the user for input until entering the magic word (done),
 then sends the entered list to a designated server to be sorted, then it is returned
 and printed to console.

Author: Harrison Blair
Class: CSI-275-01
Assignment: Lab 3: Socket Sorting

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

KEYWORD = "done"
S_IP = "68.183.63.165"
S_PORT = 7778

def build_list():
    """Prompts the user through console to input numbers until 'done', also
    verifies input and rejects any non-numbers. Returns the list entered when done"""
    list = []
    finished = False
    while not finished:
        num = input("Enter a number ('done' to end): ")
        if num.lower() == KEYWORD:
            finished = True
        else:
            try:
                x = float(num)
            except ValueError:
                print("Please enter a number (floats okay!)")
            else:
                list.append(float(num))
    return list


def list_to_bytestring(list):
    """Converts an inputed list into a byte string for protocol formating,
    returns an ascii encoded string"""
    string = "LIST "
    for entry in list:
        string += f'{entry} '
    print(string)
    return string.encode('ascii')


def sort_list(list):
    """Takes a list as an input, converts it to the proper protocol,
    then sends the data to the server to be sorted. Prints the reply when finished."""
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((S_IP, S_PORT))
    connection.sendall(list_to_bytestring(list))

    reply = connection.recv(4096)
    print(reply.decode('ascii'))

    connection.close()
    return


def main():
    sort_list(build_list())


if __name__ == "__main__":
    main()