import numpy as np
#---------------------------------------
class TTT():
   def __init__(self):
      self.is_on=True
      print('Welcome to Tic-Tac-Tow Game !!!')
      self.board_status = np.zeros(shape=(3, 3))
      # create array [0,0,0]
      #              [0,0,0]
      #              [0,0,0]
      print('Board coordianates: \n [1,2,3] \n [4,5,6] \n [7,8,9] \n')
      self.player_X_turns = True
      self.player_X_starts = True
      self.reset_board = False
      self.gameover = False
      self.tie = False
      self.O_win = False
      self.X_win = False

      self.X_score = 0
      self.O_score = 0
      self.tie_score = 0

      while self.is_on:
        self.players()

#----------------Players-----------------------------
   def players(self):
       grid=[0,0]
       if not self.reset_board:
         if self.player_X_turns:
                current_player='Player1'
         else:
             current_player = 'Player2'
         player_input = input(f"{current_player} picks yor coordinate(1-9):")

         if player_input =='1':
             grid[0]=0
             grid[1]=0
             self.checking(grid)
         elif player_input =='2':
             grid[0] = 0
             grid[1] = 1
             self.checking(grid)
         elif player_input =='3':
             grid[0] = 0
             grid[1] = 2
             self.checking(grid)
         elif player_input =='4':
             grid[0] = 1
             grid[1] = 0
             self.checking(grid)
         elif player_input =='5':
             grid[0] = 1
             grid[1] = 1
             self.checking(grid)
         elif player_input =='6':
             grid[0] = 1
             grid[1] = 2
             self.checking(grid)
         elif player_input =='7':
             grid[0] = 2
             grid[1] = 0
             self.checking(grid)
         elif player_input =='8':
             grid[0] = 2
             grid[1] = 1
             self.checking(grid)
         elif player_input =='9':
             grid[0] = 2
             grid[1] = 2
             self.checking(grid)

       else:  # Play Again
            self.play_again()
            self.reset_board = False

   def checking(self,grid):
         if self.player_X_turns:
             if not self.is_grid_occupied(grid):
                 self.board_status[grid[0]][grid[1]] = 1
                 self.player_X_turns = not self.player_X_turns
                 print(self.board_status)
             else:
                 print('The position has been taken')
         else:
             if not self.is_grid_occupied(grid):
                 self.board_status[grid[0]][grid[1]] = -1
                 self.player_X_turns = not self.player_X_turns
                 print(self.board_status)
             else:
                 print('The position has been taken')

             # Check if game is concluded
         if self.is_gameover():
             self.display_gameover()

   def is_grid_occupied(self, grid):
       if self.board_status[grid[0]][grid[1]] == 0:
           return False
       else:
           return True
#----------------Game mechanic-----------------------

   def is_winner(self,player):
       if player == 'X':
          player= 1
       else:
          player= -1

       for i in range(0,3):
           if self.board_status[0][i]==self.board_status[1][i]==self.board_status[2][i]==player:
               return True
           if self.board_status[i][0]==self.board_status[i][1]==self.board_status[i][2]==player:
               return True

       if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2]==player:
           return True
       if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0]==player:
           return True
       else:
           return False

   def is_tie(self):
       r,c = np.where(self.board_status==0)
       tie = False
       if len(r)==0:
           tie = True
       return tie

   def is_gameover(self):
       self.X_win = self.is_winner('X')
       if not self.X_win:
           self.O_win = self.is_winner('O')
       if not self.O_win:
           self.tie = self.is_tie()

       gameover = self.O_win or self.X_win or self.tie

       if self.X_win:
           print('X wins!!')
       if self.O_win:
           print('O wins!!')
       if self.tie:
           print('Tie!!!')

       return gameover
#---------------Reset-----------------------------
   def play_again(self):
       self.player_X_starts = True
       self.player_X_turns = self.player_X_starts
       self.board_status = np.zeros(shape=(3, 3))

#----------------Result---------------------------
   def display_gameover(self):

        if self.X_win:
            self.X_score += 1
            print('Winner: Player 1 (X)')

        elif self.O_win:
            self.O_score += 1
            print('Winner: Player 2 (O)')

        else:
            self.tie_score += 1
            print('Its a tie')

        print(f'Player 1 (X) : {self.X_score}' + '\n')
        print(f'Player 2 (O) : {self.O_score}' + '\n')
        print(f'Tie          : {self.tie_score}' + '\n')

        play_again = input("Do you want to play again (y/n): ")
        if play_again == 'y':
            self.reset_board = True
        else :
            self.is_on=False
#-----------------------------------------------------
TTT()
