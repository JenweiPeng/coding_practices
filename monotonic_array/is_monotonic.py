# if the array only has zero or one element, then the array is monotonic
# otherwise iterate through the array and find the trend
# if the array is monotonic, then the multiplication of two trends should always be positive
# for example, positive trend * positive trend, or negative trend * negative trend
# if the multiplication is negative, return False
def is_monotonic(array):
    array_length = len(array)
    if array_length <= 1:
    	return True
	
    start_index = 0
    trend = None
	
    while start_index < array_length - 1:
	# if two elements are the same, move on
        # otherwise, check trend
        if array[start_index] != array[start_index + 1]:
	    # current trend
            difference = array[start_index + 1] - array[start_index]
	    if trend is None:
		trend = difference
	    else:
		if trend * difference < 0:
		    return False
	start_index += 1
    return True

# Time: O(n)
# Space: O(1)
