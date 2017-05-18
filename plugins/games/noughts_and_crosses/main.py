import time
import sys
import os

class Naughts_crosses():

    def __init__(self):
        self.table = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        self.occupied = []
        self.game_over = False
        self.winner = None


    def move(self, pos, char):

        while pos in self.occupied:
            print('    Position already occupied')
            pos = int(input('    > '))

        else:
            self.occupied.append(pos)

            if pos < 4:
                self.table[0][pos-1] = char

            elif pos >= 4 and pos < 7:
                self.table[1][pos-4] = char

            elif pos >= 7 and pos < 10:
                self.table[2][pos-7] = char


    def __str__(self):
        clear()
        bar = '    +---+---+---+\n'
        board = '\n' + bar
        for line in self.table:
            board += '    | {0} | {1} | {2} |\n'.format(line[0], line[1], line[2])
            board += bar
        return board


    def check(self):
        table = self.table
        for row in table:
            if row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
                self.game_over = True
                self.winner = row[0]
                print('    ' + self.winner + ' Wins!')
                time.sleep(1)
                break

        chars = ['X', 'O']
        for col in range(0,3):
            for char in chars:
                if table[0][col] == char and table[1][col] == char and table[2][col] == char:
                    self.game_over = True
                    self.winner = char
                    print('    ' + self.winner + ' Wins!')
                    time.sleep(1)
                    break

        for char in chars:
            if table[0][0] == char and table[1][1] == char and table[2][2] == char:
                    self.game_over = True
                    self.winner = char
                    print('    ' + self.winner + ' Wins!')
                    time.sleep(1)
                    break
            elif table[2][0] == char and table[1][1] == char and table[0][2] == char:
                    self.game_over = True
                    self.winner = char
                    print('    ' + self.winner + ' Wins!')
                    time.sleep(1)
                    break



def clear():
    if sys.stdin.isatty():
        os.system('clear')


def leave():
    return None

def game_help():
    print('    Enter a number between 1 and 9 to play, type close or quit to leave')

def turn(self, char):


    commands = {'quit': leave,
                'close': leave,
                'help': game_help
                }

    choice = input('    ' + char + '\'s Turn\n\n    > ')

    if choice == 'quit' or choice == 'close':
        self.game_over = True
        print('Exiting game')
        time.sleep(1)
        return None

    elif choice == 'help':
        game_help()

    else:
        try:
            choice = int(choice)
            if char == 'X':
                self.move(choice, 'X')
            else:
                self.move(choice, 'O')

        except:
            print('\n    Please enter a valid number between 1 and 9\n')
            print(self)
            turn(self, char)



def naughtscrosses():
    game = Naughts_crosses()
    print(game)

    while game.game_over == False:
        turn(game, 'X')
        print(game)
        game.check()

        if game.game_over == False:
            turn(game, 'O')
            print(game)
            game.check()

naughtscrosses()
