class Navigation:
	def closestCross():
		for a in range(0, len(crosses)):
			Value = crosses[a][0] - x
			crosses[a] = [crosses[a][0], crosses[a][1], abs(Value)]
		
		crosses.sort(key = lambda x: int(x[2]))
		found = False
		a = 0
		while found == False:
			if checkPossibility(crosses[a][0], crosses[a][1], crosses[a][2])
				found = True
				drive(crosses[a][0], crosses[a][1])
				
			else:fec
				a = a+1
