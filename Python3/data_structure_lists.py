# Create a list
my_list = ["Cristiano Ronaldo", 7, 1986]
print(my_list)


# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',my_list[0], '\n Negative:' , my_list[-3])
print('the same element using negative and positive indexing:\n Postive:',my_list[1], '\n Negative:' , my_list[-2])
print('the same element using negative and positive indexing:\n Postive:',my_list[2], '\n Negative:' , my_list[-1])

my_list2 = ["Cristiano Ronaldo", 7.1, 1982, "CR", 1]
print(my_list2)

# Slicing
print(my_list2[3:5])

# Extend to add elements to list
my_list3 = ["Cristiano Ronaldo", 7.1, 1982, "CR", 1]
my_list3.extend(['Rock', 11])
print(my_list3)


# Append to add elements to list
my_list4 = ["Cristiano Ronaldo", 7.1, 1982, "CR", 1]
my_list4.append(['Rock', 11])
print(my_list4)

# Change the element based on the index
my_list5 = ["Messi", 10, 11.2]
print('Before change:', my_list5)
my_list5[0] = 'Lionel Messi'
print('After change:', my_list5)

# Delete the element based on the index
print('Before change:', my_list5)
del(my_list5[0])
print('After change:', my_list5)

# Split the string, default is by space
split_test = 'Lionel Andrés Messi Cuccittini'.split()
print(split_test)

# Split the string by comma
split_test2 = 'A,B,C,D'.split(',')
print(split_test2)

# COPY AND CLONE LISTS
# Copy (copy by reference) the list A

copy_list = my_list5
print('my_list5:', my_list5)
print('copy_list:', copy_list)

# Clone (clone by value) the list A
my_list6 = my_list5[:]
print(my_list6)

# Count
my_list = [1, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2) 
print(count) 
print(my_list)
print(my_list[1])

# Pop
my_list7 = [10, 20, 30, 40, 50] 
removed_element = my_list7.pop(2) # Removes and returns the element at index 2 
print(removed_element) 

# Remove
my_list8 = [10, 20, 30, 40, 50] 
my_list8.remove(30) # Removes the element 30 
print(my_list8)

# Reverse
my_list9 = [1, 2, 3, 4, 5] 
my_list9.reverse() 
print(my_list9) 
