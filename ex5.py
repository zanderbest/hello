name = 'Zander Best' 	#Defining name
age = 24					#Defining age in years
height = 74				#defining height in inches
weight = 230				#defining weight in US pounds
eyes = 'blue'			#Defining eye color
teeth = 'white'			#defining teeth color? I was told to
hair = 'light brown'		#defining my hair color

#using %s to add a string
print "Let's talk about %s." % name

#using %d to add a ...decimal? digit?
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + weight + height)