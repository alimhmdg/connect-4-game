from __future__ import print_function

from game import *
class minimax:
    state = None
    
    color = ["x","o"]
    """
    def __init__(self , state):
        self.state = []
        for i in range(6) :
            self.state.append([])
            for k in range(7) :
                self.state[i].append(state[i][k]);
    """

    def print_state(self , board):
        for x in range(6, 0, -1):
            for y in range(7, 0, -1):
                print (board[x - 1][y - 1], end=" ")
            print ("\n")
        return


        # best_move -------------------------------------------------------
    
    def best_move (self , state , curr_player):
        if (curr_player == self.color[0]):
            opp_player = self.color[1]
           # self.print_state(state)
        else:
            opp_player = self.color[0]
        children_moves = {}
        
        for i in range(7):
            if (self.is_legal_move(state, i)):
                child = self.move(state, i , curr_player)
                #self.print_state(child)
                children_moves[i] = self.minimax_algo(child , opp_player ,4)
        #self.print_state(state)

        best_move = None
        best_h_value = -9999
        moves = children_moves.items()

        for move , h_value in moves:
            if (best_h_value < h_value):
                best_h_value = h_value
                best_move = move
        #print(best_move)
        return best_move



    #------------------------------------------------------------------
    
    #minimax-----------------------------------------------------------
        
    def minimax_algo (self , state , curr_player , depth):

        if (depth == 0 or self.game_is_over(state)):
            return self.hueristic_value(state, curr_player)
        
        if (curr_player == self.color[0]):
            best_value = -99999
            opp_player= self.color[1]
            for i in range (7):
                if (self.is_legal_move(state, i)):
                    child = self.move(state, i, curr_player)
                 #   self.print_state(child)
                    #print("I AM max PLAYER")
                    v = self.minimax_algo(child , opp_player ,depth-1)
                    best_value = max(best_value , v)

            return best_value
        
        else:
            best_value = 99999
            opp_player = self.color[0]
            for i in range(7):
                if (self.is_legal_move(state, i)):
                    child = self.move(state, i, curr_player)
                  #  self.print_state(child)
                   # print("AM min PLAYER")

                    v = self.minimax_algo(child , opp_player ,depth-1)
                    best_value = min(best_value , v)

            return best_value
                
    #-------------------------------------------------
            
    def is_legal_move (self , state , col):
        for i in range(6):
            if (state[i][col] == '.'):
                return True
        return False
    
    #--------------------------------------------------
    
    def move (self , state , col , color):
        temp = [x[:] for x in state]
        for i in range (6):
            if (temp[i][col] == '.'):
                temp[i][col] = color
                return temp


    #--------------------------------------------------    
    def hueristic_value (self ,state, color):

        four = self.check_num(state , color , 4)
        three = self.check_num(state , color , 3)
        two = self.check_num(state , color , 2)

        if (color == self.color[0]):
            return four*100 + three*10 + two
        else:
            return - four*100 - three*10 - two
    #--------------------------------------------------    
        
    def game_is_over(self ,state ):
        if (self.check_col(self.color[0] ,state) or self.check_raw(self.color[0] ,state) or self.check_diagnol(self.color[0],state)):
            return True
        if (self.check_col(self.color[1] ,state) or self.check_raw(self.color[1] ,state) or self.check_diagnol(self.color[1],state)):
            return True        
        
        return False
          
    #--------------------------------------------------   
    def check_raw(self , color ,state):
        for row in range(6):
            for col in range(4):
                if( state[row][col] == state[row][col+1] == state[row][col+2] == state[row][col+3] == color):
                    return True            
        return False
    
    
    
    def check_col(self, color ,state):
        for row in range(3):
            for col in range(7):
                if( state[row][col] == state[row+1][col] == state[row+2][col] == state[row+3][col] == color ):
                    return True
        return False
    
    
    def check_diagnol(self , color , state):
        for row in range(3):
            for col in range(4):
                if (state[row][col] == state[row+1][col+1] == state[row+2][col+2] == state[row+3][col+3] == color ):
                    return True
            
        for row in range(5,2,-1):
            for col in range(4):
                if (state[row][col] == state[row-1][col+1] == state[row-2][col+2] == state[row-3][col+3] == color ):
                    return True
        return False

    #----------------------------------------------------------


    def check_num(self , state ,color, num):
        count = 0
        for k in range(6):
            for i in range(7):
                if(state[k][i] == color):
                    count += self.check_raw_line(state , k , i ,num)
                    count += self.check_col_line(state, k, i, num)
                    count += self.check_diagonal_line(state, k, i, num)
        return count

    def check_raw_line(self , state ,raw , col , num ):
        count = 0

        for i in range(col , 7):
            if (state[raw][i] == state[raw][col]):
                count = count +1
            else:
                break

        if (count >= num):
            return 1
        else:
            return 0


    def check_col_line(self, state, raw, col, num):
        count = 0

        for i in range(raw, 6):
            if (state[i][col] == state[raw][col]):
                count = count + 1
            else:
                break

        if (count >= num):
            return 1
        else:
            return 0

    def check_diagonal_line(self,state , row, col, num):

        total = 0
        Count = 0
        j = col

        for i in range(row, 6):
            if (j > 6):
                break
            elif (state[i][j] == state[row][col]):
                Count = Count + 1
            else:
                break
            j = j + 1

        if (Count >= num):
            total = total + 1

        Count = 0
        j = col
        for i in range(row, -1, -1):
            if (j > 6):
                break
            elif (state[i][j] == state[row][col]) :
                Count = Count + 1
            else:
                break
            j += 1

        if Count >= num:
            total = total + 1

        return total
