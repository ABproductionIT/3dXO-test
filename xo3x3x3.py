import numpy as np

level = 3 # start levli tiv ham el chaperna
#skzbic sax 0 ner a (float)
cube = np.zeros((level, level, level))
#player1 takic x-y grancuma 1
X = 1
#player2 takic O-n grancum a 3
O = 3
# cube (z, y, x) kordinatnery es tipi a cuyc tali print aneluc
''' 
    y x -    -     -
    |  [000. 001. 002.]
    |  [010. 011. 012.]        z0 sloy
    |  [020. 021. 022.]]

    y x -     -      -
    |  [100. 101. 102.]
    |  [110. 111. 112.]        z1 sloy
    |  [120. 121. 122.]]

    y x -    -      -
    |  [200. 201. 202.]
    |  [210. 211. 212.]        z2 sloy
    |  [220. 221. 222.]]

'''
# talis es kordinatnery` x y z, orinak 2 2 2
cord_x= 2
cord_y= 2
cord_z= 2

cube[cord_z, cord_y, cord_x]=X
print(cube)

