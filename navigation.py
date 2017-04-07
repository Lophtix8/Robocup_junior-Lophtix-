class Navigation:
	def closestCross():
		for a in range(0, len(crosses)):
			Value = int(crosses[a][0]) - x
			Value2 = int(crosses[a][1]) - y
			crosses[a] = [crosses[a][0], crosses[a][1], Value, Value2]
		
		crosses.sort(key = lambda x: int(x[2]))
		found = False
		a = 0
		while found == False:
			if checkPossibility(crosses[a][0], crosses[a][1], Value, x, 0)
				found = True
				
			else:
				a = a+1

	def checkPossibility(a, b, c, d, e):
		if c == 0:
			return False
		
		if c > 0:
			result = True
			for f in range(d+1, abs(c)):
				if [f, y] in noWall
					
				
				else:
					result = False
			
			if result = True:
				return True
