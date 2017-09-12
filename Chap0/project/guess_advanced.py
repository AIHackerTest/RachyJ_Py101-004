import random

#generate the first random number
a = random.randint(1,9)

allowed_values = list(range(0,9))
allowed_values.remove(a)
b = random.choice(allowed_values)

allowed_values.remove(b)
c = random.choice(allowed_values)

allowed_values.remove(c)
d = random.choice(allowed_values)

correct_numbers = (a,b,c,d)
print(correct_numbers)


# ten chances
for n in range(0,10):

	guess = int(input("Pls input a four-digit number.Each digit is different. >"))
	a1 = int(guess/1000)
	b1 = int((guess-a1*1000)/100)
	c1 = int((guess-a1*1000-b1*100)/10)
	d1 = guess-a1*1000-b1*100-c1*10
	guess_numbers = (a1,b1,c1,d1)

	A = 0
	B = 0

	n = n+1

	#check each of the four digits
	for i in range(0,4):
		# if the number is correct
		if guess_numbers[i] in correct_numbers:
			#if the number and position is correct, A+1
			if (correct_numbers[i]==guess_numbers[i]):
				#print ("the position is correct")
				A +=1
			# if the position is wrong, B+!
			else:
				#print("wrong postion")
				B +=1

		# else if the number is wrong
		else:
			continue

	if(A==4):
		print("Good guess. You win!")
		exit(0)
	else:
		print(str(A)+'A'+str(B)+'B')
		print(("You have %d chances left") % (10-n))
