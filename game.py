rows = 6
cols = 7
board = [[0 for _ in range(cols)] for _ in range(rows)]
winner = 0
turn = 1

def print_board():
    for i in range(rows):
        for j in range(cols):
            print(board[i][j], end=" ")
        print()
    print()

def check_cols():
    for i in range(rows):
        for j in range(0, cols-3):
            if ((board[i][j] == 1) and (board[i][j+1] == 1) and (board[i][j+2] == 1) and (board[i][j+3] == 1)):
                return 1
            elif ((board[i][j] == 2) and (board[i][j+1] == 2) and (board[i][j+2] == 2) and (board[i][j+3] == 2)):
                return 2
    return 0

def check_rows():
    for i in range(0, rows-3):
        for j in range(cols):
            if ((board[i][j] == 1) and (board[i+1][j] == 1) and (board[i+2][j] == 1) and (board[i+3][j] == 1)):
                return 1
            elif ((board[i][j] == 2) and (board[i+1][j] == 2) and (board[i+2][j] == 2) and (board[i+3][j] == 2)):
                return 2
    return 0

print_board()

while (winner == 0):
    if (turn == 1):
        player_1 = int(input("Enter your position Player 1: "))

        if ((player_1 < 1) or (player_1 > 7)):
            print("Enter value between 1 and 7.")
            print()
            continue
        else:
            player_1 = player_1 - 1

        for i in range(rows-1, -1, -1):
            if (board[i][player_1] == 0):
                board[i][player_1] = 1
                turn = 2
                break
        
        if (turn == 1):
            print("This column is full, choose another position.")
            print()
            continue
        else:
            print_board()
    
    else:
        player_2 = int(input("Enter your position Player 2: "))

        if ((player_2 < 1) or (player_2 > 7)):
            print("Enter value between 1 and 7")
            print()
            continue
        else:
            player_2 = player_2 - 1
        
        for i in range(rows-1, -1, -1):
            if (board[i][player_2] == 0):
                board[i][player_2] = 2
                turn = 1
                break
        
        if (turn == 2):
            print("This column is full, choose another position.")
            print()
            continue
        else:
            print_board()

    if (check_cols() != 0):
        winner = check_cols()
    elif (check_rows() != 0):
        winner = check_rows()

if (winner == 0):
    print("It is a Draw.")
elif (winner == 1):
    print("Player 1 wins.")
else:
    print("Player 2 wins.")