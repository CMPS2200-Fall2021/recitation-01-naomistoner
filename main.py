"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	if right >= left:
		middle = (left+right)//2
		if key == mylist[middle]:
			return middle
		if key < mylist[middle]:
			return _binary_search(mylist, key, left, (middle-1))
		if key >= mylist[middle]:
			return _binary_search(mylist, key, (middle+1), right)
	return -1

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,3,5,9,12,33], 12) == 4
	assert binary_search([-23,-2,44,76], -2) == 1
	### TODO: add two more tests here.


def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds.
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO
	#get time at start
	t0 = time.time()
	#call function (search_fn)
	#list and key are correct
	#issue is that search_fn is being read as an int instead of a Functions
	search_fn(mylist, key)
	#get time after
	t1 = time.time()
	#return time as milli
	time_total = t1-t0
	return 1000*time_total


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order.

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	### TODO
	#
	#print(sizes[0])
	#list to be returned
	ret_list = []

	for o in range(len(sizes)):
		#the length of the list = n
		n = int(sizes[o])
		#create lists to search
		search_list = []
		for i in range(int(sizes[o])):
			search_list.append(i)

		#variables to hold search times
		lin_search_time = time_search(linear_search, search_list, -1)
		bin_search_time = time_search(binary_search, search_list, -1)

		#create tuple and add to list
		search_tuple = (n, lin_search_time, bin_search_time)
		ret_list.append(search_tuple)
	return ret_list
def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
print_results(compare_search())
