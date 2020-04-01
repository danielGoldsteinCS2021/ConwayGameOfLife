# Life.py

import sys

'''
Tamir
Daniel
Emily
Cam
Ellie
'''


class Game:
    def __init__(self, fileName="inLife.txt"):

        self.numOfGen, self.board = self.readFile(fileName)# initalize board and set number of generations
        self.rowLen = len(self.board)
        self.colLen = len(self.board[0])
        self.startGame()

    # Takes the self instance as a parameter as well as the fileName
    # It reads the text file and formats it so that we have the 2D array, board, and numOfGen
    def readFile(self, fileName):
        file = open(fileName, 'r')
        lines = file.readlines()
        board = []  # initializes the 2D array that will hold the grid
        first = True    # used to read the first line, to detect the number of generations
        for line in lines:
            line = line.strip() # strip the whitespace characters
            if first:
                numOfGen = int(line)
                first = False
                continue
            row = []
            for value in line:
                row.append(int(value))
            board.append(row)
        return numOfGen, board

    # Takes the self instance as a paramater as well as the current generation number
    # It prints the current grid for the generation we are on
    def printGame(self, genNum):
        print("Generation ", genNum)
        for row in self.board:
            for val in row:
                print(val, end="")
            print()

    # Takes the self instance as a parameter as well as the position of a cell
    # return a list of the valid neighbours surrounding that position
    def generateNeighbors(self, position):

        # we have 8 neighbours - N, E, S, W, NE, NW, SE, SW
        row, col = position[0], position[1]
        # allNeighbors - are all of our neighbors (even those out of bounds)
        allNeighbors = [(row+1, col), (row-1, col),
                        (row, col+1), (row, col-1),
                        (row+1, col-1), (row-1, col-1),
                        (row+1, col+1), (row-1, col+1)]

        validNeighbors = [] # only the neighbors in bounds
        for x, y in allNeighbors:
            if x >= 0 and x < self.rowLen and y >= 0 and y < self.colLen:
                validNeighbors.append((x, y)) # appends if in bounds
        return validNeighbors

    # Takes the self instance as a parameter as well as the position of a cell
    # If the cell will be alive in the next gen it returns True, otherwise it returns False
    def willBeAlive(self, position):
        aliveNeighborCount = 0  # a count that tracks the number of alive neighbours
        r, c = position[0], position[1]

        if self.board[r][c] == 1:   # determines if the current position is alive
            alive = True
        else:
            alive = False

        neighbors = self.generateNeighbors((r, c))  # creates a list of the cells neighbours

        for row, col in neighbors:
            if self.board[row][col] == 1:
                aliveNeighborCount+=1 # if neighbor is alive, increase count

        if aliveNeighborCount == 3: # if the neighbour count is 2/3 return True for alive
            return True
        elif aliveNeighborCount == 2 and alive:
            return True
        else:   # return False as it isn't alive
            return False

    # Take the self instance as a parameter so that it has access to global variables
    # Creates the next generation according to the rules of Conway's Game of Life
    def produceNextGeneration(self):
        newBoard = []   # use new board to avoid editing current board
        for row in range(self.rowLen):
            newBoard.append([])
            for col in range(self.colLen):
                if self.willBeAlive((row, col)):    # if the cell will be alive, append a  1 in it's position
                    newBoard[row].append(1)
                else:                               # otherwise append a 0 to show it's status in the next gen
                    newBoard[row].append(0)
        self.board = newBoard

    # Takes the self instance as a parameter so that it has access to global variables
    # Initializes the game so that it runs through each generation
    def startGame(self):

        sys.stdout = open("outLife.txt", "w")   # creates the new text file the solution will print to

        self.printGame(0)   # prints initial state
        for i in range(self.numOfGen):  # for each generation it produces what the next generation would look like
            self.produceNextGeneration()
            self.printGame(i+1)

        sys.stdout.close()

if __name__ == "__main__":
    Game()
    # Game("TestCases/penta.txt") -- how to override the inLife.txt with a different file
