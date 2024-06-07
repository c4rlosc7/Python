# defined string variable
string_sample = "Cristiano Ronaldo"

# Length of String
print(len(string_sample))

# Multiply by 3 * "Cristiano Ronaldo"
print(3 * string_sample)

# Upper case String
print(string_sample.upper())

# Lower case String
print(string_sample.lower())


name = "Messi"
age = 30
team = 'Barcelona'

# My name is John and I am 30 years old. And I play for Foolball Club Barcelona
print(f"My name is {name} and I am {age} years old. And I play for Foolball Club {team}.")

# My name is John and I am 30 years old. And I play for Foolball Club Barcelona
print("My name is {} and I am {} years old. And I play for Foolball Club {}.".format(name, age, team))

# My name is John and I am 30 years old. And I play for Foolball Club Barcelona
print("My name is %s and I am %d years old. And I play for Foolball Club %s." % (name, age, team))

x = 2
y = 20

# The sum of x and y is 22.
print(f"The sum of x and y is { x + y }.")

