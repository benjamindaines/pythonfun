# This code is messy as fuck.... I know.
# 
# What we have here is a simple guessing game.  The computer will roll 2 die,
# add them together, and the user is to guess what the sum of the two die is.
#
# If the user is correct they are awareded points based on the number of 
# combinations possible to get that number with two die. 
#
# The running score is saved in a file called 'save'.
#
# I am planning on adding a loop to allow the user to play again without
# needing to re execute the script.  Perhaps some wagering could be put
# into play here as well.  
#
# The probability of each number could probably be calculated using the script,
# however I do not know how to do that yet, so I am hard coding the possible 
# point values. 
#
# I will probably make this game more complex as I learn more python.

# Here I import the 'random' module and 'exists'.  These are essential to the 
# operation of the game. 
import random
from os.path import exists

# The variables 'd1' and 'd2' represent the two die.
d1 = random.randint(1, 6)	# Random number generated between 1 and 6
d2 = random.randint(1, 6)	# Random number generated between 1 and 6

# This section deals with the save file.  Mainly checking whether it exists,
# creating it if it doesn't, and loading the contents if it does.
the_file = 'save'
does_it = exists(the_file)

if does_it == False:
	save = open(the_file, 'w')
	save.write('0')
	save.close()

saved = open(the_file, 'r+')
points = int(saved.read())	# Loads the contents of 'save' to a variable
saved.seek(0)

# This is the sum of both die and will be used to determin winning or losing.
num = int(d1 + d2)

print 
print "I have rolled two dice... what do you predict the sum of them will be?"
guess = int(raw_input('??? '))	# The user's guess 


if not (guess >= 2 and guess <= 12):	# Makes sure user didn't fuck up.
	print
	print "You do know that die will only add to number between 2 and 12 right...?"

# This section deals with scoring. Again, this can probably be slimmed down.
elif num == 2:
	pp = 6
	
elif num == 3:
	pp = 5
	
elif num == 4:
	pp = 4
	
elif num == 5:
	pp = 3
	
elif num == 6:
	pp = 2
	
elif num == 7:
	pp = 1
	
elif num == 8:
	pp = 2
	
elif num == 9:
	pp = 3
	
elif num == 10:
	pp = 4
	
elif num == 11:
	pp = 5
	
elif num == 11:
	pp = 6
	
elif num == 12:
	pp = 7

# Here we actually see if the user won or lost.  We also deal with writing the
# points to 'save' here. 
if num == guess:
	print
	print "Good Job!  You guessed correctly.  The die add to %d." % num
	print "You've won %d points!" % pp
	points = points + pp
	print "You now have %d points!" % points
	points = str(int(points))
	#save = open.the_file(
	saved.write(points)

else:
	print
	print "Sorry, you lose.  You have %d points" % points
	print "The number was.... %d" % num

# Makes sure the 'save' file is closed before exiting. 
# Extra print for nice formatting.
saved.close()
print
