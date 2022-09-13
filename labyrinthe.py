import queue
import random
from random import randint as rng

t=0


def creation():
    nnn="non"
    while nnn.lower()=="non":
        T=[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        for i in range (50):
            T[i]=rng(0,3)
            if T[i]==0:
                T[i]="#"
            else:
                T[i]=" "
        debut=rng(1,7)
        T[debut]="O"
        fin=rng(43,49)
        T[fin]="X"
    

        print(T[1],T[2],T[3],T[4],T[5],T[6],T[7])
        print(T[8],T[9],T[10],T[11],T[12],T[13],T[14])
        print(T[15],T[16],T[17],T[18],T[19],T[20],T[21])
        print(T[22],T[23],T[24],T[25],T[26],T[27],T[28])
        print(T[29],T[30],T[31],T[32],T[33],T[34],T[35])
        print(T[36],T[37],T[38],T[39],T[40],T[41],T[42])
        print(T[43],T[44],T[45],T[46],T[47],T[48],T[49])

        nnn=str(input("ce labyrinthe vous convient-il ?"))
        if nnn.lower()!="non":
            return T

def createMaze():
    T = creation()
    maze = []
    maze.append([T[1],T[2],T[3],T[4],T[5],T[6],T[7]])
    maze.append([T[8],T[9],T[10],T[11],T[12],T[13],T[14]])
    maze.append([T[15],T[16],T[17],T[18],T[19],T[20],T[21]])
    maze.append([T[22],T[23],T[24],T[25],T[26],T[27],T[28]])
    maze.append([T[29],T[30],T[31],T[32],T[33],T[34],T[35]])
    maze.append([T[36],T[37],T[38],T[39],T[40],T[41],T[42]])
    maze.append([T[43],T[44],T[45],T[46],T[47],T[48],T[49]])

    return maze


def printMaze(
    maze, path=""
):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x
    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(
    maze, moves
):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True

def findEnd(
    maze, moves
):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves,t)
        printMaze(maze, moves)
        return True

    return False


nums = queue.Queue()
nums.put("")
add = ""
maze  = createMaze()

tl=100001
p="a"






#main
while not (
    findEnd(maze, add) or (t==700000)
):
    t=t+1
    if t>100000:
        print(t)
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)
if t==300000:
    print("aucune solution trouvée.")


