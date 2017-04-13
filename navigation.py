class Navigation:
	def closestCross():
		for a in range(0, len(crosses)):
			Value = int(crosses[a][0]) - x
			Value2 = int(crosses[a][1]) - y
			crosses[a] = [crosses[a][0], crosses[a][1], Value, Value2]
		
		crosses.sort(key = lambda x: abs(int(x[2])))
		found = False
		checkingValue = 0
		##### Checking for the closest cross x-vise ############################
		while found == False:
			if int(crosses[checkingValue][3]) == 0 and checkPossibility(crosses[checkingValue][0], crosses[checkingValue][1], Value, x, 0) and crosses[checkingValue][2] != 0:
				found = True
				closestXCross = crosses[checkingValue]
				
			else:
				checkingValue = checkingValue+1
				
		##### Checking for the closest cross y-vise ############################
		found = False
		checkingValue = 0
		while found == False:
			if int(crosses[checkingValue][2]) == 0 and checkPossibility(crosses[checkingValue][0], crosses[checkingvalue][1], Value2, y, 1) and crosses[checkingValue][3] != 0:
				found = True
				closestYCross = crosses[checkingValue]
				
			else:
				checkingValue = checkingValue+1

	def checkPossibility(a, b, c, d, e):
		if c == 0:
			return False
		
		if c > 0 and e == 0:
			result = True
			for f in range(d+1, c):
				if ([f, y] not in noWall) and ([f, y] in wall):
					result = False
			
			if result = True:
				return True
			
		elif c < 0 and e == 0:
			result = True
			for f in range(d-1, c, -1):
				if ([f, y] not in noWall) and ([f, y] in wall):
					result = False
			
			if result = True:
				return True
			
		if c > 0 and e == 1:
			result = True
			for f in range(d+1, c):
				if ([x, f] not in noWall) and ([x, f] in wall):
					result = False
			
			if result = True:
				return True
			
		elif c < 0 and e == 1:
			result = True
			for f in range(d-1, c, -1):
				if ([x, f] not in noWall) and ([x, f] in wall):
					result = False
			
			if result = True:
				return True
