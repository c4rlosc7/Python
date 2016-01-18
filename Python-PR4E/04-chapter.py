#----------------first example function------------------------
# def thing():
# 	print 'Hello'
# 	print 'Fun'

# thing()
# print 'Zip'
# thing()

# python functions, there are two kinds of functions in python.
# Built-in functions, that are provided as part of pytho
#Python-raw_input, type(), float(), int().
#functions that we define ourselves and then use
#we treat the built-in function names as "new" reserved words
#(i.e.,we avoid them as variable names).

#In Python a function is some reusable code that takes arguments(s)
#as input, does some computation, and then return a result or results

#we define a function using the def reserved word

#we call / invoke the function by using the function name,
#parenthese, and arguments in an expression.

#-----------------------------------------------------------
# def max(inp):
# 	blah
# 	blah
# 	for x in y:
# 		bla 
# 		bla

#----------------------------------------------------------
# x = 5
# print 'Hello'

# def print_lyrics():
# 	print "I'm a lumberjack, and I'm okay."
# 	print 'I spleep all night and I work all day.'

# print 'Yo'
# print_lyrics()
# x = x + 2
# print x 

#-----------------------------------------------------------
# def greet():
# 	return "Hello"

# print greet(), "Glenn"
# print greet(), "Sally"

#-------------Multiple Parameters / Arguments---------------
# def addtwo(a, b):
# 	added = a + b
# 	return added

# x = addtwo(3, 5)
# print x 
#-----------------------------------------------------------
def  computepay(hours, rate):
	#hours = float(raw_input('Enter Hours: '))
	#rate = float(raw_input('Enter Rate: '))
	pay = float((hours - 5) * rate + 5 * (rate + 5))
	print 'Pay',pay 

computepay(45, 10)
	

