#Handle (open,read,write,close)
# xfile = open('mbox.txt')
# for cheese in xfile:
# 	print cheese
#---------File Handle as a Sequence----------------
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
# 	count = count + 1
# print 'Line Count:', count

#-----------Searching Through a File--------------
# fhand = open('mbox.txt')
# for line in fhand:
# 	if line.startswith('Date:'):
# 		print line

#---------Searching Through a File (fixed)----------
# fhand = open('mbox.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	if line.startswith('From:'):
# 		print line

#-------Using in to select lines-------------------
# fhand = open('mbox.txt')
# for line in fhand:
# 	line = line.rstrip()
# 	if not '@uct.ac.za' in line:
# 		continue
# 	print line

#-------Prompt for File Name----------------------
# fname = raw_input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
# 	if line.startswith('Subject:'):
# 		count = count + 1
# print 'There were', count, 'subject lines in', fname

#-------Bad File Names---------------------------
fname = raw_input('Enter the file name: ')
try:
	fhand = open(fname)
except:
	print 'File cannot be opened', fname
	exit()

count = 0
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
print 'There were', count, 'subject line in', fname






