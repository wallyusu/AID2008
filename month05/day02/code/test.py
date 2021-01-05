import numpy as np
grid = [
    [4,3,8,4],
    [9,5,1,9],
    [2,7,6,2]
]

def numMagicSquaresInside(grid):
    # li = []
    # for d in grid:
    data = np.unique(grid)
    # li.append(list(data))
    # data = np.array(li)
    print(data)
    # data1 = np.random.randn(data)
    # print(data1)
    # a = data.sum(axis=0)
    # p = data.sum(axis=1)
    # if a == p:
    #     print(data)

if __name__ == '__main__':
    numMagicSquaresInside(grid)
