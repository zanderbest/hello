#Exercise 31 of Learn Python the Hardway
#Exercise done by Zander Best
#Learn Python the Hard way is Copyright (C) 2010 Zed. A. Shaw
#
#I'm concurrently learning Git along with Zed's Guide. 

print "You enter a dark room with two doors. Do you go through door #1 or #2?"

door = raw_input("> ") #remember, the attrib here is the prompt you see

if door == "1":	#if True...
	print "There's a giant bear here eating a cake. What do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "the bear eats your face off. Good Job!"
	elif bear == "2":
		print "the bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

	
