#!/usr/local/bin/python3
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
	##### MAPPING THE ROOM ######################################################
	if d == 0:
		if (laserValue('L') > 10) and (map[str(x-1) + ',' + str(y)] == None):
			map[str(x-1) + ',' + str(y)] = noWall
		elif map[str(x-1) + ',' + str(y)] == None:
			map[str(x-1) + ',' + str(y)] = wall
			
		if (laserValue('R') > 10) and (map[str(x+1) + ',' + str(y)] == None):
			map[str(x+1) + ',' + str(y)] = noWall
		elif map[str(x+1) + ',' + str(y)] == None:
			map[str(x+1) + ',' + str(y)] = wall
			
		if (laserValue('F') > 10) and (map[str(x) + ',' + str(y+1)] == None):
			map[str(x) + ',' + str(y+1)] = noWall
		elif map[str(x) + ',' + str(y+1)] == None:
			map[str(x) + ',' + str(y+1)] = wall
			
		if (laserValue('B') > 10) and (map[str(x) + ',' + str(y-1)] == None):
			map[str(x) + ',' + str(y-1)] = noWall
		elif map[str(x) + ',' + str(y-1)] == None:
			map[str(x) + ',' + str(y-1)] = wall
			
		##### DECIDING DIRECTION TO TURN########################################
		if (map[str(x-2) + ',' + str(y)] == None) and (map[str(x-1) + ',' + str(y) == noWall]):
			x = x-2
			d = 3
			turnLeft()
		
		elif (map[str(x+2) + ',' + str(y)] == None) and (map[str(x+1) + ',' + str(y)] == noWall):
			x = x+2
			d = 1
			turnRight()
			
		elif (map[str(x) + ',' + str(y+2)] == None) and (map[str(x) + ',' + str(y+1)] == noWall):
			y = y+2
			d = 0
			turnForward()
			
		elif (map[str(x) + ',' + str(y-2)] == None) and ((map[str(x) + ',' + str(y-1)] == noWall)):
			y = y-2
			d = 2
			turnBackwards()
	
	elif d == 1:
		if (laserValue('L') > 10) and (map[str(x) + ',' + str(y+1)] == None):
			map[str(x) + ',' + str(y+1)] = noWall
		elif map[str(x) + ',' + str(y+1)] == None:
			map[str(x) + ',' + str(y+1)] = wall
			
		if (laserValue('R') > 10) and (map[str(x) + ',' + str(y-1)] == None):
			map[str(x) + ',' + str(y-1)] = noWall
		elif map[str(x) + ',' + str(y-1)] == None:
			map[str(x) + ',' + str(y-1)] = wall
			
		if (laserValue('F') > 10) and (map[str(x+1) + ',' + str(y)] == None):
			map[str(x+1) + ',' + str(y)] = noWall
		elif map[str(x+1) + ',' + str(y)] == None:
			map[str(x+1) + ',' + str(y)] = wall
			
		if (laserValue('B') > 10) and (map[str(x-1) + ',' + str(y)] == None):
			map[str(x-1) + ',' + str(y)] = noWall
		elif map[str(x-1) + ',' + str(y)] == None:
			map[str(x-1) + ',' + str(y)] = wall
			
		##### DECIDING DIRECTION TO TURN########################################
		if (map[str(x) + ',' + str(y+2)] == None) and (map[str(x) + ',' + str(y+1)] == noWall):
			y = y+2
			d = 0
			turnLeft()
		
		elif (map[str(x) + ',' + str(y-2)] == None) and (map[str(x) + ',' + str(y-1)] == noWall):
			y = y-2
			d = 2
			turnRight()
		
		elif (map[str(x+2) + ',' + str(y)] == None) and (map[str(x+1) + ',' + str(y)] == noWall):
			x = x+2
			d = 1
			turnForward()
			
		elif (map[str(x-2) + ',' + str(y)] == None) and (map[str(x-1) + ',' + str(y)] == noWall):
			x = x-2
			d = 3
			turnBackwards()
    	
	elif d == 2:
		if (laserValue('L') > 10) and (map[str(x+1) + ',' + str(y)] == None):
			map[str(x+1) + ',' + str(y)] = noWall
		elif map[str(x+1) + ',' + str(y)] == None:
			map[str(x+1) + ',' + str(y)] = wall
			
		if (laserValue('R') > 10) and (map[str(x-1) + ',' + str(y)] == None):
			map[str(x-1) + ',' + str(y)] = noWall
		elif (map[str(x-1) + ',' + str(y)] == None):
			map[str(x-1) + ',' + str(y)] = wall
			
		if (laserValue('F') > 10) and (map[str(x) + ',' + str(y-1)] == None):
			map[str(x) + ',' + str(y-1)] = noWall
		elif map[str(x) + ',' + str(y-1)] == None:
			map[str(x) + ',' + str(y-1)] = wall
			
		if (laserValue('B') > 10) and (map[str(x) + ',' + str(y+1)] == None):
			map[str(x) + ',' + str(y+1)] = noWall
		elif map[str(x) + ',' + str(y+1)] == None:
			map[str(x) + ',' + str(y+1)] = wall
			
		if (map[str(x+2) + ',' + str(y)] == None) and (map[str(x+1) + ',' + str(y)] == noWall):
			x = x+2
			d = 1
			turnLeft()
			
		elif (map[str(x-2) + ',' + str(y)] == None) and (map[str(x-1) + ',' + str(y)] == noWall):
			x = x-2
			d = 3
			turnRight()
			
		elif (map[str(x) + ',' + str(y-2)] == None) and (map[str(x) + ',' + str(y-1)] == noWall):
			y = y-2
			d = 2
			turnForward()
		
		elif (map[str(x) + ',' + str(y+2)] == None) and (map[str(x) + ',' + str(y+1)] == noWall):
			y = y+2
			d = 0
			turnBackwards()
		
	elif d == 3:
		if (laserValue('L') > 10) and (map[str(x) + ',' + str(y-1)] == None):
			map[str(x) + ',' + str(y-1)] = noWall
		elif map[str(x) + ',' + str(y-1)] == None:
			map[str(x) + ',' + str(y-1)] = wall
			
		if (laserValue('R') > 10) and (map[str(x) + ',' + str(y+1)] == None):
			map[str(x) + ',' + str(y+1)] = noWall
		elif map[str(x) + ',' + str(y+1)] == None:
			map[str(x) + ',' + str(y+1)] = wall
			
		if (laserValue('F') > 10) and (map[str(x-1) + ',' + str(y)] == None):
			map[str(x-1) + ',' + str(y)] = noWall
		elif map[str(x-1) + ',' + str(y)] == None:
			map[str(x-1) + ',' + str(y)] = wall
			
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
