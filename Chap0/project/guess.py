from random import *

# Generate a random number between 1-20
rdm_number = randint(1,20)
# print (rdm_number)

for i in range(0,10):
	guess = input("Please guess the number (0-20):")
	try:
		guess_number = int(guess)

		if (guess_number > rdm_number):
			print ("It's too big. Your have %d chances left." % (9-i))
			#guess_number()

		elif(guess_number < rdm_number):
			print ("It's too small. Your have %d chances left." % (9-i))
		else:
			print ("You are right")
			exit(0)
	#	i = i + 1
	except ValueError:
		print("That's not an int!")
