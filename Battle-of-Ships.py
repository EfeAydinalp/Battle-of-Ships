import os
import sys

letters = ['A','B','C','D','E','F','G','H','I','J']
letterDict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}

numbers = ['1','2','3','4','5','6','7','8','9']

IOerror_Output =[]

#Checks IO Error

try:
    with open(sys.argv[1]) as inp:
        shipsPlayer_1 = list(inp.read().split())
except IOError:
    IOerror_Output.append(sys.argv[1])

try:
    with open(sys.argv[2]) as inp:
        shipsPlayer_2 = list(inp.read().split())
except IOError:
    IOerror_Output.append(sys.argv[2])

try:
    with open(sys.argv[3]) as inp:
        player1_in = list(inp.read().split())
except IOError:
    IOerror_Output.append(sys.argv[3])

try:
    with open(sys.argv[4]) as inp:
        player2_in = list(inp.read().split())
except IOError:
    IOerror_Output.append(sys.argv[4])

if len(IOerror_Output) > 0 :
    ostr =""

    for i in range(len(IOerror_Output)):
        ostr += IOerror_Output[i]+" "
    print("“IOError: input file(s) " + ostr + "are not reachable.")

    exit()
##################################################################################################################

#Opens Player1.txt and read ships positions.

"""
 with open(sys.argv[1]) as inp:
    shipsPlayer_1 = list(inp.read().split())

"""

for i in range (len(shipsPlayer_1)):
    counter = 0
    for j in range(len(shipsPlayer_1[i])):
        try:
            if shipsPlayer_1[i][j] in ["P" , "B" , "C" , "S" , "D"]:
                counter +=1
                if counter == 2:
                    counter = 1
                    shipsPlayer_1[i]= shipsPlayer_1[i][:j-1]+shipsPlayer_1[i][j:]
        except:
            continue
    shipsPlayer_1[i] = shipsPlayer_1[i].replace(";","-")


#Opens Player2.txt and read ships positions.

"""
with open(sys.argv[2]) as inp:
    shipsPlayer_2 = list(inp.read().split())

"""

for i in range (len(shipsPlayer_2)):
    counter = 0
    for j in range(len(shipsPlayer_2[i])):
        try:
            if shipsPlayer_2[i][j] in ["P" , "B" , "C" , "S" , "D"]:
                counter +=1
                if counter == 2:
                    counter = 1
                    shipsPlayer_2[i]= shipsPlayer_2[i][:j-1]+shipsPlayer_2[i][j:]
        except:
            continue
    shipsPlayer_2[i] = shipsPlayer_2[i].replace(";","-")

##################################################################################################################

#Works just like print_hiddenBoard() but ship names included.

def finalOutput():
    print("Player1’s Board","      Player2’s Board")
    print('  A B C D E F G H I J' , '     A B C D E F G H I J')

    x = 1
    for i in range (10):
        if x == 10:
            print(str(x) + " ".join(shipsPlayer_1 [i]) , "  " ,str(x) +" ".join(shipsPlayer_2 [i]) )
        else:        
            print (x," ".join(shipsPlayer_1[i]) , "  ",  x," ".join(shipsPlayer_2[i]) )
            x += 1
    print('\n')
finalOutput()

print('\n')

##################################################################################################################

#Creates hidden boards and print them as game matrix.

hiddenBoard_Player1 = []
hiddenBoard_Player2 = []

for i in range(10):
    hiddenBoard_Player1.append(["-"]*10)
    hiddenBoard_Player2.append(["-"]*10)

def print_hiddenBoard():
    
    print("Player1’s Hidden Board","    Player2’s Hidden Board")
    print('  A B C D E F G H I J','     A B C D E F G H I J')

    x = 1
    for i in range (10):
        if x == 10:
            print(str(x) + " ".join(hiddenBoard_Player1 [i]) , "  " ,str(x) +" ".join(hiddenBoard_Player2 [i]) , "\n")
        else:        
            print (x," ".join(hiddenBoard_Player1[i]) , "  ",  x," ".join(hiddenBoard_Player2[i]) )
            x += 1

