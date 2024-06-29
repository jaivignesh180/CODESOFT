board = [' ' for _ in range(9)]

def print_board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_win(letter):
    
    for i in range(0, 7, 3):
        if board[i] == letter and board[i+1] == letter and board[i+2] == letter:
            return True
 
    for i in range(3):
        if board[i] == letter and board[i+3] == letter and board[i+6] == letter:
            return True

    if board[0] == letter and board[4] == letter and board[8] == letter:
        return True
    if board[2] == letter and board[4] == letter and board[6] == letter:
        return True
    return False

def check_draw():
    return ' ' not in board

def player_move(letter):
    while True:
        move = input("Player " + letter + ", enter your move (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if board[move - 1] == ' ':
                    board[move - 1] = letter
                    break
                else:
                    print("That space is already occupied!")
            else:
                print("Please enter a number between 1 and 9!")
        except:
            print("Invalid input!")

def ai_move():
    best_score = -1000
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(0, False, -1000, 1000)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

def minimax(depth, is_maximizing, alpha, beta):
    if check_win('X'):
        return -10
    elif check_win('O'):
        return 10
    elif check_draw():
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(depth + 1, False, alpha, beta)
                board[i] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(depth + 1, True, alpha, beta)
                board[i] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def play_game():
    print_board()
    while True:
        player_move('X')
        print_board()
        if check_win('X'):
            print("Player X wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break
        ai_move()
        print_board()
        if check_win('O'):
            print("AI wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break

play_game()