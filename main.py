def play():
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']

    def printBoard():
        print(board[0], '|', board[1], '|', board[2])
        print('---------')
        print(board[3], '|', board[4], '|', board[5])
        print('---------')
        print(board[6], '|', board[7], '|', board[8])

    def checkBoard():
        return False

    def placeCounter(player):
        while True:
            pos = int(input(player + ": "))-1
            if board[pos] == "X" or board[pos] == "O":
                print("Error! Position already contains a counter")
            elif (pos < 0) or (pos > 8):
                print("Error! Position value must be between 1 and 9")
            else:
                break

        if player == "Player 1":
            board[pos] = "X"
        else:
            board[pos] = "O"

    finished = False
    playersTurn = True

    while not finished:
        printBoard()

        finished = checkBoard()
        if finished:
            break

        if playersTurn:
            placeCounter("Player 1")
            playersTurn = False
        else:
            placeCounter("Player 2")
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
