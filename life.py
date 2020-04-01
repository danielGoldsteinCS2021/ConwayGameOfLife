
# Life.py

'''
Tamir
Daniel
Emily
Cam
Ellie
'''
import pygame


class Game:
    def __init__(self, fileName="inLife.txt"):
        self.numOfGen, self.board = self.readFile(fileName) # initalize board and set number of generations
        self.rowLen = len(self.board)
        self.colLen = len(self.board[0])
        # Set the HEIGHT and WIDTH of the screen
        WINDOW_SIZE = [900, 600]
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        # Set title of screen
        pygame.display.set_caption("Conway's Game Of Life")
        self.drawGrid()
        self.startGame()

    def drawGrid(self):
        # Draw the grid
        MARGIN = 0
        WIDTH = 12
        HEIGHT = 12
        offsetLength = 450 - WIDTH - (self.colLen*WIDTH)//2 # aprox
        offsetHeight = 300 - HEIGHT - (self.rowLen*HEIGHT)//2 # aprox
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        GREEN = (0, 255, 0)
        RED = (255, 0, 0)
        for r in range(self.rowLen):
            for c in range(self.colLen):
                color = BLACK
                if self.board[r][c] == 1:
                    color = (13, 214, 224)
                pygame.draw.rect(self.screen, color,
                                [offsetLength+((MARGIN + WIDTH) * c) + MARGIN,
                                 offsetHeight+((MARGIN + HEIGHT) * r) + MARGIN,
                                 WIDTH, HEIGHT])
        pygame.display.flip()

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
        self.numOfGen = 10000000
        self.screen.fill((0,0,0))
        done = False
        i = 0
        while(i < self.numOfGen and not done):
            #screen.fill((0,0,0))
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
            pygame.time.Clock().tick(3)
            self.produceNextGeneration()
    #        self.printGame(i+1)
            self.drawGrid()
            i+=1

if __name__ == "__main__":
    # Initialize pygame
    pygame.init()
    Game("test.txt")
