from tkinter import *

WIN_COLOR = 'red'

class TicTacToe(object):
    def __init__(self):
        self.window = Tk()
        self.window.title('Tic Tac Toe')
        self.window.resizable(False,False)
        
        self.main_grid = Frame(self.window,bd=3,width=600,height=600)
        self.main_grid.grid(pady=(80,15), padx=15)
        
        self.playerTurn = True
        self.board = [' ' for i in range(10)]

        self.makeGUI()
        self.makeButton()
        self.window.mainloop()
        self.b1 

    def makeGUI(self):
        roleFrame = Frame(self.window)
        roleFrame.place(relx=0.5, y=45, anchor="center")
        self.roleLabel = Label(roleFrame, text="Player : X    Computer : O",font=('Arial',20))
        self.roleLabel.grid(row=0)

        self.resetLabel = Button(roleFrame, text="Reset",font=('Helvetica',14), command=lambda : self.reset())
        self.resetLabel.grid(row=1)

    def makeButton(self):
        self.b1 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b1))
        self.b2 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b2))
        self.b3 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b3))
        self.b4 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b4))
        self.b5 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b5))
        self.b6 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b6))
        self.b7 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b7))
        self.b8 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b8))
        self.b9 = Button(self.main_grid, text=" ", font=("Helvetica", 40), height=2, width=3, bg="white", command=lambda: self.playerMove(self.b9))

        self.buttons = ['', self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
        self.board = [' ' for i in range(10)]

        self.b1.grid(row=0, column=0, padx=10, pady=10)
        self.b2.grid(row=0, column=1, padx=10, pady=10)
        self.b3.grid(row=0, column=2, padx=10, pady=10)
        self.b4.grid(row=1, column=0, padx=10, pady=10)
        self.b5.grid(row=1, column=1, padx=10, pady=10)
        self.b6.grid(row=1, column=2, padx=10, pady=10)
        self.b7.grid(row=2, column=0, padx=10, pady=10)
        self.b8.grid(row=2, column=1, padx=10, pady=10)
        self.b9.grid(row=2, column=2, padx=10, pady=10)

    def playerMove(self, b):
        if b['text'] == ' ' and self.playerTurn:
            b["text"] = "X"
            boardIndex = self.buttons.index(b)
            self.board[boardIndex] = 'X'
            self.playerTurn = False

        if self.isWinner(self.board, 'X'):
            self.isWinner(self.board, 'X')
            self.disbale()
            self.winnerMessage('X')
        else:
            self.computerMove()
    
    def computerMove(self):
        move = self.computer()
        self.playerTurn = True
        if move == 0:
            self.disbale()
            self.winnerMessage("Tie")
        else:
            self.buttons[move]['text'] = 'O'
            self.board[move] = 'O'
            self.playerTurn = True
            if self.isWinner(self.board, 'O'):
                self.disbale()
                self.winnerMessage('O')
    
    def winnerMessage(self, letter):
        if letter == 'X':
            self.roleLabel['text'] = 'Congratulations, You Won!!!'
        elif letter == 'O':
            self.roleLabel['text'] = 'Sorry, Computer won this time!'
        elif letter == 'Tie':
            self.roleLabel['text'] = 'Tie Game!!'

    
    def isWinner(self, board, letter):
        if board[1]==letter and board[2] == letter and board[3] == letter:
            self.b1.config(bg=WIN_COLOR)
            self.b2.config(bg=WIN_COLOR)
            self.b3.config(bg=WIN_COLOR)
            return True
        elif board[4]==letter and board[5] == letter and board[6] == letter:
            self.b4.config(bg=WIN_COLOR)
            self.b5.config(bg=WIN_COLOR)
            self.b6.config(bg=WIN_COLOR)
            return True
        elif board[7]==letter and board[8] == letter and board[9] == letter:
            self.b7.config(bg=WIN_COLOR)
            self.b8.config(bg=WIN_COLOR)
            self.b9.config(bg=WIN_COLOR)
            return True
        elif board[1]==letter and board[4] == letter and board[7] == letter:
            self.b1.config(bg=WIN_COLOR)
            self.b4.config(bg=WIN_COLOR)
            self.b7.config(bg=WIN_COLOR)
            return True
        elif board[2]==letter and board[5] == letter and board[8] == letter:
            self.b2.config(bg=WIN_COLOR)
            self.b5.config(bg=WIN_COLOR)
            self.b8.config(bg=WIN_COLOR)
            return True
        elif board[3]==letter and board[6] == letter and board[9] == letter:
            self.b3.config(bg=WIN_COLOR)
            self.b6.config(bg=WIN_COLOR)
            self.b9.config(bg=WIN_COLOR)
            return True
        elif board[1]==letter and board[5] == letter and board[9] == letter:
            self.b1.config(bg=WIN_COLOR)
            self.b5.config(bg=WIN_COLOR)
            self.b9.config(bg=WIN_COLOR)
            return True
        elif board[3]==letter and board[5] == letter and board[7] == letter:
            self.b3.config(bg=WIN_COLOR)
            self.b5.config(bg=WIN_COLOR)
            self.b7.config(bg=WIN_COLOR)
            return True
    
    def selectRandom(self,li):
        import random
        ln = len(li)
        r = random.randrange(0,ln)
        return li[r]

    def computer(self):
        possibleMoves = [x for x, letter in enumerate(self.board) if letter == ' ' and x != 0]
        move = 0
        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = self.board[:]
                boardCopy[i] = let
                if self.isWinner(boardCopy, let):
                    move = i
                    return move
        cornersOpen = []
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
        if len(cornersOpen) > 0:
            move = self.selectRandom(cornersOpen)
            return move
        if 5 in possibleMoves:
            move = 5
            return move
        edgesOpen = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)      
        if len(edgesOpen) > 0:
            move = self.selectRandom(edgesOpen) 
        return move

    def disbale(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)
    
    def reset(self):
        self.roleLabel['text'] = "Player : X    Computer : O"
        self.makeButton()
    

if __name__ == '__main__':
    TicTacToe()