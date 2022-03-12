boardlist = list() ; selected1 = [] ; selected2 = [] ; e = 0
def check_rows():
    for row in boardlist:
        if turn % 2 == 0:
            if row.count(row[0]) == len(row) and row[0] != 0:
                return True
        elif turn % 2 != 0:
            if row.count(row[0]) == len(row) and row[0] != 0:
                return True

def check_columns():
    for col in range(len(boardlist)):
        check = list()
        for row in boardlist:
            check.append(row[col])
        if turn % 2 == 0:
            if check.count(check[0]) == len(check) and check[0] != 0:
                return True
        elif turn % 2 != 0:
            if check.count(check[0]) == len(check) and check[0] != 0:
                return True
def check_diag():
    diagonal = list()
    for column, row in enumerate(reversed(range(len(boardlist)))):
        diagonal.append(boardlist[row][column])
    if turn % 2 == 0:
        if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] != 0:
            return True
    elif turn % 2 != 0:
        if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] != 0:
            return True

    diagonal = list()
    for u in range(len(boardlist)):
        diagonal.append(boardlist[u][u])
    if turn % 2 == 0:
        if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] != 0:
            return True
    elif turn % 2 != 0:
        if diagonal.count(diagonal[0]) == len(diagonal) and diagonal[0] != 0:
            return True

def check_tie():
    if check_game() != True and len(selected1) + len(selected2) == rowcolumn**2:
        return True

def check_game():
    if check_rows() == True:
        return True
    elif check_columns() == True:
        return True
    elif check_diag() == True:
        return True

def matrix(boardlist):
    for i in boardlist:
        for j in i:
            try:
                if j >= 10:
                    print(j, end='  ')
                else:
                    print("",j, end='  ')
            except TypeError:
                if j == 'X':
                    print("",j, end='  ')
                elif j == 'O':
                    print("",j, end='  ')
        print()

def gameboard(size, rowcolumn):
    increment = 0
    while increment < len(size):
        boardlist.append(size[increment:(increment+rowcolumn)])
        increment += rowcolumn
    matrix(boardlist)
    return boardlist

while e == 0:
    try:
        rowcolumn = int(input("What size game GoPy?"))
        turn = 0

        if rowcolumn <= 0 or rowcolumn == 1:
            print("Please enter a valid number.")
        else:
            size = [i for i in range(rowcolumn**2)]
            gameboard(size,rowcolumn)
            while True:
                try:
                    if e == 1:
                        break
                    elif turn % 2 == 0:
                        Player1move= int(input(("Player 1 turn-->")))
                        if Player1move in selected1:
                            print("You have made this choice before.")
                            turn += 1
                            continue
                        elif Player1move in selected2:
                            print("The other player has made this choice before.")
                            turn += 1
                            continue
                        elif Player1move not in range(rowcolumn**2):
                            print("Please enter a valid number.")
                            turn +=1
                            continue
                        for i in range(rowcolumn):
                            if Player1move in boardlist[i]:
                                for j in range(rowcolumn):
                                    if boardlist[i][j] == Player1move:
                                        selected1.append(Player1move)
                                        selected1.sort()
                                        boardlist[i][j] = 'X'
                        if check_game() == True:
                            print("Winner: X")
                            e += 1
                            break

                        elif check_tie() == True:
                            print("No winner")
                            e += 1
                            break
                        else:
                            matrix(boardlist)
                        turn += 1
                    else:
                        Player2move = int(input("Player 2 turn-->"))
                        if Player2move in selected1:
                            print("The other player has made this choice before.")
                            turn += 1
                            continue
                        elif Player2move in selected2:
                            print("You have made this choice before.")
                            turn += 1
                            continue
                        elif Player2move not in range(rowcolumn**2):
                            print("Please enter a valid number.")
                            turn+=1
                            continue
                        for i in range(rowcolumn):
                            if Player2move in boardlist[i]:
                                for j in range(rowcolumn):
                                    if boardlist[i][j] == Player2move:
                                        selected2.append(Player2move)
                                        selected2.sort()
                                        boardlist[i][j] = 'O'

                        if check_game() == True:
                            print("Winner: O")
                            e += 1
                            break
                        elif check_tie() == True:
                            print("No winner")
                            e += 1
                            break
                        else:
                            matrix(boardlist)
                        turn+=1
                except ValueError:
                    print("You cannot input that.")
    except ValueError:
        print("You must enter an integer.")

