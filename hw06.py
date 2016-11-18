#CDT Yelverton, Brett
#x97226
"""
CITATION: CDT Cowley, Patrick , B-1 2019. CDT Cowley completely walked me through problem number one. I had previously been taking the problem straight up and
trying to unpack the tuple into lists. CDT Cowley pointed me in the direction of using dictionaries in order to achieve the end table and how one might go about setting the tuples
into the dictionary. I was then able to code down to where we begin to iterate through idTuple and assign the terrorist ID's across the first row and column of the table.
At this point CDT Cowley showed me how to get the program to iterate through and edit the board as such.
Finally CDT Cowley showed me how to get the program to iterate through the board and the original dictionary and
check for contacts between the two terrorists and input the X in that location.
.
CDT An, Beomjin, B-1 2019. CDT An reminded me to turn my numbers from strings into integers before attempting to sum them in problem 2.
Then in problem 3 CDT An reminded me that I needed to set a max value for the number of dots for my polygonal numbers. He also showed me how
to set the problem up in set notation as I was doing it in list notation before that.
.
For problem 4 I googled some code to look at how to manipulate dictionaries. I found this website
https://code.tutsplus.com/tutorials/how-to-merge-two-python-dictionaries--cms-26230 and through this was able to code a function that would merge my two sets of phone numbers
"""



import csv
from itertools import chain
from collections import defaultdict

def tango_links(idTuple, contactTuple):
	"""
	>>> tango_links(('t1', 't2', 't3', 't4', 't5'), (('t1', 't3'), ('t2', 't5'), ('t4', 't1'), ('t4', 't2')))
	[['-', 't1', 't2', 't3', 't4', 't5'], ['t1', '-', '-', 'X', '-', '-'], ['t2', '-', '-', '-', '-', 'X'], ['t3', '-', '-', '-', '-', '-'], ['t4', 'X', 'X', '-', '-', 	'-'], ['t5', '-', '-', '-', '-', '-']]

	>>> tango_links(('Alice', 'Bob', 'Carol', 'Dave', 'Eve'), (('Alice', 'Carol'), ('Bob', 'Eve'), ('Dave', 'Alice'), ('Dave', 'Bob')))
	[['-', 'Alice', 'Bob', 'Carol', 'Dave', 'Eve'], ['Alice', '-', '-', 'X', '-', '-'], ['Bob', '-', '-', '-', '-', 'X'], ['Carol', '-', '-', '-', '-', '-'], ['Dave', 		'X', 'X', '-', '-', '-'], ['Eve', '-', '-', '-', '-', '-']]

	>>> tango_links(('You', 'Need', 'More', 'Practice!'), (('You', 'More'), ('Practice!', 'You'), ('Practice!', 'Need')))
	[['-', 'You', 'Need', 'More', 'Practice!'], ['You', '-', '-', 'X', '-'], ['Need', '-', '-', '-', '-'], ['More', '-', '-', '-', '-'], ['Practice!', 'X', 'X', '-', 		'-']]
    """
	directory={}
    board = [['-' for x in range(len(idTuple)+1)] for y in range(len(idTuple)+1)]
    for idName in idTuple:
        directory[idName]=[]
    for contactPair in contactTuple:
        directory[contactPair[0]].append(contactPair[1])
    index = 0
    while index < len(idTuple):
        board[index + 1][0] = idTuple[index]
        board[0][index + 1] = idTuple[index]
        index += 1
    for tup in board[1:]:
        for x in directory[tup[0]]:
            tup[board[0].index(x)] = 'X'
    return board
        
def avg_selected(filename, column_name):
	"""
	>>> avg_selected('EPA_data.csv', 'City FE (Guide) - Conventional Fuel')
	20.3
    """
    file = open(filename, 'r')
    list_to_sum = []
    reader = csv.reader(file)
    iterable = 0
    for line_list in reader:
        if iterable == 0:
            index = line_list.index(column_name)
            iterable += 1 
        else:
            list_to_sum.append(int(line_list[index]))
    denom = len(list_to_sum)
    num = sum(list_to_sum)
    avg = num/denom
    ans = round(avg,1)
    return ans

def common_polygonals(num):
	"""
	>>> result = common_polygonals(10)
	>>> type(result) is set
	True
	>>> sorted(list(result))
	[1]

	>>> result = common_polygonals(100)
	>>> type(result) is set
	True
	>>> sorted(list(result))
	[1]

	>>> result = common_polygonals(1000)
	>>> type(result) is set
	True
	>>> sorted(list(result))
	[1]

	>>> result = common_polygonals(10000)
	>>> type(result) is set
	True
	>>> sorted(list(result))
	[1, 4186]

	>>>  result = common_polygonals(5786000)
	>>> type(result) is set
	True
	>>> sorted(list(result))
	[1, 4186, 5785101]

	>>> result = common_polygonals(5785101)
	>>> type(result) is set
	True
	>>> sorted(list(result))
	[1, 4186, 5785101]
    """
    triset = set()
    hexset = set()
    triskset = set()
    for n in range(1,num + 1):
        trinum = (n**2 + n)/2
        if trinum <= num:
            triset.add(round(trinum))
        hexnum = 2*(n**2)-n
        if hexnum <= num:
            hexset.add(round(hexnum))
        trisknum = (11*(n**2)-(9*n))/2
        if trisknum <= num:
            triskset.add(round(trisknum))
        if min(trinum,hexnum,trisknum) > num:
            break
    answer = triset&hexset&triskset
    return answer

def merge_phonebooks(mobile_nums,work_nums):
	"""
	>>> work_nums = {'Alice': '111-111-1111', 'Bill': '222-111-1111', 'Carol': '333-111-1111', 'Eve': '222-111-1111'}
	>>> mobile_nums = {'Alice': '111-222-2222', 'Carol': '333-222-2222', 'Dude': '444-222-2222', 'Eve': '222-222-2222'}
	>>> result = merge_phonebooks(work_nums, mobile_nums)
	>>> type(result) is dict
	True
	>>> sorted(list(result.items()))
	[('Alice', ['111-111-1111', '111-222-2222']), ('Bill', ['222-111-1111']), ('Carol', ['333-111-1111', '333-222-2222']), ('Dude', ['444-222-2222']), ('Eve', 			 ['222-111-1111', '222-222-2222'])]
    """
	d = defaultdict(list)
	for x, y in chain(mobile_nums.items(), work_nums.items()):
		d[x].append[y]
	return d

if __name__=='__main__':
    import doctest
    doctest.testmod()
