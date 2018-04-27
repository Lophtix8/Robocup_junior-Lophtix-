#!/usr/local/bin/python3
from arduinoControl import *

x = 0
y = 0
d = 0

notDiscovered = []
discovered = []
wall = []
noWall = []
blackGround = []
heatedTile = []
letterTile = []
start = [0, 0]
crosses = []

def Mapping():
        serialWrite(5)
        color = int(ser.readline(), 10)
        if color == 0;
            serialWrite(1)
        serialWrite(4)
	##### MAPPING THE ROOM ######################################################
	if d == 0:
		if ((US[0] and US[3]) > 10) and not ([x-1, y] in wall or noWall == False):
			noWall.append([x-1, y])
			notDiscovered.append([x-2, y])
		elif not [x-1, y] in wall or noWall == False:
			wall.append([x-1, y])
			
		if ((US[2] and US[5]) > 10) and not ([x+1, y] in wall or noWall == False):
			noWall.append([x+1, y])
			notDiscovered.append([x+2, y])
		elif not [x+1, y] in wall or noWall == False:
			wall.append([x+1, y])
			
		if (US[1] > 10) and not ([x, y+1] in wall or noWall == False):
			noWall.append([x, y+1])
			notDiscovered.append([x, y+2])
		elif not [x, y+1] in wall or noWall == False:
			wall.append([x, y+1])
			
		if (laserValue('B') > 10) and not ([x, y-1] in wall or noWall == False):
			noWall.append([x, y-1])
			notDiscovered.append([x, y-2])
		elif not [x, y-1] in wall or noWall == False:
			wall.append([x, y-1])
		
		##### ADDING CORNERS ####################################################
		if ([x+1, y] in noWall) and ([x-1, y] in Wall) and ([x, y+1] in noWall) and ([x, y-1] in wall):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in wall) and ([x-1, y] in noWall) and ([x, y+1] in wall) and ([x, y-1] in noWall):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in noWall) and ([x-1, y] in wall) and ([x, y+1] in wall) and ([x, y-1] in noWall):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in wall) and ([x-1, y] in noWall) and ([x, y+1] in noWall) and ([x, y-1] in wall):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in wall) and ([x-1, y] in noWall) and ([x, y+1] in noWall) and ([x, y-1] in noWall) and not([x, y] in crosses):
			crosses.append([x, y, len(crosses)])
		
		elif ([x+1, y] in noWall) and ([x-1, y] in wall) and ([x, y+1] in noWall) and ([x, y-1] in noWall) and not([x, y] in crosses):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in noWall) and ([x-1, y] in noWall) and ([x, y+1] in wall) and ([x, y-1] in noWall) and not([x, y] in crosses):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in noWall) and ([x-1, y] in noWall) and ([x, y+1] in noWall) and ([x, y-1] in wall) and not([x, y] in crosses):
			crosses.append([x, y, len(crosses)])
			
		elif ([x+1, y] in noWall) and ([x-1, y] in noWall) and ([x, y+1] in noWall) and ([x, y-1] in noWall) and not([x, y] in crosses):
			crosses.append([x, y, len(crosses)])
		
		##### DECIDING DIRECTION TO TURN ########################################
		if ([x-2, y] in notDiscovered) and ([x-1, y] in noWall):
			x = x-2
			d = 3
			serialWrite(3)
			serialWrite(0)
		
		elif ([x+2, y] in notDiscovered) and ([x+1, y] in noWall):
			x = x+2
			d = 1
			serialWrite(2)
			serialWrite(0)
			
		elif ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			serialWrite(0)
			
		elif ([y, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			serialWrite(1)
		
		else:
			
	
	elif d == 1:
		if ((US[0] and US[3]) > 10) and not ([x, y+1] in wall or noWall):
			noWall.append([x, y+1])
			notDiscovered.append([x, y+2])
			
		elif not [x, y+1] in wall or noWall:
			wall.append([x, y+1])
			
		if ((US[2] and US[5]) > 10) and not ([x, y-1] in wall or noWall):
			noWall.append([x, y-1])
			notDiscovered.append([x, y-2])
		elif not [x, y-1] in wall or noWall:
			wall.append([x, y-1])
			
		if (US[1] > 10) and not ([x+1, y] in wall or noWall):
			noWall.append[x+1, y]
			notDiscovered.append([x+2, y])
		elif not [x+1, y] in wall or noWall:
			wall.append([x+1, y])
			
		if (laserValue('B') > 10) and not ([x-1 ,y] in wall or noWall):
			noWall.append([x-1, y])
			notDiscovered.append([x-2, y])
		elif not [x-1, y] in wall or noWall:
			wall.append([x-1, y])
			
		##### DECIDING DIRECTION TO TURN ########################################
		if ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			serialWrite(3)
			serialWrite(0)
		
		elif ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			serialWrite(2)
			serialWrite(0)
		
		elif ([x+2, y] in notDiscovered) and ([x+1, y] in noWall):
			x = x+2
			d = 1
			serialWrite(0)
			
		elif ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			x = x-2
			d = 3
			serialWrite(1)
    	
	elif d == 2:
		if ((US[0] and US[3]) > 10) and not ([x+1, y] in wall or noWall):
			noWall.append([x+1, y])
			if not [x+1, y] in discovered:
				notDiscovered.append([x+2, y])
		elif not [x+1, y] in wall or noWall:
			wall.append([x+1, y])
			
		if ((US[2] and US[5]) > 10) and not ([x-1, y] in wall or noWall):
			noWall.append([x-1, y])
			if not [x-1, y] in discovered:
				notDiscovered.append([x-2, y])
		elif not [x-1, y] in wall or noWall:
			wall.append([x-1, y])
			
		if (US[1] > 10) and not ([x, y-1] in wall or noWall):
			noWall.append([x, y-1])
			notDiscovered.append([x, y-2])
		elif not [x, y-1] in wall or noWall:
			wall.append([x, y-1])
			
		if (laserValue('B') > 10) and not ([x, y+1] in wall or noWall):
			noWall.append([x, y+1])
		elif not [x, y+1] in wall or noWall:
			wall.append([x, y+1])

		##### DECIDING DIRECTION TO TURN ##############################################
		if ([x+2, y] in notDiscovered) and ([x+2, y] in noWall):
			x = x+2
			d = 1
			serialWrite(3)
			serialWrite(0)
			
		elif ([x-2, y] in notDiscovered) and ([x-1, y] in noWall):
			x = x-2
			d = 3
			serialWrite(2)
			serialWrite(0)
			
		elif ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			serialWrite(0)
		
		elif ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			serialWrite(1)
		
	elif d == 3:
		if ((US[0] and US[3]) > 10) and not ([x, y-1] in wall or noWall):
			noWall.append([x, y-1])
			if not [x, y-2] in discovered:
				notDiscovered.append([x, y-2])
		elif not [x, y-1] in wall or noWall:
			wall.append([x, y-1])
			
		if ((US[2] and US[5]) > 10) and not ([x, y+1] in wall or noWall):
			noWall.append([x, y+1])
			if not [x, y+2] in discovered:
				notDiscovered.append([x, y+2])
		elif not [x, y+1] in wall or noWall:
			wall.append([x, y+1])
			
		if not (US[1] > 10) and not ([x-1, y] in wall or noWall):
			noWall.append([x-1, y])
			if not [x-2, y] in discovered:
				notDiscovered.append([x-2, y])
		elif not [x-1, y] in wall or noWall:
			wall.append([x-1, y])
			
		if (laserValue('B') > 10) and not ([x+1, y] in wall or noWall):
			noWall.append([x+1, y])
			if not [x+2, y] in discovered:
				notDiscovered.append(x+2, y)
		elif not [x+1, y] in wall or noWall:
			wall.append([x+1, y])
		
		##### DECIDING DIRECTION TO TURN ########################################
		if ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			serialWrite(3)
			serialWrite(0)
		
		elif ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			serialWrite(2)
			serialWrite(0)
			
		elif ([x-2, y] in notDiscovered) and ([x-1, y] in noWall):
			x = x-2
			d = 3
			serialWrite(0)
			
		elif ([x+2, y]) and ([x+1, y] in noWall):
			x = x+2
			d = 1
			serialWrite(1)