##################################################################################################################

#Opens OptionalPlayer 1-2 txt files and read them for checking status of ships

with open("OptionalPlayer1.txt") as inp:
    OptionalPlayer_1 = list(inp.read().split())

with open("OptionalPlayer2.txt") as inp:
    OptionalPlayer_2 = list(inp.read().split())

B1_Player1 = []
B2_Player1 = []
P1_Player1 = []
P2_Player1 = []
P3_Player1 = []
P4_Player1 = []

OptionalShips_Player1 = [B1_Player1,B2_Player1,P1_Player1,P2_Player1,P3_Player1,P4_Player1]

B1_Player2 = []
B2_Player2 = []
P1_Player2 = []
P2_Player2 = []
P3_Player2 = []
P4_Player2 = []

OptionalShips_Player2 = [B1_Player2,B2_Player2,P1_Player2,P2_Player2,P3_Player2,P4_Player2]

status_Player1 = []
status_Player2 = []

def pull_OptionalShips(OptionalPlayer,OptionalShips):

    global letters

    j = 0

    for i in OptionalPlayer:
        shipType = i[0]
        orientation = i.split(";")[1]
        coorLetter = i.split(";")[0].split(",")[1]
        coorNumber = int(i.split(";")[0].split(",")[0].split(":")[1])

        if shipType == 'B':
            if orientation == 'right':
                for k in range (4):
                    OptionalShips[j].append([coorNumber-1,letters.index(coorLetter)+k])
            elif orientation == 'down':
                for k in range (4):
                    OptionalShips[j].append([coorNumber-1+k,letters.index(coorLetter)])

        if shipType == 'P':
            if orientation == 'right':
                for k in range (2):
                    OptionalShips[j].append([coorNumber-1,letters.index(coorLetter)+k])
            elif orientation == 'down':
                for k in range (2):
                    OptionalShips[j].append([coorNumber-1+k,letters.index(coorLetter)])

        j += 1

pull_OptionalShips(OptionalPlayer_1,OptionalShips_Player1)
pull_OptionalShips(OptionalPlayer_2,OptionalShips_Player2)

Carrier_1 = []
Battleship_1 = []
Destroyer_1 = []
Submarine_1 = []
Patrol_Boat_1 = []

allShips_Player1 = [Carrier_1,Battleship_1,Destroyer_1,Submarine_1,Patrol_Boat_1]

Carrier_2 = []
Battleship_2 = []
Destroyer_2 = []
Submarine_2 = []
Patrol_Boat_2 = []

allShips_Player2 = [Carrier_2,Battleship_2,Destroyer_2,Submarine_2,Patrol_Boat_2]

#Uses optional ships and check optional ships coordinates to find status of ships.
#For ships which is not in optional ships, just count them in matrix and when count number is zero than understands that type of ship sink.

