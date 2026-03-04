# Player 1 (Server)

import socket
import threading
import gameboard as gb
from tkinter import *
from tkinter import messagebox

serverAddress = '127.0.0.1'
port = 8000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress,port))
serverSocket.listen(1)

clientSocket = None
start = False
user = False
player2 = ""
board = None
pos = 0


def createThread(con):
    thread = threading.Thread(target=con)
    thread.daemon = True
    thread.start()


def receive():
    global start,user,player2,board
    while True:
        if start and not user:
            try:
                data = clientSocket.recv(1024)
                name = data.decode()

                board = gb.Board(name)
                player2 = name

                sendData = "player1".encode()
                clientSocket.send(sendData)

                user = True
            except:
                pass


def acceptConnection():
    global clientSocket,start

    clientSocket,address = serverSocket.accept()

    message = "Incoming play request from "+str(address)
    answer = messagebox.askyesno("Connection",message)

    if answer:
        clientSocket.send("accepted".encode())
        start = True
        receive()

    else:
        clientSocket.send("rejected".encode())
        clientSocket.close()


createThread(acceptConnection)

window = Tk()
window.title("Tic Tac Toe Player1")
window.geometry("400x400")

label = Label(window,text="Server Running")
label.pack()

window.mainloop()