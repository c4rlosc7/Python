# Create a new tuple
tuple1 = ("football", 10, 7.2, 8)
print(tuple1)

# Type - Tuple
print(type(tuple1))

# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])


# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
print(type(tuple1[3]))

# Negative index to get the value of the last element
print(tuple1[-1])


# Negative index to get the value of the second last element
print(tuple1[-2])

# Negative index to get the value of the third last element
tuple1[-3]

# Concatenate two tuples
tuple2 = tuple1 + ("hello", 11)
print(tuple2)


# SLICING

# Slice from index 0 to index 2
print(tuple2[0:2]) # ('football', 10)

# Slice from index 3 to index 5
print(tuple2[3:5]) # (8, 'hello')


# Length of tuple
print(len(tuple2)) 


# SORTING

# A sample tuple
tuple3 = (1, 4, 8, 0, 3, 2, 7, 12, 13, 21)
print(tuple3)

# Sort the tuple
tuple3_sorted = sorted(tuple3)
print(tuple3_sorted)



# Nested Tuple
# Create a nest tuple
nested_t =(1, 2, ("james", "ospina"), (7,10), ("cuadrado", (1, 2) ) )
print(nested_t)


# Print element on each index
print("Element 0 of Tuple: ", nested_t[0])
print("Element 1 of Tuple: ", nested_t[1])
print("Element 2 of Tuple: ", nested_t[2])
print("Element 3 of Tuple: ", nested_t[3])
print("Element 4 of Tuple: ", nested_t[4])

print("")

# Print element on each index, including nest indexes
print("Element 2, 0 of Tuple: ",   nested_t[2][0])
print("Element 2, 1 of Tuple: ",   nested_t[2][1])
print("Element 3, 0 of Tuple: ",   nested_t[3][0])
print("Element 3, 1 of Tuple: ",   nested_t[3][1])
print("Element 4, 0 of Tuple: ",   nested_t[4][0])
print("Element 4, 1 of Tuple: ",   nested_t[4][1])

# Print the first element in the second nested tuples
print(nested_t[2][1][0])

# Print the second element in the second nested tuples
print(nested_t[2][1][1])

# Print the first element in the second nested tuples
print(nested_t[4][1][0])

# Print the second element in the second nested tuples
print(nested_t[4][1][1])