def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
	total_waiting_time = 0
	N = len(queries)
	# note: the waiting time of a task will be executed again
	# when we process a new task. for example, if the waiting time
	# of current task is T, and there are N tasks left.
	# then, this taks will be calculated for N more times.
	# we can use this logic to calculate the total waiting time.
	for idx, waiting_time in enumerate(queries):
		# Total number of queries, N = len(queries)
		# idx: 0, number of queries left: N - 1, waiting time of queries[0] will be executed again for N - 1 more times.
		# idx: 1, number of queries left: N - 2, waiting time of queries[1] will be executed again for N - 2 more times.
		# idx: 2, number of queries left: N - 3, waiting time of queries[2] will be executed again for N - 3 more times.
		# and so on...
		number_of_queries_left = N - (idx + 1)
		total_waiting_time += waiting_time * number_of_queries_left
		
	return total_waiting_time

# time complexity: the fastest time for sorting will be O(nlogn), then the for loop will take O(n)
# so the total time complexity is O(nlogn + n)
# and because nlogn is greater than n, so we can reduce to O(nlogn)

# space complexity: we dont need extra space, we are using constant space for this problem, so the 
# space complexity is O(1)