def status_of_Ships(shipsPlayer,OptionalShips,hiddenBoard,Status,allShips):

    allShips[0].clear()
    allShips[1].clear()
    allShips[2].clear()
    allShips[3].clear()
    allShips[4].clear()

    C_counter = 0
    S_counter = 0
    D_counter = 0

    for i in shipsPlayer:
        if (i.count('C')) == 1 :
            C_counter += 1
        else :
            C_counter += i.count('C')

    for i in shipsPlayer:
        if (i.count('S')) == 1 :
            S_counter += 1
        else:
            S_counter += i.count('S')
 
    for i in shipsPlayer:
        if (i.count('D')) == 1 :
            D_counter += 1
        else:
            D_counter += i.count('D')

    if C_counter == 0:
        allShips[0].append('X') 
    else:
        allShips[0].append('-')

    if S_counter == 0:
        allShips[3].append('X')
    else:
        allShips[3].append('-')

    if D_counter == 0:
        allShips[2].append('X')
    else:
        allShips[2].append('-')

    xCounter = 0

    if hiddenBoard[OptionalShips[0][0][0]][OptionalShips[0][0][1]] == 'X' and hiddenBoard[OptionalShips[0][1][0]][OptionalShips[0][1][1]] == 'X' and hiddenBoard[OptionalShips[0][2][0]][OptionalShips[0][2][1]] == 'X' and hiddenBoard[OptionalShips[0][3][0]][OptionalShips[0][3][1]] == 'X':
        xCounter += 1

    if hiddenBoard[OptionalShips[1][0][0]][OptionalShips[1][0][1]] == 'X' and hiddenBoard[OptionalShips[1][1][0]][OptionalShips[1][1][1]] == 'X' and hiddenBoard[OptionalShips[1][2][0]][OptionalShips[1][2][1]] == 'X' and hiddenBoard[OptionalShips[1][3][0]][OptionalShips[1][3][1]] == 'X':
         xCounter += 1

    allShips[1].append('X ' * xCounter + '- ' * (2-xCounter))

    xCounter = 0

    if hiddenBoard[OptionalShips[2][0][0]][OptionalShips[2][0][1]] == 'X' and hiddenBoard[OptionalShips[2][1][0]][OptionalShips[2][1][1]] == 'X':
        xCounter += 1
    if hiddenBoard[OptionalShips[3][0][0]][OptionalShips[3][0][1]] == 'X' and hiddenBoard[OptionalShips[3][1][0]][OptionalShips[3][1][1]] == 'X':
        xCounter += 1
    if hiddenBoard[OptionalShips[4][0][0]][OptionalShips[4][0][1]] == 'X' and hiddenBoard[OptionalShips[4][1][0]][OptionalShips[4][1][1]] == 'X':
        xCounter += 1
    if hiddenBoard[OptionalShips[5][0][0]][OptionalShips[5][0][1]] == 'X' and hiddenBoard[OptionalShips[5][1][0]][OptionalShips[5][1][1]] == 'X':
        xCounter += 1

    allShips[4].append('X ' * xCounter + '- ' * (4-xCounter))

    Status.append(allShips[0])
    Status.append(allShips[1])
    Status.append(allShips[2])
    Status.append(allShips[3])
    Status.append(allShips[4])
    
status_of_Ships(shipsPlayer_1,OptionalShips_Player1,hiddenBoard_Player1,status_Player1,allShips_Player1)

status_of_Ships(shipsPlayer_2,OptionalShips_Player2,hiddenBoard_Player2,status_Player2,allShips_Player2)

#Just print status of players but make them more cosmetic :) .

def printStatus():
    
    print("Carrier " , status_Player1[0][0] , "\t\t\t Carrier " , status_Player2[0][0])
    print("Battleship " , status_Player1[1][0] , "\t\t Battleship " , status_Player2[1][0])
    print("Destroyer " , status_Player1[2][0], "\t\t\t Destroyer " , status_Player2[2][0])
    print("Submarine " , status_Player1[3][0], "\t\t\t Submarine " , status_Player2[3][0])
    print("Patrol Boat " , status_Player1[4][0] , "\t\t Patrol Boat " , status_Player2[4][0])
    print("\n")

printStatus()
##################################################################################################################

#Opens Player1.in and read player moves.

"""
with open(sys.argv[3]) as inp:
    player1_in = list(inp.read().split())

"""
input_movesPlayer_1 = []

semicolonIndexes = [index for index in range(len(player1_in[0])) if player1_in[0][index] == ';']
semicolonIndexes.insert(0,-1)

i = 0
j = 1

while j < len(semicolonIndexes):
    input_movesPlayer_1.append(player1_in[0][semicolonIndexes[i]+1:semicolonIndexes[j]])
    i += 1
    j += 1

#Opens Player2.in and read player moves.

"""
with open(sys.argv[4]) as inp:
    player2_in = list(inp.read().split())

"""
input_movesPlayer_2 = []

semicolonIndexes = [index for index in range(len(player2_in[0])) if player2_in[0][index] == ';']
semicolonIndexes.insert(0,-1) 

