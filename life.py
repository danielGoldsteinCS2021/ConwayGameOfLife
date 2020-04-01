
# Life.py

'''
Tamir
Daniel
Emily
Cam
Ellie
'''


class Game:
    def __init__(self, fileName="test.txt"): # REMEMBER TO CHANGE FILE NAME
        self.numOfGen, self.board = self.readFile(fileName)
        self.rowLen = len(self.board)
        self.colLen = len(self.board[0])
        self.startGame()

    def readFile(self, fileName):
        file = open(fileName, 'r')
        lines = file.readlines()
        board = []
        for line in lines:
            line = line.strip()
            row = []
            for value in line:
                row.append(int(value))
            board.append(row)
        numOfGen = int(board[0][0])
        board = board[1:]
        return numOfGen, board

    def printGame(self, genNum):
        print("Generation ", genNum)
        for row in self.board:
            for val in row:
                print(val, end="")
            print()

    def generateNeighbors(self, position):
        # we have 8 neighbors - N, E, S, W, NE, NW, SE, SW
        row, col = position[0], position[1]
        # below returns all of our neighbors
        allNeighbors = [(row+1, col), (row-1, col),
                        (row, col+1), (row, col-1),
                        (row+1, col-1), (row-1, col-1),
                        (row+1, col+1), (row-1, col+1)]
        validNeighbors = []
        for x, y in allNeighbors:
            if x >= 0 and x < self.rowLen and y >= 0 and y < self.colLen:
                validNeighbors.append((x, y))
        return validNeighbors



    # boolean function that returns whether
    # position will be alive in next generation
    def willBeAlive(self, position):
        aliveNeighborCount = 0
        r, c = position[0], position[1]
        if self.board[r][c] == 1:
            alive = True
        else:
            alive = False
        neighbors = self.generateNeighbors((r, c))
        for row, col in neighbors:
            if self.board[row][col] == 1:
                aliveNeighborCount+=1
        if aliveNeighborCount == 3:
            return True
        elif aliveNeighborCount == 2 and alive:
            return True
        else:
            return False

    def produceNextGeneration(self):
        newBoard = []
        for row in range(self.rowLen):
            newBoard.append([])
            for col in range(self.colLen):
                if self.willBeAlive((row, col)):
                    newBoard[row].append(1)
                else:
                    newBoard[row].append(0)
        self.board = newBoard


    def startGame(self):
        self.printGame(0)
        for i in range(self.numOfGen):
            self.produceNextGeneration()
            self.printGame(i+1)

Game()
