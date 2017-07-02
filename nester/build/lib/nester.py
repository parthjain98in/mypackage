def printit(lists):
	for each in lists:
		if isinstance(each, list):
			printit(each)
		else:
			print(each)