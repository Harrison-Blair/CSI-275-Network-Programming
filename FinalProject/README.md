# CSI-275-02 Network Programming Final Project

These python scripts impliment client and server functionality for a chat program. The program allows users to pick a screen name and send either public or private (individual) messages. This is accomplished through the use of UTF-8 encoded JSON messages sent over a TCP connection to the server. The server has the capability for "unlimited" connections, solely limited by hardware, due to the use of threading. The implemenation was done on Python 3.11, due to the majority of the class's code being written in that version.

## Setup

**! IMPORTANT !**

***By default the server runs on ports 1245 and 1246. If you wish to change the ports OR the hostname, edit the HOST, SEND_PORT, and/or RECV_PORT variables in BOTH the server.py and client.py files!***

First set up the server by running the server.py script, then clients may launch the client.py script. Clients will not attempt connection until a valid screen name is entered.

## How to use the client

### Account Creation

When opening the client.py program, the user will be prompted to enter an [alphanumeric](https://www.geeksforgeeks.org/python-string-isalnum-method/) username.
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/9f5c0b9c-b174-4f75-849b-6b4e87117ce6)

After entering a valid username, the user will be greeted with a menu-like screen displaying all the optional actions.
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/9a39263a-f6a1-457b-8333-60f514d7eca2)

This is all that is required in order to recieve messages, which will populate the console when recieved
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/6b61fee9-fdda-41aa-ac1e-406f7e18d7a1)

### Sending Messages
There are two kinds of messages you are able to send.
- Broadcasts are sent to all users who are connected to the server
- Private messages are shared between the user who sent them and their target recipient only

#### Public Messages
In order to send a public message, type out your message and press enter.
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/5356d7b1-dd32-479f-b05f-f454d5f8469e)
The message will be repeated in console for the user who sent it, and will be printed for every other user connected

#### Private Messages
In order to send a private message, begin your message with a '@' symbol followed by the username of the recipient. In the event that 'Harrison' wants to send a private message to 'Joe', they would input the following. User names are case sensitive!
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/8fc0aa00-dad2-4f24-8770-1aba13260364)

If the user requested doesnt exist, or can't be found, the user will recieve an error message
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/43ffac85-b0b3-45de-9cb7-86993872f09b)

Private messages when recieved will look like the following.
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/0bea1cbf-9d17-4bdd-b8b5-afe25d68b438)

### Exiting
In order to exit the program, type '!' followed by 'exit'. This is also case sensitive, so be careful.
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/3e568a7a-7538-4a54-aa55-5f76223abc5f)
This will close the program and tell the server to remove you from the list of users active. If you do not use '!exit', the server will still think you are connected, which may cause errors.

## Server Console
The output of server.py is purely for diagnostic and debugging purposes.

When a user connects to the server, the following START message will be output in console:
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/cf5a7b19-16e6-4827-960e-180b32c5c3b8)

When a user sends a BROADCAST message, the following will be output to console:
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/7d42e0ce-0632-4127-8b3e-5668f02961ea)

If a user sends a PRIVATE message, it will show as private, and will say who the target of the message is.
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/354800cd-0d69-43e5-b460-00ea957b7d5a)

Once a user enters the '!exit' command, the server will output the connection that has been ended
![image](https://github.com/Harrison-Blair/CSI-275-Network-Programming/assets/90780621/74a85700-75d0-4e71-adf7-c7376c866549)
