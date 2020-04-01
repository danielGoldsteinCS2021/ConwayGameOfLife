
# Life.py

'''
Tamir
Daniel
Emily
Cam
Ellie
'''


class Game:
    def __init__(self, fileName="inLife.txt"):
        self.numOfGen, self.board = self.readFile(fileName) # initalize board and set number of generations
        self.rowLen = len(self.board)
        self.colLen = len(self.board[0])
        self.startGame()

    # Reads txt file and creates board
    # as a 2d Array. Sets the number of
    # generations to be created as well.
    def readFile(self, fileName):
        file = open(fileName, 'r')
        lines = file.readlines()
        board = []
        first = True # used for first line, which is number of generations
        for line in lines:
            line = line.strip()
            if first:
                numOfGen = int(line)
                first = False
                continue
            row = []
            for value in line:
                row.append(int(value))
            board.append(row)
        return numOfGen, board

    # Prints out current game state
    def printGame(self, genNum):
        print("Generation ", genNum)
        for row in self.board:
            for val in row:
                print(val, end="")
            print()

    def generateNeighbors(self, position):
        # we have 8 neighbors - N, E, S, W, NE, NW, SE, SW
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

    # predicate function that returns whether
    # position will be alive in next generation
    def willBeAlive(self, position):
        aliveNeighborCount = 0 # count of alive neighbors
        r, c = position[0], position[1]
        if self.board[r][c] == 1:
            alive = True
        else:
            alive = False
        neighbors = self.generateNeighbors((r, c))
        for row, col in neighbors:
            if self.board[row][col] == 1:
                aliveNeighborCount+=1 # if neighbor is alive, increase count
        if aliveNeighborCount == 3:
            return True
        elif aliveNeighborCount == 2 and alive:
            return True
        else:
            return False

    # creates the next generation
    def produceNextGeneration(self):
        newBoard = [] # use new board to avoid editing current board
        for row in range(self.rowLen):
            newBoard.append([])
            for col in range(self.colLen):
                if self.willBeAlive((row, col)):
                    newBoard[row].append(1)
                else:
                    newBoard[row].append(0)
        self.board = newBoard

    # runs game
    def startGame(self):
        self.printGame(0) # prints intial state
        for i in range(self.numOfGen):
            self.produceNextGeneration()
            self.printGame(i+1)

if __name__ == "__main__":
    Game("test.txt")
