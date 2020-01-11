import random                  # I want 'random' so I can randomize the AI's choices
                               # whenever it cant win or 'intercept' the player
board_tiles = ['-', '-', '-',
               '-', '-', '-',          # Here I declare some variables globaly
               '-', '-', '-']          # so i can use them later
board_rows = ''
board_columns = ''
board_diagonals = ''
board_layout = ''
def board_update():
    global board_rows, board_columns, board_diagonals, board_layout      # In this function I update the variables above
    board_rows = [(board_tiles[0], board_tiles[1], board_tiles[2]),      # this is called all the time in the program so
                  (board_tiles[3], board_tiles[4], board_tiles[5]),      # that the game knows exactly how is the board
                  (board_tiles[6], board_tiles[7], board_tiles[8])]      # at all times
    board_columns = [(board_tiles[0], board_tiles[3], board_tiles[6]),
                     (board_tiles[1], board_tiles[4], board_tiles[7]),
                     (board_tiles[2], board_tiles[5], board_tiles[8])]
    board_diagonals = [(board_tiles[0], board_tiles[4], board_tiles[8]),
                       (board_tiles[2], board_tiles[4], board_tiles[6])]
    board_layout = ''' {} | {} | {}
 {} | {} | {}
 {} | {} | {}'''.format(board_tiles[0], board_tiles[1], board_tiles[2], board_tiles[3], board_tiles[4],
                           board_tiles[5], board_tiles[6], board_tiles[7], board_tiles[8])
def board_display():
    board_update()            # Here I make a function to display the board
    print('-----------')      # I declare it because it's used a lot
    print(board_layout)

def check_if_tie():
    board_update()
    if '-' not in board_tiles and check_winner() is None:     # These two functions are needed to check if the game tied
        return True                                           # or if there is a winner, and if there is, if it's the AI
    else:                                                     # or the player. The 'tie' one can either return True or
        return False                                          # False, and the 'winner' one can return 'X' or 'O'
                                                              # depending on which won the game
def check_winner():                                           # ('X' being the player and 'O' being the AI)
    board_update()
    for i in board_rows + board_columns + board_diagonals:
        if i.count('X') == 3:
            return 'X'
        elif i.count('O') == 3:
            return 'O'
    return None

def player_turn():
    board_update()                                                       # In this function I get the input from the
    selected_tile = int(input('Select a tile (1 - 9): ')) - 1            # player in the form of a number (1 - 9),
    while board_tiles[selected_tile] != '-':                             # the numbers refer to the tiles on the board
        selected_tile = int(input('Insert another tile (1 - 9): ')) - 1  # as seen on the right:        1 | 2 | 3
    board_tiles[selected_tile] = 'X'                                     # There's a section that       4 | 5 | 6
                                                                         # checks if the input is       7 | 8 | 9
def ai_tile():                                                           # valid (if the tile is already occupied)
    intercept_tile = 0
    win_tile = 0
    for row in board_rows:
        if row.count('O') == 2 and row.count('X') == 0:           # This function is needed so the AI can know where
            for i in row:                                         # to place it's tile, his decision can be:
                if i == '-':                                      # - To end the game if it's possible.
                    return win_tile                               # - To 'intercept' the player from winning.
                win_tile += 1                                     # - To randomly select a tile.
        win_tile += 3                                             # (this is the hierarchy of it's decisions, meaning
    win_tile = 0                                                  #  that the AI will prefer to win the game over
    for column in board_columns:                                  #  intercepting the player or playing randomly)
        if column.count('O') == 2 and column.count('X') == 0:
            for i in column:                                      # The function checks for a row, column or diagonal
                if i == '-':                                      # that either has 2 'O' and no 'X' or for one that
                    return win_tile                               # has 2 'X' and no 'O', so that it can either 'win'
                win_tile += 3                                     # or intercept the player from winning, if none
        win_tile += 1                                             # meets this condition, then it picks a tile randomly
    win_tile = 0
    x = 4                                                         # The 'x' variable that is local to this function is
    for diagonal in board_diagonals:                              # used to keep track of the tile in which the AI has
        if diagonal.count('O') == 2 and diagonal.count('X') == 0: # to win or intercept the player in diagonals, my
            for i in diagonal:                                    # idea was that for each diagonal, the number of tiles
                if i == '-':                                      # that are needed to be skipped are different
                    return win_tile                               # (in the first iteration of the loop 'x' is 4, meaning
                win_tile += x                                     # that the tiles jump from 1 to 5 to 9, in the second
        x -= 2                                                    # iteration, 'x' is 2, then the tiles jump from 3 to 5
        win_tile += x                                             # to 7, 1 - 5 - 9 and 3 - 5 - 7 being the diagonals)

    for row in board_rows:
        if row.count('X') == 2 and row.count('O') == 0:
            for i in row:
                if i == '-':
                    return intercept_tile
                intercept_tile += 1
        intercept_tile += 3
    intercept_tile = 0
    for column in board_columns:
        if column.count('X') == 2 and column.count('O') == 0:
            for i in column:
                if i == '-':
                    return intercept_tile
                intercept_tile += 3
        intercept_tile += 1
    intercept_tile = 0
    x = 4
    for diagonal in board_diagonals:
        if diagonal.count('X') == 2 and diagonal.count('O') == 0:
            for i in diagonal:
                if i == '-':
                    return intercept_tile
                intercept_tile += x
        x -= 2
        intercept_tile += x
    random_tile = random.randint(0, 8)
    while board_tiles[random_tile] != '-':         # Here it decides to randomly choose a tile.
        random_tile = random.randint(0, 8)
    return random_tile

def ai_turn():                                     # In this funcion, I did all the aesthetics of the ai turn
    board_update()                                 # like printing which tile it chose and everything
    print('-----------')                           # 'ai_tile()' is used here, and it returns the tile that
    ai_choice = ai_tile()                          # the AI picked.
    board_tiles[ai_choice] = 'O'
    print('AI chooses tile {}'.format(ai_choice + 1))
def game():
    while check_winner() is None and check_if_tie() is False:
        board_display()                                          # This function is the main one, it checks if
        player_turn()                                            # the game is over, sequences the turns,
        if check_winner() is None and check_if_tie() is False:   # displays the board and announces the winner.
            ai_turn()
        else:
            break
    if check_winner() is 'X':
        board_display()
        print('The player won!')
        print('-----------')
    else:
        board_display()
        print('The AI won!')
        print('-----------')
game()