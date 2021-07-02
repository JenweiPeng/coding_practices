# return the array if it is empty
# startIndex = 0 and endIndex = array length - 1
# if array[startIndex] is equal to toMove
# set array[startIndex] = array[endIndex]
# and set array[endIndex] = toMove
# then endIndex = endIndex - 1
# else (array[startIndex] is not equal to toMove])
# startIndex = startIndex
# repeat as long as startIndex is smaller than endIndex

def moveElementToEnd(array, toMove):
    if len(array) == 0:
        return array
	
    startIndex = 0
    endIndex = len(array) - 1
	
    while startIndex <= endIndex:
    	if array[startIndex] == toMove:
    	    array[startIndex] = array[endIndex]
    	    array[endIndex] = toMove
    	    endIndex -= 1
    	else:
    	    startIndex += 1
    
    return array

# time complexity: O(n) since the worst case we might need to traverse through all the elements
# space O(1)
