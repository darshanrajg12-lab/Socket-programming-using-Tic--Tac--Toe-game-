# Multiplayer Tic Tac Toe using Socket Programming

## Overview

This project implements a multiplayer Tic Tac Toe game using Python socket programming.

The application follows a client-server architecture where one player acts as the server and another connects as a client.

The GUI is built using Tkinter and threading is used for handling simultaneous network communication.

## Features

- Multiplayer game over TCP sockets
- GUI built with Tkinter
- Client-server architecture
- Multithreading for network communication
- Packet analysis using Wireshark

## Technologies Used

- Python
- Socket Programming
- Tkinter
- Threading
- Wireshark

## Project Structure
tic-tac-toe-socket-game
│
├── src
│ ├── player1.py
│ ├── player2.py
│ └── gameboard.py
│
├── docs
│ └── project_report.pdf
│
├── screenshots
│
├── requirements.txt
└── README.md
## Running the Project

Start server:

python src/player1.py

Start client:

python src/player2.py
