#  #  #  #  VERSION 1.0  #  #  #  #

import numpy as np
import time

h = 13
w = 17

currH = 7
currW = 7

d1 = 2
d2 = 2
d3 = 2
d4 = 2

grid = np.zeros((h, w))

def updateGrid(grid, h, w, currH, currW, d1, d2, d3, d4):
    grid[currH, currW] = 4
    
########################################### UP
    if d1 == 2:
        # TILES
        n = 2
        for _ in range(2):   # D1
            if grid[currH - n, currW] == 0:
                grid[currH - n, currW] = 2
            elif grid[currH - n, currW] == 1:
                grid[currH - n, currW] = 3
            
            n = n+2
        
        # WALLS
        n = 1
        for _ in range(2):   # D1
            if grid[currH - n, currW] == 0:
                grid[currH - n, currW] = 1
            
            n = n+2
        if grid[currH - n, currW] == 0:
            grid[currH - n, currW] = 2
########################################### RIGHT
    if d2 == 2:
        # TILES
        n = 2
        for _ in range(2):   # D2
            if grid[currH, currW + n] == 0:
                grid[currH, currW + n] = 2
            elif grid[currH, currW + n] == 1:
                grid[currH, currW + n] = 3
            
            n = n+2
        
        # WALLS
        n = 1
        for _ in range(2):   # D2
            if grid[currH, currW + n] == 0:
                grid[currH, currW + n] = 1
            
            n = n+2
        if grid[currH, currW + n] == 0:
            grid[currH, currW + n] = 2
########################################### DOWN
    if d1 == 2:
        # TILES
        n = 2
        for _ in range(2):   # D3
            if grid[currH + n, currW] == 0:
                grid[currH + n, currW] = 2
            elif grid[currH + n, currW] == 1:
                grid[currH + n, currW] = 3
            
            n = n+2
        
        # WALLS
        n = 1
        for _ in range(2):   # D3
            if grid[currH + n, currW] == 0:
                grid[currH + n, currW] = 1
            
            n = n+2
        if grid[currH + n, currW] == 0:
            grid[currH + n, currW] = 2
########################################### LEFT
    if d2 == 2:
        # TILES
        n = 2
        for _ in range(2):   # D4
            if grid[currH, currW - n] == 0:
                grid[currH, currW - n] = 2
            elif grid[currH, currW - n] == 1:
                grid[currH, currW - n] = 3
            
            n = n+2
        
        # WALLS
        n = 1
        for _ in range(2):   # D4
            if grid[currH, currW - n] == 0:
                grid[currH, currW - n] = 1
            
            n = n+2
        if grid[currH, currW - n] == 0:
            grid[currH, currW - n] = 2
###########################################
    
    return(grid)


grid = updateGrid(grid, h, w, currH, currW, d1, d2, d3, d4)

print(grid)




'''
# TILES
    0 = undiscovered
    1 = lr
    2 = ud
    3 = lrud
    4 = visited

# WALLS
    0 = undiscovered
    1 = no wall
    2 = possible wall
    3 = wall
'''


'''
def measureFront(laserF):
    if laserF <= 30:
        return(0)
    elif 30 < laserF <= 60:
        return(1)
    elif 60 < laserF <= 75:
        return(2)
    elif 75 < laserF:
        return(3)
'''
