#Exercise 32 of Learn Python the Hardway
#Exercise done by Zander Best
#Learn Python the Hard way is Copyright (C) 2010 Zed. A. Shaw
#
#I'm concurrently learning Git along with Zed's Guide. 

def iterate(r):  	#defines iterate func with 1 argument: r
	n = 0			#defines the variable we will iterate: n
	numbers = [] 	#defines a list where we store results: numbers
	i = input("Choose a number: ")
	print i
	while n <= r:	#For each time n is less than r (our restraint)
		print n 	#print the value of n
		numbers.append(n) #expand the list size and store the latest value of n
		print numbers #print the list as it stands now
		n += i		#finally iterate n by 1, and then repeat this while loop



iterate(6) 			#call the function, pass r (the restraint) as 6