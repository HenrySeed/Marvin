import utilities
from time import sleep

class Naughts_crosses():
    
    
    def __init__(self):
        self.table = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.occupied = []
        self.game_over = False
        self.winner = None
        
    def leave(self):
        print('\nOkay, we should play again later then')
        self.game_over = True    
        
    def game_help(self):
        print('\n    Enter a number between 1 and 9 to play, type close or quit to leave')    
        
    def move(self, pos, char):   
        
        if pos == 'quit' or pos == 'close': 
            self.leave()
            return None
        
        elif pos == 'help': 
            self.game_help()
            return None        

        
        while pos in self.occupied or pos not in ['1','2','3','4','5','6','7','8','9']:
            
            if pos not in ['1','2','3','4','5','6','7','8','9']:
                print('    Please enter a number between 1 and 9')
                
            elif pos in self.occupied:
                print('    Position already occupied')
                
            pos = input('    > ')
             
                
        pos = int(pos)
           
        self.occupied.append(pos)
        
        if pos < 4:
            self.table[0][pos-1] = char
            
        elif pos >= 4 and pos < 7:
            self.table[1][pos-4] = char
            
        elif pos >= 7 and pos < 10:
            self.table[2][pos-7] = char
    
    
    def __str__(self):
        utilities.clear_w_logo()
        
        pieces = []
        
        for row in self.table:
            for i in row:
                if i == 'X':
                    pieces += ['__  __ ', '\\ \\/ / ', ' \\  /  ', ' /  \\  ', '/_/\\_\\ ']
                elif i == 'O':
                    pieces += ['  ___  ',' / _ \\ ','| | | |','| |_| |',' \___/ ']
                else:
                    pieces += ['       ','       ','       ','       ','       ']
  
        return '''
        +-----------+-----------+-----------+
        |  {0}  |  {5}  |  {10}  |
        |  {1}  |  {6}  |  {11}  |
        |  {2}  |  {7}  |  {12}  |
        |  {3}  |  {8}  |  {13}  |
        |  {4}  |  {9}  |  {14}  |
        |           |           |           |
        +-----------+-----------+-----------+
        |  {15}  |  {20}  |  {25}  |
        |  {16}  |  {21}  |  {26}  |
        |  {17}  |  {22}  |  {27}  |
        |  {18}  |  {23}  |  {28}  |
        |  {19}  |  {24}  |  {29}  |
        |           |           |           |
        +-----------+-----------+-----------+
        |  {30}  |  {35}  |  {40}  |
        |  {31}  |  {36}  |  {41}  |
        |  {32}  |  {37}  |  {42}  |
        |  {33}  |  {38}  |  {43}  |
        |  {34}  |  {39}  |  {44}  |
        |           |           |           |
        +-----------+-----------+-----------+
        
        
        '''.format(pieces[0],pieces[1],pieces[2],pieces[3],pieces[4],pieces[5],
                   pieces[6],pieces[7],pieces[8],pieces[9],pieces[10],pieces[11],
                   pieces[12],pieces[13],pieces[14],pieces[15],pieces[16],pieces[17],
                   pieces[18],pieces[19],pieces[20],pieces[21],pieces[22],pieces[23],
                   pieces[24],pieces[25],pieces[26],pieces[27],pieces[28],pieces[29],
                   pieces[30],pieces[31],pieces[32],pieces[33],pieces[34],pieces[35],
                   pieces[36],pieces[37],pieces[38],pieces[39],pieces[40],pieces[41],
                   pieces[42],pieces[43],pieces[44])
    
    
    def check(self):
        table = self.table
        for row in table:
            if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
                self.game_over = True
                self.winner = row[0]
                print('    ' + self.winner + ' Wins!')
                break
            
        chars = ['X', 'O']
        for col in range(0,3):
            for char in chars:
                if table[0][col] == char and table[1][col] == char and table[2][col] == char:
                    self.game_over = True
                    self.winner = char
                    print('    ' + self.winner + ' Wins!')
                    break 
                
        for char in chars:
            if table[0][0] == char and table[1][1] == char and table[2][2] == char:
                    self.game_over = True
                    self.winner = char
                    print('    ' + self.winner + ' Wins!')
                    break 
            elif table[2][0] == char and table[1][1] == char and table[0][2] == char:
                    self.game_over = True
                    self.winner = char
                    print('    ' + self.winner + ' Wins!')
                    break 
            
            
        
    
def turn(game, char):
        
        choice = input('    ' + char + '\'s Turn\n\n    > ')
           
        if char == 'X': game.move(choice, 'X')
        else: game.move(choice, 'O')    
                   

            
        
def naughtscrosses():
    game = Naughts_crosses()
    utilities.clear_w_logo()
    print(game)
    
    while game.game_over == False:
        turn(game, 'X')
        if game.game_over == False: print(game)
        game.check()
        
        if game.game_over == False:
            turn(game, 'O')
            if game.game_over == False: print(game)  
            game.check()
            