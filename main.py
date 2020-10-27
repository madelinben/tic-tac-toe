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
        winCombo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for i in winCombo:
            if board[i[0]] == board[i[1]] == board[i[2]] == "X":
                print("Congratulations! Player 1 Wins!")
                return True
            elif board[i[0]] == board[i[1]] == board[i[2]] == "O":
                print("Congratulations! Player 2 Wins!")
                return True

        count = 0
        for j in range(9):
            if board[j] == "X" or board[j] == "O":
                count += 1
            if count == 9:
                print("Tie!")
                return True

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
    while not valid:
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
