import socket
import select
import errno  # matches error codes
import sys
import os
import tkinter as tk
from tkinter.font import Font
from tkinter import *
from tkinter import ttk, messagebox as msg_box


class client():
    def __init__(self, ip='', port='', username='', font=None):
        self.__IP = ip
        self.__PORT = port
        self.__CLIENT_FONT = font
        self.__my_username = username
        self.__connect()

    def __connect(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print ('Successful connection to master server!')
        HEADER_LENGTH = 10
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.__IP, self.__PORT))
        client_socket.setblocking(False)

        username = self.__my_username.encode("utf-8")
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(username_header + username)

        while True:
            message = input(f"{self.__my_username} > ")
            if message and 0 < + len(message) < 121:
                message = message.encode("utf-8")
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
                client_socket.send(message_header + message)
            else:
                print("Enter a message between 1 and 120 characters")
            try:
                while True:  # receive messages
                    username_header = client_socket.recv(HEADER_LENGTH)
                    if not len(username_header):  # no data received
                        print("connection closed by the server")
                        sys.exit()

                    username_length = int(username_header.decode("utf-8").strip())
                    username = client_socket.recv(username_length).decode("utf-8")

                    message_header = client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode("utf-8"))
                    message = client_socket.recv(message_length).decode("utf-8")

                    print(f"{username} > {message}")

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:  # no more messages to be received
                    msg_box.showerror('Reading error', str(e))
                    sys.exit()
                continue

            except Exception as e:
                msg_box.showerror('General Error ', str(e))
                sys.exit()


"""HEADER_LENGTH=10

IP="127.0.0.1"
PORT=1234

my_username=input("Username: ")
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username=my_username.encode("utf-8")
username_header=f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
    message=input(f"{my_username} > ")
    if message and 0 <+ len(message) < 121:
        message=message.encode("utf-8")
        message_header=f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)
        time.sleep(3)
    else:
        print("Enter a message between 1 and 120 characters")
    try:
        while True: #receive messages
            username_header=client_socket.recv(HEADER_LENGTH)
            if not len(username_header):#no data received
                print("connection closed by the server")
                sys.exit()
            
            username_length=int(username_header.decode("utf-8").strip())
            username =client_socket.recv(username_length).decode("utf-8")
            
            message_header=client_socket.recv(HEADER_LENGTH)
            message_length=int(message_header.decode("utf-8"))
            message=client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")
            
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:#no more messages to be received
            print('Reading error',str(e))
            sys.exit()
        continue
    
    except Exception as e:
        print('General Error ',str(e))
        sys.exit()
"""
