#------------------Loops and Iteration----------------------
# n = 5 
# while n > 0:
# 	print n
# 	n = n - 1

# print 'Blastoff!!!'
# print n

#--------------------------------------------------
# n = 5
# while n > 0:
# 	print 'Lather'
# 	print 'Rinse'
# 	n = n -1    #without sentence the loop is infinite
# print 'Dry off'

# n = 0
# while n > 0:
# 	print 'Lather'
# 	print 'Rinse'
# print 'Dry off'

# while True:
# 	line = raw_input('> ')
# 	if line[0] == '#':
# 		continue
# 	if line == 'done':
# 		break		
# 	print line
# print 'Done!!!'

#-------------------------A simple definite Loop-----
# for i in [5, 4, 3, 2, 1]:
# 	print i
# print 'Blastoff!!!'

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
# 	print 'Happy new year:', friend
# print 'Done!!!'

# print 'Before'
# for thing in [9, 41, 12, 3, 74, 15]:
# 	print thing
# print 'After'

# largest_so_far = -1
# print 'Before', largest_so_far
# for the_num in [9, 41, 12, 3, 74, 15]:
# 	if the_num > largest_so_far:
# 		largest_so_far = the_num
# 	print largest_so_far, the_num

# print 'After', largest_so_far

# count = 0
# sum = 0
# print 'Before', count, sum
# for value in [9, 41, 12, 3, 74, 15]:
# 	count = count + 1
# 	sum = sum + value
# 	print count, sum, value
# print 'After', count, sum, sum / count

# print 'Before'
# for value in [9, 41, 12, 3, 74, 15]:
# 	if value > 20:
# 		print 'Large number', value
# print 'After'

# found = False
# print 'Before', found
# for value in [9, 41, 12, 3, 74, 15]:
# 	if value == 3:
# 		found = True
# 	print found, value
# print 'After', found

#--------The "is" and "is not" Operators----------
smallest = None
print 'Before'
for value in [9, 41, 12, 3, 74, 15]:
	if smallest is None:
		smallest = value
	elif value < smallest:
		smallest = value
	print smallest, value
print 'After', smallest

