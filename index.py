from tkinter import *
from gui import *
from minimax import *
from game import *
g = gui()
game = game()
mainmenu = Tk()
mainmenu.maxsize(width=350,height=120)
game.center(mainmenu)
mainmenu.title('Menu')
mainmenu.resizable(0,0)
def start_2p():
    mainmenu.destroy()
    g.main()
def start_ai():
    mainmenu.destroy()
    game.main()

def menu():
    b_player_1 = Button(mainmenu,text='One Player',height=2,command=start_ai)
    b_player_2 = Button(mainmenu,text='Two Player',height=2,command=start_2p)
    b_exit = Button(mainmenu,text='Exit',command=mainmenu.quit,height=2)
    b_player_1.pack(fill=X)
    b_player_2.pack(fill=X)
    b_exit.pack(fill=X)

menu()
mainmenu.mainloop()

