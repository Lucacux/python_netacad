import random

def main():
    board = initialize_board()
    print_board(board)
    
    while True:
        user_pos = user_input(board)
        board[user_pos] = 'O'
        print_board(board)
        if check_winner(board, 'O'):
            print("You won!")
            break
        
        comp_pos = computer_move(board)
        if comp_pos is None:
            print("It's a draw!")
            break
        board[comp_pos] = 'X'
        print_board(board)
        if check_winner(board, 'X'):
            print("The machine won!")
            break

def print_board(board):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print(f"|   {board[i*3]}   |   {board[i*3+1]}   |   {board[i*3+2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def initialize_board():
    return [str(i) for i in range(1, 10)]

def user_input(board):
    while True:
        try:
            number = int(input("Enter your move (1-9): "))
            if 1 <= number <= 9 and board[number - 1] not in ['X', 'O']:
                return number - 1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def computer_move(board):
    empty_cells = [i for i in range(9) if board[i] not in ['X', 'O']]
    return random.choice(empty_cells) if empty_cells else None

def check_winner(board, player):
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

if __name__ == "__main__":
    main()
