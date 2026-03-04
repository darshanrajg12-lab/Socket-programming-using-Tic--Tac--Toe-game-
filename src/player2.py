# Player 2 (Client)

import socket
from tkinter import *
from tkinter import messagebox

serverAddress = '127.0.0.1'
port = 8000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectServer():

    try:
        clientSocket.connect((serverAddress,port))
        clientSocket.send("player2".encode())

        response = clientSocket.recv(1024).decode()

        if response == "accepted":
            messagebox.showinfo("Connected","Connected to server")
        else:
            messagebox.showerror("Rejected","Server rejected connection")

    except:
        messagebox.showerror("Error","Unable to connect")


window = Tk()
window.title("Tic Tac Toe Player2")
window.geometry("400x400")

button = Button(window,text="Connect",command=connectServer)
button.pack()

window.mainloop()