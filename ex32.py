#Exercise 32 of Learn Python the Hardway
#Exercise done by Zander Best
#Learn Python the Hard way is Copyright (C) 2010 Zed. A. Shaw
#
#I'm concurrently learning Git along with Zed's Guide. 



i = 0 
numbers = [] #this is a list (array?)

while i < 6:
	print "At the top i %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers: 
	print num