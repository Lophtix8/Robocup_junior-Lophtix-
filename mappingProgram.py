from sensorProgram import *
from arduinoControl import *

x = 0
y = 0
d = 0

notDiscovered = 0
discovered = 1
wall = 3
noWall = 4
blackGround = 5
heatedTile = 6
letterTile = 7
start = 8

def Mapping():
	if d == 0:
		if laserValue('L') > 10:
			Map[str(x-1) + ',' + str(y)] = noWall
		else:
			Map[str(x-1) + ',' + str(y)] = wall
			
		if laserValue('R') > 10:
			Map[str(x+1) + ',' + str(y)] = noWall
		else:
			Map[str(x+1) + ',' + str(y)] = wall
			
		if laserValue('F') > 10:
			Map[str(x) + ',' + str(y+1)] = noWall
		else:
			Map[str(x) + ',' + str(y+1)] = wall
			
		if laserValue('B') > 10:
			Map[str(x) + ',' + str(y-1)] = noWall
		else:
			Map[str(x) + ',' + str(y-1)] = wall
			
	elif d == 1:
		if laserValue('L') > 10:
			Map[str(x) + ',' + str(y+1)] = noWall
		else:
			Map[str(x) + ',' + str(y+1)] = wall
			
		if laserValue('R') > 10:
			Map[str(x) + ',' + str(y-1)] = noWall
		else:
			Map[str(x) + ',' + str(y-1)] = wall
			
		if laserValue('F') > 10:
			Map[str(x+1) + ',' + str(y)] = noWall
		else:
			Map[str(x+1) + ',' + str(y)] = wall
			
		if laserValue('B') > 10:
			Map[str(x-1) + ',' + str(y)] = noWall
		else:
			Map[str(x-1) + ',' + str(y)] = wall
    	
	elif d == 2:
		if laserValue('L') > 10:
			Map[str(x+1) + ',' + str(y)] = noWall
		else:
			Map[str(x+1) + ',' + str(y)] = wall
			
		if laserValue('R') > 10:
			Map[str(x-1) + ',' + str(y)] = noWall
		else:
			Map[str(x-1) + ',' + str(y)] = wall
			
		if laserValue('F') > 10:
			Map[str(x) + ',' + str(y-1)] = noWall
		else:
			Map[str(x) + ',' + str(y-1)] = wall
			
		if laserValue('B') > 10:
			Map[str(x) + ',' + str(y+1)] = noWall
		else:
			Map[str(x) + ',' + str(y+1)] = wall
		
	elif d == 3:
		if laserValue('L') > 10:
			Map[str(x) + ',' + str(y-1)] = noWall
		else:
      			Map[str(x) + ',' + str(y-1)] = wall
			
		if laserValue('R') > 10:
			Map[str(x) + ',' + str(y+1)] = noWall
		else:
			Map[str(x) + ',' + str(y+1)] = wall
			
		if laserValue('F') > 10:
			Map[str(x-1) + ',' + str(y)] = noWall
		else:
			Map[str(x-1) + ',' + str(y)] = wall
			
		if laserValue('B') > 10:
			Map[str(x+1) + ',' + str(y)] = noWall
		else:
			Map[str(x+1) + ',' + str(y)] = wall
