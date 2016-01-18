# Tuples

# fhand = open('romeo.txt')
# counts = dict()
# for line in fhand:
# 	words = line.split()
# 	for word in words:
# 		counts[word] = counts.get(word, 0) + 1

# lst = list()
# for key, val in counts.items():
# 	lst.append((val,key))

# lst.sort(reverse=True)

# for val, key in lst[:10]:
# 	print key, val

#------ expression regular ----------
# using re.search() like find()
#import re 

# hand = open('mbox.txt')
# for line in hand:
# 	line = line.rstrip()
# 	#if re.search('From:', line):
# 	if line.find('From:') >= 0:
# 		print line 

#----using re.search() like startswith()
# import re 
# hand = open('mbox.txt')
# for line in hand:
# 	line = line.rstrip()
# 	#if re.search('^From:', line):
# 	if line.startswith('From:'):
# 		print line 






