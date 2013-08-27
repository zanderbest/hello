#Exercise 19 of Learn Python 12 the Hardway
#Exercise done by Zander Best
#Learn Python the Hard way is Copyright (C) 2010 Zed. A. Shaw
#
#I'm concurrently learning Git along with Zed's Guide. 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "you have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enopugh for a Party!"
	print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do the math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "Fuck absolution, lets get dynamic"
cheese_and_crackers(amount_of_cheese + 500, amount_of_crackers + 600)

print "This is cheese and crackers %r %r:" % cheese_and_crackers