i = 0
j = 1
while j < len(semicolonIndexes):
    input_movesPlayer_2.append(player2_in[0][semicolonIndexes[i]+1:semicolonIndexes[j]])
    i += 1
    j += 1

##################################################################################################################

#Convert inputs of moves of players to matrix versions of them.
#Just like if we want second element in list we should write list[1].

matrix_movesPlayer_1 = []
matrix_movesPlayer_2 = []

def getMatrix(inputMovesPlayer,matrixMovesPlayer):

    for i in inputMovesPlayer:
        try:
            splittedMoves = i.split(",")
            
            if len(splittedMoves) == 0 :
                matrixMovesPlayer.append(';')
            elif int(splittedMoves[0])<11 and splittedMoves[1] in letters and len(splittedMoves[1]) == 1:
                matrixMovesPlayer.append([int(splittedMoves[0])-1,letterDict[splittedMoves[1]]])
            else:
                matrixMovesPlayer.append(i)  
        except:
            matrixMovesPlayer.append(i)
         
getMatrix(input_movesPlayer_1,matrix_movesPlayer_1)

getMatrix(input_movesPlayer_2,matrix_movesPlayer_2)

##################################################################################################################

roundCounter = 1
moveCounter_Player1 = 0
moveCounter_Player2 = 0

pull_OptionalShips(OptionalPlayer_1,OptionalShips_Player1)
pull_OptionalShips(OptionalPlayer_2,OptionalShips_Player2)

#Checks if someone win or not.

def control ():

    global status_Player1
    global status_Player2

    if (status_Player1[0][0] == 'X' and status_Player1[1][0] == 'X X ' and status_Player1[2][0] == 'X' and status_Player1[3][0] == 'X' and status_Player1[4][0] == 'X X X X ') or (status_Player2[0][0] == 'X' and status_Player2[1][0] == 'X X ' and status_Player2[2][0] == 'X' and status_Player2[3][0] == 'X' and status_Player2[4][0] == 'X X X X ') :
        return False
    else:
        return True

#Game

