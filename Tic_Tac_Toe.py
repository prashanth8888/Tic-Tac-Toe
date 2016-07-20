# @ Author : Prashanth
# Build    : Python V3.4
# Date     : 16-May-2016
# Description: Tic-Tac-Toe Game


import itertools


class Tic__Tac_Toe():

    li = [[None] * 3, [None] * 3, [None] * 3]
    error = None
    count = 0
    breaker = False
    x_winner = False
    o_winner = False


    def __init__(self, **kwargs):
        self.variables = kwargs

    def initliaze(self):
        global li
        li = [[None] * 3, [None] * 3, [None] * 3]

    def experiment(self):
        global li
        li[0][0] = 'X'
        li[0][1] = '0'

    def display(self):
        global li
        for items in li:
            print(items)

    def game_over_check(self, y, player_value):
        global li

        if li[0][y] == li[1][y] == li[2][y] == player_value:
            return True

        elif li[0][0] == li[1][1] == li[2][2] == player_value:
            return True

        elif li[0][2] == li[1][1] == li[2][0] == player_value:
            return True

        else:
            return False

    def game_over_check1(self, x, player_value):
        global li

        if li[x][0] == li[x][1] == li[x][2] == player_value:
            return True

        elif li[0][0] == li[1][1] == li[2][2] == player_value:
            return True

        elif li[0][2] == li[1][1] == li[2][0] == player_value:
            return True

        else:
            return False

    def draw_board(self, x=0):

        for i in range(x, 9):
            curr_pos = i
            check_game = self.check_and_proceed()
            if check_game is False:
                valuer = self.swap_players(i)
                row = input('Enter the Row position')
                check_input = self.validate_input(row, i)
                if check_input is True:
                    row = int(row)
                col = input('Enter the Column Position')
                check_input = self.validate_input(col, i)
                if check_input is True:
                    col = int(col)
                handbarrow = self.add_value(row, col, valuer)
                if handbarrow is 'type1':
                    self.draw_board(curr_pos)
                if handbarrow is None:
                    self.display()
            else:
                self.draw_board()


    def check_and_proceed(self):
        global li, breaker, x_winner, o_winner
        try:
            for x in range(0, 3):
                x_winner = self.game_over_check1(x, 'X')
                o_winner = self.game_over_check1(x, 'O')
                if x_winner or o_winner is True:
                    raise AssertionError

        except AssertionError:
            pass



        if x_winner is False and o_winner is False:
            try:
                for y in range(0, 3):
                    x_winner = self.game_over_check(y, 'X')
                    o_winner = self.game_over_check(y, 'O')
                    if x_winner or o_winner is True:
                        raise AssertionError
            except AssertionError:
                pass

        if x_winner is True:
                        print("The Game is Over")
                        print("Player X wins the Game!")
                        self.display()
                        print("Resetting for a new board")
                        self.initliaze()
                        self.display()
                        return True

        elif o_winner is True:
                        print("The Game is Over")
                        print("Player O wins the Game!")
                        self.display()
                        print("Resetting for a new board")
                        self.initliaze()
                        self.display()
                        return True

        elif x_winner is False and o_winner is False:
                        check_game_over = self.board_full_check()
                        if check_game_over is True:
                            print("The Game is Over")
                            print("The Game is Drawn, Well played both of you!")
                            self.display()
                            print("Resetting for a new board")
                            self.initliaze()
                            self.display()
                        else:
                            return False
        else:
                        return False

    def board_full_check(self):
        global li
        count = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if (li[i][j] == 'X') or (li[i][j] == 'O'):
                    count += 1
        if count == 9:
            return True
        else:
            return False


    def swap_players(self, i):

            if i % 2 == 0:
                print("Player X turn to Play")
                value = 'X'
                return value
            else:
                print("Player O turn to Play")
                value = 'O'
                return value



    def validate_input(self, val, position):
        try:
            val = int(val)
        except ValueError:
            print("The Entered Value is not an Integer")
            self.draw_board(position)

        if 0 <= int(val) <= 2:
            return True
        else:
            print("The Number is not in between the positions 0,1 and 2")
            self.draw_board(position)

    def add_value(self, row, col, value):
        global li

        if li[row][col] is not None:
            print("Already a value exists in the position")
            error = 'type1'
            return error

        elif li[row][col] is None:
            li[row][col] = value
            error = None
            return error
        else:
            error = 'type2'
            return error


def main():

    ttt_obj = Tic__Tac_Toe()
    ttt_obj.initliaze()
    ttt_obj.display()
    ttt_obj.draw_board()


if __name__ == "__main__": main()



