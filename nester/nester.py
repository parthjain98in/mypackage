def printit(lists, tab):
	for each in lists:
		if isinstance(each, list):
			printit(each,tab+1)
		else:
				for c in range(tab):
						print("\t",end='')
				print(each)
