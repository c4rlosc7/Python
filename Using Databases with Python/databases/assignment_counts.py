import sqlite3

conn = sqlite3.connect('assignmentorg.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
#CREATE TABLE Counts (email TEXT, count INTEGER)

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split('@')
    org = pieces[1]
    #print org
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    try: 
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
    except:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org, ))        

    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

