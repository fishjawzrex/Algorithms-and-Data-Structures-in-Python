'''THIS IS AN EXERCISE TO DEMOSTRATE THE USE OF 
BOTH THE RECURSION AND MEMOIZATION TECHNIQUES'''
frame = {} #dictionary to be used for memoization

def fib(n):
	if  n in frame: #check to see if n is in dictionary
		return frame[n]#if n is in dict, return value, and exit
	if n == 1: #base case 1
		value = 1
	elif n == 2: #base case 2
		value = 1
	elif n > 2:
		value = fib(n-1) + fib(n-2)#main recursive function
		frame[n] = value # save n and corresponding fib_no in hash table
	return value # note that we return at the end of the function, all others were subbed with "value" variable.
	
print fib(10)