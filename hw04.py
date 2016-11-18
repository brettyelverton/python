# CDT Brett Yelverton
# x97226
# CDT Cowley B-1 '19, CDT Cowley showed me how to use the pop command in problem three in order to
# extremely efficiently do the insert problem. West Point, NY 5OCT2016.
# Problem 1 :

def roulette_wheel(fitList):
    """
    >>> roulette_wheel([1, 2, 3, 4])
    [0.1, 0.3, 0.6, 1.0]
    >>> roulette_wheel([342, 325, 578, 123, 87, 435, 677])
    [0.133, 0.26, 0.485, 0.533, 0.567, 0.736, 1.0]
    >>> roulette_wheel([56, 87, 23, 45, 0, 23, 34])
    [0.209, 0.534, 0.62, 0.788, 0.788, 0.874, 1.001]
    """
    fitTotal = 0
    fitSolution = []
    for num in fitList:
        fitTotal = fitTotal + num
    xCount = 0
    for x in fitList:
        xCount += 1
        indSoln = fitList[xCount-1]/fitTotal
        fitSolution.append(indSoln)
    valCount=0
    for val in fitSolution:
        valCount+=1
        if valCount == 1:
            fitSolution[valCount] = round(fitSolution[valCount],3)
        else:
            fitSolution[valCount-1] = round((fitSolution[valCount -1] + fitSolution[valCount-2]),3)
    return fitSolution

def gen_child(pOne,pTwo,cross,mutation):
    """
    >>> gen_child([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], \
    3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    >>> gen_child([1, 0, 1, 1, 0, 1, 0, 1, 1, 1], \
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 1], \
    3, [0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
    >>> gen_child([1, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1], \
    8, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 1]
    
    """
    changedList = []
    indexCount = 0
    for var in pOne:
        if indexCount < cross:
            indexCount += 1
            changedList.append(var)
        else:
            break
    indexCount2 = 0
    for var2 in pTwo:
        if indexCount2 >= cross: 
            indexCount2 += 1
            changedList.append(var2)
        else:
            indexCount2 += 1
    entCount = -1	
    for ent in mutation:
        entCount += 1
        if ent == 1:
            if changedList[entCount] == 0:
                changedList[entCount] = 1
            elif changedList[entCount] == 1:
                changedList[entCount] = 0
	return changedList
	
def zipper_merge(dest,src):
	"""
	Test 1:
	>>> dest = [1, 2, 3, 4, 5]
	>>> src = [6, 7, 8, 9, 10]
	>>> zipper_merge(dest, src)
	>>> dest
	[1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
	>>> src
	[]

	Test 2:
	>>> dest = [1, 2, 3, 4]
	>>> src = [6, 7, 8, 9, 10, 11]
	>>> zipper_merge(dest, src)
	>>> dest
	[1, 6, 2, 7, 3, 8, 4, 9, 10, 11]
	>>> src
	[]

	Test 3:
	>>> dest = [1, 2, 3, 4, 5]
	>>> src = [6, 7]
	>>> zipper_merge(dest, src)
	>>> dest
	[1, 6, 2, 7, 3, 4, 5]
	>>> src
	[]

	Test 4:
	>>> dest = []
	>>> src = [2, 1, 5, 6]
	>>> zipper_merge(dest, src)
	>>> dest
	[2, 1, 5, 6]
	>>> src
	[]

	Test 5:
	>>> dest = [2, 1, 5, 6]
	>>> src = []
	>>> zipper_merge(dest, src)
	>>> dest
	[2, 1, 5, 6]
	>>> src
	[]

	Test 6:
	>>> dest = []
	>>> src = []
	>>> zipper_merge(dest, src)
	>>> dest
	[]
	>>> src
	[]
	"""
    index = 1
    while len(src) > 0:
        dest.insert(index, src.pop(0))
        index += 2

if __name__=='__main__':
    import doctest
    doctest.testmod()
