# Conditional Step (<,<=,==,>=,>,!=)
# x = 5
# if x == 5:
# 	print 'Equals 5'

# if x > 4:
# 	print 'Greater than 4'	

# if x >= 5:
# 	print 'Greater than or Equals 5'

# if x < 6: print 'Less than 6'
# if x <= 5:
# 	print 'Less than or Equals 5'

# if x != 6:
# 	print 'Not equal 6'

#---------------Nested Decisions------------------------
# x = 5
# if x > 2:
# 	print 'Bigger than 2'
# 	print 'Still bigger'
# print 'Done with 2'

# for i in range(5):
# 	print i
# 	if i > 2:
# 		print 'Bigger than 2'
# 		print 'Done with i', i
# 	print 'All Done'

#---------------Two-way Decisions------------------------
# x = 4
# if x > 2:
# 	print 'Bigger'
# else:
# 	print 'Smaller'

# print 'All done'

#---------------Multi-way-------------------------------
# x = 4
# if x < 2:
# 	print 'Small'
# elif x < 10:
# 	print 'Medium'
# else:
# 	print 'LARGE'
# print 'All Done'

#---------------Multi-way Puzzles-------------------------
# x = 4 
# if x < 2:
# 	print 'Below 2'
# elif x >= 2:
# 	print 'Two or more'
# else:
# 	print 'Something else'

#----------------The try / except Structure---------------
# if the code in the TRY works-the EXCEPT is skipped
# if the code in the TRY fails-it jumps to the EXCEPT section


# Exercise 45 10
hours = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
pay = (hours - 5) * rate + 5 * (rate + 5)
print 'Pay',pay 

# Exercise 
# Rewrite your pay program using try and except so 
# that your program handles non-numeric input 
# gracefully.
hours = raw_input('Enter a number: ')
rate = raw_input('Enter Rate: ')
try:
	aux_hours = float(hours)
	aux_rate = float(rate)
except:
	aux_hours = -1
	aux_rate  = -1

if aux_hours > 0:
	if aux_rate > 0:
		print 'Nice work, you pay', (aux_hours - 5) * aux_rate + 5 * (aux_rate + 5)
else:
	print 'Not a number'






















