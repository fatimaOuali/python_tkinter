import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.create_widgets()

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self, text="", font=("Helvetica", 20), width=6, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(" " not in row for row in self.board):
                messagebox.showinfo("Tie!", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showwarning("Invalid Move", "This position is already occupied. Try again.")

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = " "
        self.current_player = "X"

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
