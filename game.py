from __future__ import print_function
import minimax
from tkinter import messagebox as msg
from tkinter import *
class game (object):
    board = None
    Round = 0
    turn = None
    finished = None
    players = [None , None]
    winner = None
    check = None
    start = None
    again = None
    cols = None
    win = None
    game = None
    
    def __init__(self):
        self.board = []
        for x in range(6):
            self.board.append([])
            for y in range(7):
                self.board[x].append('.')

        self.players[0] = AI_player()
        self.players[1] = player('o')
        self.turn = self.players[0]


    def main(self):
        self.game = Tk()
        self.game.title('Connect 4')
        self.center(self.game)
        self.game.minsize(width=440,height=300)
        frame = Frame(self.game,width=500,height=500)
        frame.grid()
        i = 1
        self.cols = [0 for x in range(7)]
        self.check = [[0 for x in range(7)] for x in range(6)]
        for row in range(6):
            self.check.append([])
            for col in range(7):
                self.check[row][col]=Label(frame,width=8,height=2,borderwidth=2,relief="ridge",bg='white')
                self.check[row][col].grid(column=col,row=row+1)

        self.start = Button(frame, width=8, height=2, text='Start',state= 'normal', borderwidth=2, relief="ridge",bg='black',fg='white',command=self.Start_AI)
        self.start.grid(column=0,row=9)

        for inp in range(7):
            self.cols[inp] = Button(frame, width=7, height=2, text=i, borderwidth=2,state='disabled', relief="ridge",command=lambda x=inp: self.next_move(x))
            i += 1
            self.cols[inp].grid(column=inp,row=0)
        self.game.mainloop()

    def print_state(self):
        for x in range (6,0,-1):

            for y in range(7,0,-1):

                print (self.board[x-1][y-1] , end=" ")
            print ("\n")
        return
    
    
    def switch_player (self):
        
        if (type(self.turn) is type(self.players[0])):
            self.turn = self.players[1]

        else:
            self.turn = self.players[0]
            
        self.Round = self.Round + 1
        return

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
        g = game()
        g.main()


        #msg._show('Congratulations !! ',winner)

        
    def next_move (self,col):

        if(self.winner == None):
            p = self.turn

            if (self.Round > 42):
                self.finished = True
                return

            m = p.move_Player(col)
            for i in range(6):
                 if(self.board[i][m] == "."):
                    self.board[i][m] = p.color
                    #print(i,m)
                    self.gui()
                    self.check_fours()
                    self.switch_player()
                    if self.turn.color == 'x':
                        self.Start_AI()
                    return
        else:
            self.cong()
        return

    def Start_AI(self):
        for button in self.cols:
            button['state'] = 'normal'
        self.start['state'] = 'disabled'
        if self.winner == None:
            p = self.turn
            col = p.move_AI(self.board)
            for row in range(6):
                if(self.board[row][col] == "."):
                    self.board[row][col] = p.color
                    #print(row,col)
                    self.gui()
                    self.check_fours()
                    self.switch_player()
                    break
        if (self.winner != None):
            self.cong()
        return

    

    def gui(self):
        for row in range(6):
            for col in range(7):
                if self.board[row][col] == 'x':
                    self.check[row][col].config(bg='red')
                elif self.board[row][col] == 'o':
                    self.check[row][col].config(bg='green')

    def check_fours (self):
        self.check_raw()
        self.check_col()
        self.check_diagnol()
    
    def check_raw (self):
        for k in range (6):
            for i in range(4):
                if (self.board[k][i] == self.board[k][i+1] == self.board[k][i+2] == self.board[k][i+3] == self.turn.color):
                    self.check[k][i].config(bg='yellow')
                    self.check[k][i + 1].config(bg='yellow')
                    self.check[k][i + 2].config(bg='yellow')
                    self.check[k][i + 3].config(bg='yellow')
                    self.winner = self.turn.color
    
   
    def check_col (self):
        for k in range (3):
            for i in range(7):
                if (self.board[k][i] == self.board[k+1][i] == self.board[k+2][i] == self.board[k+3][i] == self.turn.color ):
                    self.check[k][i].config(bg='yellow')
                    self.check[k+1][i].config(bg='yellow')
                    self.check[k+2][i].config(bg='yellow')
                    self.check[k+3][i].config(bg='yellow')
                    self.winner = self.turn.color       
    
    
    def check_diagnol(self):
        for k in range (3):
            for i in range(4):
                if (self.board[k][i] == self.board[k+1][i+1] == self.board[k+2][i+2] == self.board[k+3][i+3] == self.turn.color ):
                    self.check[k][i].config(bg='yellow')
                    self.check[k + 1][i + 1].config(bg='yellow')
                    self.check[k + 2][i + 2].config(bg='yellow')
                    self.check[k + 3][i + 3].config(bg='yellow')
                    self.winner = self.turn.color
                    return 
        for k in range (5,2,-1):
            for i in range(4):
                if (self.board[k][i] == self.board[k-1][i+1] == self.board[k-2][i+2] == self.board[k-3][i+3] == self.turn.color ):
                    self.check[k][i].config(bg='yellow')
                    self.check[k - 1][i + 1].config(bg='yellow')
                    self.check[k - 2][i + 2].config(bg='yellow')
                    self.check[k - 3][i + 3].config(bg='yellow')
                    self.winner = self.turn.color
        
        
class player(object):
    color = None  
    
    def __init__ (self, color):
        self.color = color   
        

    def move_Player(self ,col):
        return col




class AI_player () :
    
    color = 'x'

    def move_AI (self ,state):
        m = minimax.minimax()
        nxt_move =  m.best_move(state, self.color)
        return nxt_move

