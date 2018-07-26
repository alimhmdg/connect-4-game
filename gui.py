from tkinter import *
from tkinter import messagebox as msg
class gui:
    round = None
    turn = None
    end = None
    winner = None
    check = None
    game = None
    win = None
    def __init__(self):
        self.round =0
        self.turn = 'green'

    def main(self):
        self.game = Tk()
        self.game.title('Connect 4')
        self.game.minsize(width=414, height=288)
        self.center(self.game)
        frame = Frame(self.game,width=500,height=500)
        frame.grid()
        i = 1
        self.check = [[0 for x in range(7)] for x in range(7)]
        for row in range(7):
            self.check.append([])
            for col in range(7):
                if row == 6:
                    self.check[row][col]=Button(frame, width=7, height=2,text=i,borderwidth=2,relief="ridge",command=lambda x1=col: self.play(x1))
                    i += 1
                else:
                    self.check[row][col]=Button(frame,width=7,height=2,borderwidth=2,relief="ridge",bg='white')
                self.check[row][col].grid(column=col,row=row)
        self.game.mainloop()

    def center(self,toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w / 2 - size[0] / 2
        y = h / 2 - size[1] / 2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def cong(self):
        winner_msg = 'Congratulations !! ' + self.winner
        self.win = Tk()
        self.win.title('Msg')
        self.center(self.win)
        self.win.maxsize(width=300,height=100)
        winner = Label(self.win,text=winner_msg,height=3,bg='black',fg='white')
        winner.pack(fill=X)
        self.again = Button(self.win,text='Play Again',height=3,command=self.restart)
        self.again.pack(fill=X)
        self.win.mainloop()

    def restart(self):
        self.game.destroy()
        self.win.destroy()
        g = gui()
        g.main()

    def change_player(self):
        if self.turn == 'green':
            self.turn = 'red'
        else:
            self.turn = 'green'
        self.round += 1

    def play(self,col):
        if self.winner == None:
            if self.round >= 42:
                self.end = True
                return
            if self.end != True:
                for row in range(5,-1,-1):
                    if (self.check[row][col].cget('bg')) == 'white':
                        self.check[row][col].config(bg=self.turn)
                        break
                self.waysWin()
                self.change_player()
        if self.winner != None:
            self.cong()
            return


    def waysWin(self):
        self.colWin()
        self.rowWin()
        self.curveWin()

    def colWin(self):
        for col in range(7):
            for row in range(5,2,-1):
                if (self.check[row][col].cget('bg') == self.check[row - 1][col].cget('bg') == self.check[row - 2][col].cget('bg') == self.check[row - 3][col].cget('bg') == self.turn):
                    self.check[row][col].config(bg='yellow')
                    self.check[row-1][col].config(bg='yellow')
                    self.check[row-2][col].config(bg='yellow')
                    self.check[row-3][col].config(bg='yellow')
                    self.winner = self.turn
                   # print("congratulations !! " + self.winner)
                    self.end = True;
                    return

    def rowWin(self):
        for row in range(5,-1,-1):
            for col in range(4):
                if(self.check[row][col].cget('bg') == self.check[row][col+1].cget('bg') == self.check[row][col+2].cget('bg') == self.check[row][col+3].cget('bg') == self.turn):
                    self.check[row][col].config(bg='yellow')
                    self.check[row][col + 1].config(bg='yellow')
                    self.check[row][col + 2].config(bg='yellow')
                    self.check[row][col + 3].config(bg='yellow')
                    self.winner = self.turn
                    #print("congratulations !! " + self.winner)
                    self.end = True;
                    return

    def curveWin(self):
        for row in range(3):
            for col in range(4):
                if (self.check[row][col].cget('bg') == self.check[row+1][col+1].cget('bg') == self.check[row+2][col+2].cget('bg') == self.check[row+3][col+3].cget('bg') == self.turn):
                    self.check[row][col].config(bg='yellow')
                    self.check[row + 1][col + 1].config(bg='yellow')
                    self.check[row + 2][col + 2].config(bg='yellow')
                    self.check[row + 3][col + 3].config(bg='yellow')
                    self.winner = self.turn
                    #print("congratulations !! " + self.winner)
                    self.end = True;
                    return
        for row in range(5,2,-1):
            for col in range(4):
                if (self.check[row][col].cget('bg') == self.check[row-1][col+1].cget('bg') == self.check[row-2][col+2].cget('bg') == self.check[row-3][col+3].cget('bg') == self.turn):
                    self.check[row][col].config(bg='yellow')
                    self.check[row - 1][col + 1].config(bg='yellow')
                    self.check[row - 2][col + 2].config(bg='yellow')
                    self.check[row - 3][col + 3].config(bg='yellow')
                    self.winner = self.turn
                    #print("congratulations !! " + self.winner)
                    self.end = True;
                    return

