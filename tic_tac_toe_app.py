import tkinter as tk
from tkinter import messagebox

board = ['', '', '', '', '', '', '', '', '']
Player = 0

# create GUI with the board
def showBoard():
    global Player
    turn_label.config(text=f"Player {Player + 1}'s turn")
    for i in range(3):
        for j in range(3):
            button = tk.Button(root, text=board[i * 3 + j], width=8, height=4,
                               command=lambda row=i, col=j: on_button_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")

def Draw():
    return '' not in board

def valid(row, col):
    return board[row * 3 + col] == ''

def checkWin(player):
    chk = 'X' if player == 0 else 'O'

    # check row
    if board[0] == chk and board[1] == chk and board[2] == chk:
        return True
    if board[3] == chk and board[4] == chk and board[5] == chk:
        return True
    if board[6] == chk and board[7] == chk and board[8] == chk:
        return True
    # check col
    if board[0] == chk and board[3] == chk and board[6] == chk:
        return True
    if board[1] == chk and board[4] == chk and board[7] == chk:
        return True
    if board[2] == chk and board[5] == chk and board[8] == chk:
        return True
    # check diagonal
    if board[0] == chk and board[4] == chk and board[8] == chk:
        return True
    if board[2] == chk and board[4] == chk and board[6] == chk:
        return True

    return False

# Function to handle button clicks
def on_button_click(row, col):
    global Player
    if valid(row, col):
        board[row * 3 + col] = 'X' if Player == 0 else 'O'
        showBoard()
        if checkWin(Player):
            messagebox.showinfo("Game Over", f"Player {Player + 1} Wins!")
            reset_game()
        elif Draw():
            messagebox.showinfo("Game Over", "Match Draw!")
            reset_game()
        else:
            Player ^= 1
            turn_label.config(text=f"Player {Player + 1}'s turn")

# Function to generate result message
def result_message():
    global Player
    if checkWin(0):
        return "Player 1 Wins!"
    elif checkWin(1):
        return "Player 2 Wins!"
    elif Draw():
        return "Match Draw!"
    else:
        return ""

def reset_game():
    result_label.config(text=result_message())
    global Player, board
    Player = 0
    board = ['', '', '', '', '', '', '', '', '']

    response = messagebox.askquestion("One more game?", "Do you want to play one more game?")

    if response == "yes":
        result_label.config(text="")
        showBoard()
    else:
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

window_width = 400
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"+{x_position}+{y_position}")

title_label = tk.Label(root, text="Tic Tac Toe", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=3)

turn_label = tk.Label(root, text="", font=("Helvetica", 16))
turn_label.grid(row=4, column=0, columnspan=3, sticky="w")

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.grid(row=4, column=2, columnspan=3, sticky="e")

# Set row and column weights to make the buttons expand and fill the available space
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

showBoard()
root.mainloop()
