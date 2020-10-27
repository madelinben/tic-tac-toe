def play():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    def printBoard():
        for i in range(len(board)):
            for j in range(len(board[i]) - 2):
                print(board[i][j], '|', board[i][j + 1], '|', board[i][j + 2])
                if i < len(board) - 1:
                    print('---------')

    def checkBoard():
        return False

    finished = False
    playersTurn = True

    while not finished:
        printBoard()

        finished = checkBoard()
        if finished:
            break

        if playersTurn:
            position = input("Player 1: ")
            playersTurn = False
        else:
            position = input("Player 2: ")
            playersTurn = True

    valid = False
    while valid:
        userInput = input("Play again [y/n]").lower()
        if userInput == "y":
            valid = True
            play()
        elif userInput == "n":
            valid = True
            quit()
        else:
            print("Error! Value must be either y/n")


play()
