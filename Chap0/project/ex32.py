# create lists
the_count = [1,2,3,4,5]
fruits = ['apple','oranges','pears','apricots']
change = [1,'penies',2, 'dimes',3,'quarters']

# print each item in the_count list
for number in the_count:
	print ("This is count %d" % number)
	
for fruit in fruits:
	print ("A fruit of type: %s" % fruit)
	
for i in change:
	print ("I got %r" % i)

# build an empty list
elements = []

# append items to the list
for i in range(0,6):
	print ("Adding %d to the list." %i)
	elements.append(i)

# print out each items in the new created list	
for i in elements:
	print("Element was: %d" % i)