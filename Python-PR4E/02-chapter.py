#type int, float, double, string
x_int  = 1
print type (x_int)

x_float  = 1.2
print type (x_float)

# Type Conversions
i = 42
print type(i)
f = float(i)
print f

# String Conversions
sval = '123'
print type(sval)

ival = int(sval)
print ival

# User Input 
#name = raw_input ('Who are you ')
#print 'welcome dear lord', name

# User Input 
#inp = raw_input('Europe floor ?')
#usf = int(inp) + 1
#print 'US floor', usf

# String Operations
print 'abc' + '123'

print 'Hi' * 5

# Example 
hours = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
pay = hours * rate
print 'Pay',pay 