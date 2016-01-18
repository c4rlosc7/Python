#----------STRING--------------------------
#Using a while statement and an iteration variable, 
#and the len function, we can construct a loop to 
#look at each of the letters in a string individually

# fruit = 'banana'
# index = 0
# while index < len(fruit):
# 	letter = fruit[index]
# 	#print index, letter with index and letter
# 	print letter # only letter
# 	index = index + 1

#----------------------------------------------
# word = 'banana'
# countA = 0 
# countN = 0 
# for letter in word:
# 	if letter == 'a':
# 		countA = countA + 1 

# 	if letter == 'n':
# 		countN = countN + 1 	

# print 'letter A ',countA 
# print 'letter N ',countN

#----------------------------------------------
# s = 'monty python'
# print s[0:6]
# print s[6:20]

#----------------lower and capital (letter)-----

# greet = 'Hello Bob'
# zap = greet.lower() #lower miniscula (lower case)
# zap1 = greet.upper() #lower mayuscula (capital letter)
# print 'lower case ',zap
# print 'capital word ',zap1
#-------------------chance the letter----------
# greet = 'Hello Bob'
# nstr = greet.replace('o','@')
# print nstr

#-------------Stripping Whitespace------------
# greet = '        Hello Bob        '
# print greet.lstrip()
# print greet.rstrip()
# print greet.strip()

# line = 'Please have a nice day'
# print line.startswith('Please')
# print line.startswith('p')

data = 'From c4rlosc7@gmail.com Sat Jan  5 09:14:16 2008'
atpos = data.find('c')
print atpos

sppos = data.find(' ',atpos)
print sppos

host = data[atpos:sppos]
print host