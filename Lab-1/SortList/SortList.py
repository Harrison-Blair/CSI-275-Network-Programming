""" Description: Prompts the user for input until entering the magic word (done), then sorts the array of integers and floats submitted by the user

Author: Harrison Blair
Class: CSI-275-01
Assignment: Lab 1: Sorting with Python

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
keyword = "done"

def make_list():
    list = []
    finished = False
    while not finished:
        num = input("Enter a number ('done' to end): ")
        if num.lower() == keyword:
            finished = True
        else:
            try:
                x = float(num)
            except ValueError:
                print("Please enter a number (floats okay!)")
            else:
                list.append(float(num))
    print("Unsorted List: ")
    print(list)
    return list

def sort_list(list):
    print("Sorted List: ")
    print(sorted(list))
    return sorted(list)

def main():
    sort_list(make_list())

if __name__ == "__main__":
    main()