def game():
    try:
        shipNames = ['B','C','D','S','P']

        global roundCounter
        global moveCounter_Player1
        global moveCounter_Player2
        
        while control() and ((len(input_movesPlayer_1) >= moveCounter_Player1) and (len(input_movesPlayer_2) >= moveCounter_Player2)): 
            if (len(input_movesPlayer_1) == moveCounter_Player1) and (len(input_movesPlayer_2) == moveCounter_Player2):
                raise IndexError
            if roundCounter % 2 == 0:
                player = "Player2"

            else:
                player = "Player1"
            
            print("\n")
            print(player + "’s Move\n\nRound : ",	roundCounter//2,"\t\t\t\t Grid Size: " + str(len(letters)) + "x" + str(len(letters)) + "\n")
            
            print_hiddenBoard()

            status_of_Ships(shipsPlayer_1,OptionalShips_Player1,hiddenBoard_Player1,status_Player1,allShips_Player1)
            status_of_Ships(shipsPlayer_2,OptionalShips_Player2,hiddenBoard_Player2,status_Player2,allShips_Player2)

            printStatus()
        
            if player == "Player1":
            
                print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                if type(matrix_movesPlayer_1[moveCounter_Player1]) == str:

                    if (len(matrix_movesPlayer_1[moveCounter_Player1]) > 4) or (len(matrix_movesPlayer_1[moveCounter_Player1])<3):
                        print("Valueerror")
                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                    elif ((matrix_movesPlayer_1[moveCounter_Player1][0][0] not in numbers) or (matrix_movesPlayer_1[moveCounter_Player1][0][2] not in letters)) and (matrix_movesPlayer_1[moveCounter_Player1][0][1] == ',') :
                        print("Assertionerror")
                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                    elif ((matrix_movesPlayer_1[moveCounter_Player1][0][3] not in letters)) and (matrix_movesPlayer_1[moveCounter_Player1][0][2] == ',') :
                        print("Assertionerror")
                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                    elif (matrix_movesPlayer_1[moveCounter_Player1][0][0] in numbers) and (matrix_movesPlayer_1[moveCounter_Player1][0][1] in numbers):
                        print("Assertionerror")
                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])
                    
                    elif matrix_movesPlayer_1[moveCounter_Player1][0].count(',') > 1 :
                        print("ValueError")
                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                    elif matrix_movesPlayer_1[moveCounter_Player1][0].count(',') == 1 :
                        x = matrix_movesPlayer_1[moveCounter_Player1][0].index(',')
                        if matrix_movesPlayer_1[moveCounter_Player1][0][x-1] in letters and matrix_movesPlayer_1[moveCounter_Player1][0][x+1] in letters:
                            print("ValueError")
                            moveCounter_Player1 += 1
                            print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])
                        elif matrix_movesPlayer_1[moveCounter_Player1][0][x-1] in ['0','1','2','3','4','5','6','7','8','9'] and matrix_movesPlayer_1[moveCounter_Player1][0][x+1] in ['0','1','2','3','4','5','6','7','8','9'] :
                            print("ValueError")
                            moveCounter_Player1 += 1
                            print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])                          
                    else:
                        print("IndexError")

                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                if type(matrix_movesPlayer_1[moveCounter_Player1]) != str:

                    if hiddenBoard_Player2[matrix_movesPlayer_1[moveCounter_Player1][0]][matrix_movesPlayer_1[moveCounter_Player1][1]] in ['X','O'] :
                        print("error")
                        moveCounter_Player1 += 1
                        print("Enter your move: " , input_movesPlayer_1[moveCounter_Player1])

                    else:
                        if shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]][matrix_movesPlayer_1[moveCounter_Player1][1]] in shipNames:

                            hiddenBoard_Player2[matrix_movesPlayer_1[moveCounter_Player1][0]][matrix_movesPlayer_1[moveCounter_Player1][1]] = 'X'
                            shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]] = shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]][ :matrix_movesPlayer_1[moveCounter_Player1][1]] + 'X' + shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]][matrix_movesPlayer_1[moveCounter_Player1][1]+1: ]
                            
                            status_of_Ships(shipsPlayer_1,OptionalShips_Player1,hiddenBoard_Player1,status_Player1,allShips_Player1)
                            status_of_Ships(shipsPlayer_2,OptionalShips_Player2,hiddenBoard_Player2,status_Player2,allShips_Player2)

                            moveCounter_Player1 += 1
                            roundCounter += 1
                            
                        else:
                            hiddenBoard_Player2[matrix_movesPlayer_1[moveCounter_Player1][0]][matrix_movesPlayer_1[moveCounter_Player1][1]] = 'O'
                            shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]] = shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]][ :matrix_movesPlayer_1[moveCounter_Player1][1]] + 'O' + shipsPlayer_2[matrix_movesPlayer_1[moveCounter_Player1][0]][matrix_movesPlayer_1[moveCounter_Player1][1]+1: ]
                
                            moveCounter_Player1 += 1
                            roundCounter += 1

            if player == "Player2":
                print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                if type(matrix_movesPlayer_2[moveCounter_Player2]) == str:

                    if (len(matrix_movesPlayer_2[moveCounter_Player2]) > 4) or (len(matrix_movesPlayer_2[moveCounter_Player2])<3):
                        print("Valueerror")
                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                    elif ((matrix_movesPlayer_2[moveCounter_Player2][0][0] not in numbers) or (matrix_movesPlayer_2[moveCounter_Player2][0][2] not in letters)) and (matrix_movesPlayer_2[moveCounter_Player2][0][1] == ',') :
                        print("Assertionerror")
                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                    elif ((matrix_movesPlayer_2[moveCounter_Player2][0][3] not in letters)) and (matrix_movesPlayer_2[moveCounter_Player2][0][2] == ',') :
                        print("Assertionerror")
                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                    elif (matrix_movesPlayer_2[moveCounter_Player2][0][0] in numbers) and (matrix_movesPlayer_2[moveCounter_Player2][0][1] in numbers):
                        print("Assertionerror")
                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])
                    
                    elif matrix_movesPlayer_2[moveCounter_Player2][0].count(',') > 1 :
                        print("ValueError")
                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                    elif matrix_movesPlayer_2[moveCounter_Player2][0].count(',') == 1 :
                        x = matrix_movesPlayer_2[moveCounter_Player2][0].index(',')
                        if matrix_movesPlayer_2[moveCounter_Player2][0][x-1] in letters and matrix_movesPlayer_2[moveCounter_Player2][0][x+1] in letters:
                            print("ValueError")
                            moveCounter_Player2 += 1
                            print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])
                        elif matrix_movesPlayer_2[moveCounter_Player2][0][x-1] in ['0','1','2','3','4','5','6','7','8','9'] and matrix_movesPlayer_2[moveCounter_Player2][0][x+1] in ['0','1','2','3','4','5','6','7','8','9'] :
                            print("ValueError")
                            moveCounter_Player2 += 1
                            print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])
                    else:
                        print("IndexError")

                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                if type(matrix_movesPlayer_2[moveCounter_Player2]) != str:

                    if hiddenBoard_Player1[matrix_movesPlayer_2[moveCounter_Player2][0]][matrix_movesPlayer_2[moveCounter_Player2][1]] in ['X','O'] :
                        print("error")
                        moveCounter_Player2 += 1
                        print("Enter your move: " , input_movesPlayer_2[moveCounter_Player2])

                    else:
                        if shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]][matrix_movesPlayer_2[moveCounter_Player2][1]] in shipNames:
                            hiddenBoard_Player1[matrix_movesPlayer_2[moveCounter_Player2][0]][matrix_movesPlayer_2[moveCounter_Player2][1]] = 'X'
                            shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]] = shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]][ :matrix_movesPlayer_2[moveCounter_Player2][1]] + 'X' + shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]][matrix_movesPlayer_2[moveCounter_Player2][1]+1: ]
                
                            status_of_Ships(shipsPlayer_1,OptionalShips_Player1,hiddenBoard_Player1,status_Player1,allShips_Player1)
                            status_of_Ships(shipsPlayer_2,OptionalShips_Player2,hiddenBoard_Player2,status_Player2,allShips_Player2)
                            moveCounter_Player2 += 1
                            roundCounter += 1
                        
                        else:
                            hiddenBoard_Player1[matrix_movesPlayer_2[moveCounter_Player2][0]][matrix_movesPlayer_2[moveCounter_Player2][1]] = 'O'
                            shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]] = shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]][ :matrix_movesPlayer_2[moveCounter_Player2][1]] + 'O' + shipsPlayer_1[matrix_movesPlayer_2[moveCounter_Player2][0]][matrix_movesPlayer_2[moveCounter_Player2][1]+1: ]
                
                            moveCounter_Player2 += 1
                            roundCounter += 1


        else:                   
            print('\n' + player , 'Wins!\n\nFinal Information\n')
            finalOutput()
            status_of_Ships(shipsPlayer_1,OptionalShips_Player1,hiddenBoard_Player1,status_Player1,allShips_Player1)
            status_of_Ships(shipsPlayer_2,OptionalShips_Player2,hiddenBoard_Player2,status_Player2,allShips_Player2)
            printStatus()
    
    except IndexError:
        if player == 'Player1':
           player = "Player2"

        else:
            player = "Player1" 

        print("\n")
        print(player,'left.\n\n')
        print("kaBOOM: run for your life!")

#Print the output and write it to document.

print("Battle of Ships Game\n\n")

original_stdout = sys.stdout

with open("Battleship.out","w",encoding="utf-8") as f:
    sys.stdout = f
    f.write("Battle of Ships Game\n\n")
    game()
    sys.stdout = original_stdout

with open("Battleship.out", 'r',encoding="utf-8") as f:
    print(f.read())
##################################################################################################################


