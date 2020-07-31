c = list("_________")

print("--------- \n" + '| ' + c[0] + ' ' + c[1] + ' ' + c[2] + ' |\n'
      + '| ' + c[3] + ' ' + c[4] + ' ' + c[5] + ' |\n'
      + '| ' + c[6] + ' ' + c[7] + ' ' + c[8] + ' |\n'
      + "---------")

coordinates = ["13", "23", "33", "12", "22", "32", "11", "21", "31"]

counter_moves = 0


flag = True
while flag == True:
    cells = [c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]]
    move = input("Enter the coordinates: > ").split()
    for char in move:
        if not char.isdigit():
            print("You should enter numbers!")
            break
        else:
            first = int(move[0])
            second = int(move[1])
            if first > 3 or second > 3:
                print("Coordinates should be from 1 to 3!")
                break
            else:
                coord = move[0] + move[1]
                index = coordinates.index(coord)
                if cells[index] == "_":
                    if counter_moves == 0:
                        c[index] = "X"
                        counter_moves = 1
                        print("--------- \n" + '| ' + c[0] + ' ' + c[1] + ' ' + c[2] + ' |\n'
                              + '| ' + c[3] + ' ' + c[4] + ' ' + c[5] + ' |\n'
                              + '| ' + c[6] + ' ' + c[7] + ' ' + c[8] + ' |\n'
                              + "---------")
                    else:
                        c[index] = "O"
                        counter_moves = 0
                        print("--------- \n" + '| ' + c[0] + ' ' + c[1] + ' ' + c[2] + ' |\n'
                          + '| ' + c[3] + ' ' + c[4] + ' ' + c[5] + ' |\n'
                          + '| ' + c[6] + ' ' + c[7] + ' ' + c[8] + ' |\n'
                          + "---------")
                    cells = [c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8]]
                    rows = [[c[0], c[1], c[2]], [c[3], c[4], c[5]], [c[6], c[7], c[8]], [c[0], c[3], c[6]],
                            [c[1], c[4], c[7]], [c[2], c[5], c[8]],
                            [c[0], c[4], c[8]], [c[2], c[4], c[6]]]
                    countx = 0  # flag for win
                    countX = 0  # counter for X's in the c input
                    counto = 0
                    countO = 0
                    countdraw = 0
                    empty = 0
                    for row in rows:
                        if row == ["X", "X", "X"]:
                            countx += 1
                            countdraw += 1
                        elif row == ["O", "O", "O"]:
                            counto += 1
                            countdraw += 1
                        for i in row:
                            if i == "_":
                                empty += 1

                    for c_ in cells:
                        if c_ == "X":
                            countX += 1
                        elif c_ == "O":
                            countO += 1

                    if (countx == 1 and counto == 1) or ((abs(countX - countO)) > 1):
                        print("Impossible")
                        flag = False
                    elif countdraw == 0 and empty == 0:
                        print("Draw")
                        flag = False
                    elif countx == 1:
                        print("X wins")
                        flag = False
                    elif counto == 1:
                        print("O wins")
                        flag = False
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    break
