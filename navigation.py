class Navigation:
	def closestCross():
		for a in range(0, len(cross)):
			Value = cross[a][0] - x
			cross[a] = [cross[a][0], cross[a][1], abs(Value)]
		
		cross.sort(key = lambda x: int(x[2]))
		found = False
		a = 0
		while found == False:
			if checkPossibility(cross[a][0], cross[a][1], cross[a][2])
				found = True
				drive(cross[a][0], cross[a][1])
				
			else:
				a = a+1