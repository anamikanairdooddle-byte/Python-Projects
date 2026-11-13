
def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        print("---------")


def check_winner(board, mark):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for line in wins:
        if board[line[0]] == mark and board[line[1]] == mark and board[line[2]] == mark:
            return True

    return False


def play_game():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = 1
    mark = "X"
    moves = 0

    while moves < 9:
        display_board(board)
        print("Player", player, "-", mark)

        position = input("Choose a cell (1-9): ").strip()

        if not position.isdigit():
            print("Enter a valid number")
            continue

        position = int(position)

        if position < 1 or position > 9:
            print("Choose a number from 1 to 9")
            continue

        if board[position - 1] in ["X", "O"]:
            print("Cell already occupied")
            continue

        board[position - 1] = mark
        moves += 1

        if check_winner(board, mark):
            display_board(board)
            print("Player", player, "wins!")
            return

        if player == 1:
            player = 2
            mark = "O"
        else:
            player = 1
            mark = "X"

    display_board(board)
    print("Game is a draw!")


while True:
    print("\nTIC TAC TOE")
    print("Player 1: X | Player 2: O")

    play_game()

    answer = input("Play again? (yes/no): ").strip().lower()

    if answer != "yes":
        print("Thank you for playing!")
        break
