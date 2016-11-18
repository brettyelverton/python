#CDT Brett Yelverton : x97226
#CDT An, Beomjin B-1, '19', Cadet An showed me how to break up the tuple into two values in order to make use of the usual unmuttable
#data structure. Additionally CDT an showed me how he set up the enumerate for loop to allow the yMoves and xMoves to be tied together.
#Lastly CDT an showed me the structure for list comprehensions and how to change a for loop into a list comprehension allowing me to complete number 2.
#West Point, NY. 21 OCT 2016.
#CDT Baker, David B-4, '19', CDT Baker assisted me with number three on this homework set. He showed me his setup for the problem as well as 
# teaching me how to create a dictionary. He then taught me how to create the pop append structure that makes up the stack data type.
# His help allowed me to complete the problem and this homework assignment. He also showed me his setup for checking the stack created words
# with the txt file given to us. West Point, NY. 21 OCT 2016.



def knight_moves(location,board_size):
	"""
	>>> knight_moves((0, 0), 3)
	([(1, 2), (2, 1)], [['N', '.', '.'], ['.', '.', 'X'], ['.', 'X', '.']])
	>>> knight_moves((2, 1), 4)
	([(0, 0), (0, 2), (1, 3), (3, 3)], [['X', '.', 'X', '.'], ['.', '.', '.', 'X'], ['.', 'N', '.', '.'], ['.', '.', '.', 'X']])
	>>> knight_moves((3, 3), 8)
	([(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)], [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', 'X', '.', 'X', '.', '.', '.'], ['.', 'X', '.', '.', '.', 'X', '.', '.'], ['.', '.', '.', 'N', '.', '.', '.', '.'], ['.', 'X', '.', '.', '.', 'X', '.', '.'], ['.', '.', 'X', '.', 'X', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])

	"""
	board = []

	for x in range(board_size):
    	board.append(["."] * board_size)

	yVal,xVal=location
	board[yVal][xVal]='N'
	xMoves=(-1,1,2,2,1,-1,-2,-2)
	yMoves=(2,2,1,-1,-2,-2,-1,1)
	for num,movement in enumerate(xMoves):
		m=movement,yMoves[num]
		newY,newX = m
		if (yVal + newY) >= 0 and (yVal + newY) < board_size and (xVal + newX) >= 0 and (xVal + newX) < board_size:
			board[yVal+newY][xVal+newX]='X'


def true_comprehension_test(string):
	"""
	>>> true_comprehension_test('Pitter Patter')
	[160, 464, 228, 32]
	>>> true_comprehension_test('Mississippi!')
	[77, 460, 224, 33]
	"""
	checkList=[]
	listOne=[x for x in string if x not in "aeiou"]
	checkList=[y for y in listOne if y not in checkList]
	return([ord(letter)*listOne.count(letter) for position,letter in enumerate(checkList)])




def four_letter_words(digits):
	"""
	>>> four_letter_words('0000')
	[]
	>>> four_letter_words('7023')
	[]
	>>> four_letter_words('3542')
	['FLIC']
	>>> four_letter_words('9867')
	['YUMP']
	>>> four_letter_words('5279')
	['JASY']
	>>> four_letter_words('7569')
	['PLOW', 'PLOY', 'SLOW']
	"""
	input_file = open('fours.txt')
	assignment = {'0':' '.'1':' ','2':['A','B','C'],'3':['D','E','F'],'4':['G','H','I'],'5':['J','K','L'],'6':['M','N','U'],'7':['P','Q','R','S'],'8':['T','U','V'],'9':['W','X','Y','Z']}
	stack = []
	results = [] 
	for initial in string[0]:
		for i in assignment[initial]:
			stack.append(i)
	while stack != []:
		file = stack.pop()
		if len(file) >= 4:
			results.append(file)
		else:
			for i in string[len(file)]:
				for a in assignment[i]:
					stack.append(file+a)
	listOne = []
	listTwo = []
	for line in input_file:
		if word in line.split():
			listOne.append(word)
	for i in results:
		if i in listOne:
			listTwo.append(i)
	return(listTwo[,,-1])

