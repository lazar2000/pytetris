import random, time, pygame, sys
from pygame.locals import *

DEBUG = ""


def log(msg):
    global DEBUG
    DEBUG += str(msg)


############################################
# SETTING UP THE GAME MECHANICS            #
############################################

# INITIAL VALUES
#######################

# INITALIZING THE BOARD
BOARD = []


def initBoard():
    global BOARD
    BOARD = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]


initBoard()


# PIECES
#######################

class Piece:
    shape = []
    coord = [4, 0]
    index = 0

    def check(self):
        shp = self.shape[self.index]
        global BOARD
        log("{} {} {} {}".format(self.coord[0], len(BOARD[0]) - len(shp) + 1, self.coord[1],
                                 len(BOARD) - len(shp[0]) + 1))
        if (
                self.coord[0] < 0 or
                self.coord[1] < 0 or
                self.coord[0] > len(BOARD[0]) - len(shp) + 1 or
                self.coord[1] > len(BOARD) - len(shp[0]) + 1
        ):
            return False
        try:
            for i in range(len(shp)):
                for j in range(len(shp[0])):
                    if BOARD[self.coord[1] + j][self.coord[0] + i] != '.' and shp[i][j] != '.':
                        return False
            return True
        except:
            log(" ERR001")
            return False

    def draw(self, tile, bpos):
        print(self.shape)
        print(self.index)
        shp = self.shape[self.index]
        global SCREEN
        for i in range(len(shp)):
            for j in range(len(shp[0])):
                if (shp[i][j] != '.'):
                    SCREEN.blit(tile, [bpos[0] + (self.coord[0] + i) * 24, bpos[1] + (self.coord[1] + j) * 24])

    def add(self):
        shp = self.shape[self.index]
        global BOARD
        for i in range(len(shp)):
            for j in range(len(shp[0])):
                if (shp[i][j] != '.'):
                    BOARD[self.coord[1] + j][self.coord[0] + i] = shp[i][j]

    def move(self, x, y, r):
        self.coord[0] += x
        self.coord[1] += y
        self.index += r
        self.index = self.index % len(self.shape)
        if (not self.check()):
            self.coord[0] -= x
            self.coord[1] -= y
            self.index -= r
            return False
        return True


class PieceT(Piece):
    shape = [
        [
            ['K', 'K', 'K'],
            ['.', 'K', '.']
        ],
        [
            ['K', '.'],
            ['K', 'K'],
            ['K', '.']
        ],
        [
            ['.', 'K', '.'],
            ['K', 'K', 'K']
        ],
        [
            ['.', 'K'],
            ['K', 'K'],
            ['.', 'K']
        ]
    ]


class PieceS(Piece):
    shape = [
        [
            ['.', 'L', 'L'],
            ['L', 'L', '.']
        ],
        [
            ['L', '.'],
            ['L', 'L'],
            ['.', 'L']
        ]
    ]


class PieceZ(Piece):
    shape = [
        [
            ['P', 'P', '.'],
            ['.', 'P', 'P']
        ],
        [
            ['.', 'P'],
            ['P', 'P'],
            ['P', '.']
        ]
    ]


class PieceQ(Piece):
    shape = [
        [
            ['Y', 'Y'],
            ['Y', 'Y']
        ]
    ]


class PieceI(Piece):
    shape = [
        [
            ['B', 'B', 'B', 'B']
        ],
        [
            ['B'],
            ['B'],
            ['B'],
            ['B']
        ]
    ]


class PieceL(Piece):
    shape = [
        [
            ['R', 'R', 'R'],
            ['R', '.', '.']
        ],
        [
            ['R', '.'],
            ['R', '.'],
            ['R', 'R']
        ],
        [
            ['.', '.', 'R'],
            ['R', 'R', 'R']
        ],
        [
            ['R', 'R'],
            ['.', 'R'],
            ['.', 'R']
        ]
    ]


class PieceG(Piece):
    shape = [
        [
            ['G', 'G', 'G'],
            ['.', '.', 'G']
        ],
        [
            ['G', 'G'],
            ['G', '.'],
            ['G', '.']
        ],
        [
            ['G', '.', '.'],
            ['G', 'G', 'G']
        ],
        [
            ['.', 'G'],
            ['.', 'G'],
            ['G', 'G']
        ]
    ]


# new random piece
def newPiece():
    i = random.randint(0, 6)
    if (i == 1):
        rtn = PieceS()
    elif (i == 2):
        rtn = PieceZ()
    elif (i == 3):
        rtn = PieceT()
    elif (i == 4):
        rtn = PieceI()
    elif (i == 5):
        rtn = PieceL()
    elif (i == 6):
        rtn = PieceG()
    else:
        rtn = PieceQ()
    rtn.index = random.randint(0, len(rtn.shape)-1)
    return rtn


