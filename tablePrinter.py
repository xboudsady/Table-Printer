tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]

def printTable(inputLists):
	# initialize the list "colWidths" with zeros equal to the length of the input list
	colWidth = [0] * len(inputLists)

	# iterate over the input list to find the longest word in each inner list
	# if its larger than the current value, set it as the new value
	for i in range(len(inputLists)):
		for j in range(len(inputLists[i])):
			colWidth[i] = len(inputLists[i][j])

	# assuming each inner list is the same length as the first, iterate over the input list
	# printing the x value from each inner list, right justified to its corresponding value

	for x in range(len(inputLists[0])):
		for y in range(len(inputLists)):
			print(inputLists[y][x].rjust(colWidth[y]), end = ' ')
		print(' ')

printTable(tableData)