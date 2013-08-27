#Exercise 30 of Learn Python the Hardway
#Exercise done by Zander Best
#Learn Python the Hard way is Copyright (C) 2010 Zed. A. Shaw
#
#I'm concurrently learning Git along with Zed's Guide. 

people = 20
cars = 30
buses = 15

if cars > people:
	print "We should take the cars"
elif cars < people:
	print "We should not take the cars"
else:
	print "we cant make up our minds."

if buses > cars:
	print "thats too many buses"
elif buses < cars:
	print "Maybe we could take the buses?"
else:
	print "we're pretty damn indecisive"

if people > buses:
	print "Alright, take the bus"
else:
	print "Looks like we're staying home"