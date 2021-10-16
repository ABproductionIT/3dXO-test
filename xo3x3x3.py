import numpy as np
from calculation import checkWinner
# menak es parametr@ talises qashvumes mi kom
level = 4

def makeCube(level):
    return  np.zeros((level, level, level))

cube = makeCube(level)

X = 1
O = level + X

# cube[2][0][0] = 1
# cube[2][1][0] = 1
# cube[2][2][0] = 1

# cube[0][2][0] = 1
# cube[1][1][1] = 1
# cube[2][0][2] = 1

cube[0,0,0] = 1
cube[1,1,3] = 1
cube[2,2,2] = 1


print(cube)
print(checkWinner(cube, X, O, level))

