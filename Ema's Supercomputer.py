#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#
def validPair(cross1, cross2):
    for pos in cross2:
        if pos in cross1:
            return False
    return True

def goodSpots(r,c,i):
    if grid[r+i][c] == 'G' and grid[r-i][c] == 'G' and grid[r][c+i] == 'G' and grid[r][c-i] == 'G':
        return True
    return False
    
def getCrosses(r, c):
    indices = set((r,c))
    crosses = [[1, indices]]
    area = 1
    i = 1
    while r + i < n and r - i >= 0 and c + i < m and c - i >= 0 and goodSpots(r,c,i):
        area += 4
        for pos in [(r+i, c),(r-i, c),(r, c+i), (r, c-i)]:
            indices.add(pos)
        crosses.append([area, indices.copy()])
        i += 1
    return crosses

def twoPluses(grid):
    # find all crosses
    product_area = 0
    crosses = [] 
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 'G':
                crosses += getCrosses(r,c)
    # find two largest crosses
    AREA_INDEX, INDICES_INDEX = 0, 1
    for i in range(len(crosses)):
        for j in range(i+1, len(crosses)):
            if validPair(crosses[i][INDICES_INDEX], crosses[j][INDICES_INDEX]):
                product_area = max(product_area, crosses[i][AREA_INDEX]*crosses[j][AREA_INDEX])
    return product_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
