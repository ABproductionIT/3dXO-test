import numpy as np
from calculation import checkWinner
# menak es parametr@ talises qashvumes mi kom
level = 3


def makeCube(level):
    return np.zeros((level, level, level))


cube = makeCube(level)

X = 1
O = level + X

# cube[2][0][0] = 1
# cube[2][1][0] = 1
# cube[2][2][0] = 1

cube[0][2][0] = 1
cube[1][1][1] = 1
cube[2][0][2] = 1

# cube[0,0,0] = O
# cube[1,1,1] = O
# cube[2,2,2] = O
# cube[3,3,3] = O




print(cube)
print(checkWinner(cube, X, O, level))
