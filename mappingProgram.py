#!/usr/local/bin/python3
from sensorProgram import *
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
start = []

def Mapping():
	##### MAPPING THE ROOM ######################################################
	if d == 0:
		if (laserValue('L') > 10) and ([x-1, y] in wall or noWall == False):
			noWall.append([x-1, y])
			notDiscovered.append([x-2, y])
		elif [x-1, y] in wall or noWall == False:
			wall.append([x-1, y])
			
		if (laserValue('R') > 10) and ([x+1, y] in wall or noWall == False):
			noWall.append([x+1, y])
			notDiscovered.append([x+2, y])
		elif [x+1, y] in wall or noWall == False:
			wall.append([x+1, y])
			
		if (laserValue('F') > 10) and ([x, y+1] in wall or noWall == False):
			noWall.append([x, y+1])
			notDiscovered.append([x, y+2])
		elif [x, y+1] in wall or noWall == False:
			wall.append([x, y+1])
			
		if (laserValue('B') > 10) and ([x, y-1] in wall or noWall == False):
			noWall.append([x, y-1])
			notDiscovered.append([x, y-2])
		elif [x, y-1] in wall or noWall == False:
			wall.append([x, y-1])
			
		##### DECIDING DIRECTION TO TURN ########################################
		if ([x-2, y] in notDiscovered) and ([x-1, y] in noWall):
			x = x-2
			d = 3
			turnLeft()
		
		elif ([x+2, y] in notDiscovered) and ([x+1, y] in noWall):
			x = x+2
			d = 1
			turnRight()
			
		elif ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			turnForward()
			
		elif ([y, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			turnBackwards()
		
		else:
			
	
	elif d == 1:
		if (laserValue('L') > 10) and ([x, y+1] in wall or noWall):
			noWall.append([x, y+1])
			notDiscovered.append([x, y+2])
			
		elif [x, y+1] in wall or noWall:
			wall.append([x, y+1])
			
		if (laserValue('R') > 10) and ([x, y-1] in wall or noWall):
			noWall.append([x, y-1])
			notDiscovered.append([x, y-2])
		elif [x, y-1] in wall or noWall:
			wall.append([x, y-1])
			
		if (laserValue('F') > 10) and ([x+1, y] in wall or noWall):
			noWall.append[x+1, y]
			notDiscovered.append([x+2, y])
		elif [x+1, y] in wall or noWall:
			wall.append([x+1, y])
			
		if (laserValue('B') > 10) and ([x-1 ,y] in wall or noWall):
			noWall.append([x-1, y])
			notDiscovered.append([x-2, y])
		elif [x-1, y] in wall or noWall:
			wall.append([x-1, y])
			
		##### DECIDING DIRECTION TO TURN########################################
		if ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			turnLeft()
		
		elif ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			turnRight()
		
		elif ([x+2, y] in notDiscovered) and ([x+1, y] in noWall):
			x = x+2
			d = 1
			turnForward()
			
		elif ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			x = x-2
			d = 3
			turnBackwards()
    	
	elif d == 2:
		if (laserValue('L') > 10) and ([x+1, y] in wall or noWall):
			noWall.append([x+1, y])
			if not [x+1, y] in discovered:
				notDiscovered.append([x+2, y])
		elif [x+1, y] in wall or noWall:
			wall.append([x+1, y])
			
		if (laserValue('R') > 10) and ([x-1, y] in wall or noWall):
			noWall.append([x-1, y])
			if not [x-1, y] in discovered:
				notDiscovered.append([x-2, y])
		elif [x-1, y] in wall or noWall:
			wall.append([x-1, y])
			
		if (laserValue('F') > 10) and ([x, y-1] in wall or noWall):
			noWall.append([x, y-1])
			notDiscovered.append([x, y-2])
		elif [x, y-1] in wall or noWall:
			wall.append([x, y-1])
			
		if (laserValue('B') > 10) and ([x, y+1] in wall or noWall):
			noWall.append([x, y+1])
		elif [x, y+1] in wall or noWall:
			wall.append([x, y+1])
			
		if ([x+2, y] in notDiscovered) and ([x+2, y] in noWall):
			x = x+2
			d = 1
			turnLeft()
			
		elif ([x-2, y] in notDiscovered) and ([x-1, y] in noWall):
			x = x-2
			d = 3
			turnRight()
			
		elif ([x, y-2] in notDiscovered) and ([x, y-1] in noWall):
			y = y-2
			d = 2
			turnForward()
		
		elif ([x, y+2] in notDiscovered) and ([x, y+1] in noWall):
			y = y+2
			d = 0
			turnBackwards()
		
	elif d == 3:
		if (laserValue('L') > 10) and ([x, y-1] in wall or noWall):
			noWall.append([x, y-1])
			if not [x, y-2] in discovered:
				notDiscovered.append([x, y-2])
		elif [x, y-1] in wall or noWall:
			wall.append([x, y-1])
			
		if (laserValue('R') > 10) and ([x, y+1] in wall or noWall):
			noWall.append([x, y+1])
			if not [x, y+2] in discovered:
				notDiscovered.append([x, y+2])
		elif [x, y+1] in wall or noWall:
			wall.append([x, y+1])
			
		if (laserValue('F') > 10) and ([x-1, y] in wall or noWall):
			noWall.append([x-1, y])
			if not [x-2, y] in discovered:
				notDiscovered.append([x-2, y])
		elif [x-1, y] in wall or noWall:
			wall.append([x-1, y])
			
		if (laserValue('B') > 10) and (map[str(x+1) + ',' + str(y)] == None):
			map[str(x+1) + ',' + str(y)] = noWall
		elif map[str(x+1) + ',' + str(y)] == None:
			map[str(x+1) + ',' + str(y)] = wall
			
		if (map[str(x) + ',' + str(y-2)] == None) and (map[str(x) + ',' + str(y-1)] == noWall):
			y = y-2
			d = 2
			turnLeft()
		
		elif (map[str(x) + ',' + str(y+2)] == None) and (map[str(x) + ',' + str(y+1)] == noWall):
			y = y+2
			d = 0
			turnRight()
			
		elif (map[str(x-2) + ',' + str(y)] == None) and (map[str(x-1) + ',' + str(y)] == noWall):
			x = x-2
			d = 3
			turnForward()
			
		elif (map[str(x+2) + ',' + str(y)] == None) and (map[str(x+1) + ',' + str(y)] == noWall):
			x = x+2
			d = 1
			turnBackwards()