############################################
# SETTING UP THE GRAPHICS                  #
############################################

# INITIAL VALUES, LOADING RESOURCES
#######################

# INITIALIZING PYGAME
pygame.init()

# BOARD POSITION
BRD_POS = [280, 60]

# SETTING COLORS
C_BLACK = (0, 0, 0)
C_BLUE = (44, 52, 163)
C_DARK = (63, 63, 63)
C_GREEN = (34, 177, 76)
C_LIGHT = (153, 217, 234)
C_PINK = (255, 100, 150)
C_PURPLE = (163, 73, 164)
C_RED = (237, 28, 36)
C_YELLOW = (255, 201, 14)
C_WHITE = (255, 255, 255)

# SETTING FONTS
F_48 = pygame.font.Font("res/times.ttf", 48)
F_36 = pygame.font.Font("res/times.ttf", 36)
F_24 = pygame.font.Font("res/times.ttf", 24)
F_12 = pygame.font.Font("res/times.ttf", 12)
F_48B = pygame.font.Font("res/timesbd.ttf", 48)
F_36B = pygame.font.Font("res/timesbd.ttf", 36)
F_24B = pygame.font.Font("res/timesbd.ttf", 24)
F_12B = pygame.font.Font("res/timesbd.ttf", 12)
# setting bold versions of fonts
#F_48B.set_bold(True)
#F_36B.set_bold(True)
#F_24B.set_bold(True)
#F_12B.set_bold(True)

# LOADING BLOCKS
B_EMPTY = pygame.image.load("res/b-empty.png")
B_NEW = pygame.image.load("res/b-new.png")
B_RED = pygame.image.load("res/b-red.png")
B_GREEN = pygame.image.load("res/b-green.png")
B_BLUE = pygame.image.load("res/b-blue.png")
B_YELLOW = pygame.image.load("res/b-yellow.png")
B_PURPLE = pygame.image.load("res/b-purple.png")
B_PINK = pygame.image.load("res/b-pink.png")
B_LIGHT = pygame.image.load("res/b-light.png")

# SCREEN SETUP
SIZE = WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("CS1102 Tetris")
pygame.display.set_icon(pygame.image.load("res/icon.png"))


# GRAPHIC FUNCTIONS
#######################

# DRAW THE BOARD ON THE SCREEN
def printBoard(pos):
    global BOARD, SCREEN
    inpos = [pos[0], pos[1]]
    pygame.draw.rect(SCREEN, C_WHITE, pygame.Rect(pos[0] - 2, pos[1] - 2, 244, 484), 1)
    pygame.draw.rect(SCREEN, C_BLACK, pygame.Rect(pos[0] - 1, pos[1] - 1, 242, 482), 1)
    for row in BOARD:
        pos[0] = inpos[0]
        for field in row:
            sq = B_EMPTY
            if (field == 'R'):
                sq = B_RED
            if (field == 'B'):
                sq = B_BLUE
            if (field == 'G'):
                sq = B_GREEN
            if (field == 'Y'):
                sq = B_YELLOW
            if (field == 'P'):
                sq = B_PURPLE
            if (field == 'K'):
                sq = B_PINK
            if (field == 'L'):
                sq = B_LIGHT
            SCREEN.blit(sq, pos)
            pos[0] += 24
        pos[1] += 24
    pos[0] = inpos[0]
    pos[1] = inpos[1]


############################################
# THE GAME LOOP                            #
############################################

def gameOver():
    initBoard()


pc = newPiece()

step = 0

while True:
    DEBUG = "S{:08} ".format(step)
    x = 0
    y = 0
    r = 0
    # for this not to actually be an infinite loop, we need to quit on pressing X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += 1
            if event.key == pygame.K_LEFT:
                x -= 1
            if event.key == pygame.K_RIGHT:
                x += 1
            if event.key == pygame.K_UP:
                r = 1
        pc.move(x, y, r)

    for r in BOARD:
        t = True
        for f in r:
            if (f=='.'):
                t = False
        if (t):
            BOARD.remove(r)
            BOARD.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])

    # clearing the screen
    SCREEN.fill(C_BLACK)

    # printing the board
    printBoard(BRD_POS)

    pc.draw(B_NEW, BRD_POS)

    rndr = F_12.render(DEBUG, False, C_WHITE)
    SCREEN.blit(rndr, [0, 0])

    if (step % 5 == 0):
        if (not pc.move(0, 1, 0)):
            pc.add()
            pc = newPiece()
            pc.coord = [4, 0]
            if (not pc.check()):
                gameOver()

    pygame.time.wait(50)

    # sending display to buffer
    pygame.display.flip()
    step += 1
