def num_letters(n_rows,n_columns):
    return n_rows*n_columns-((n_rows-2)*(n_columns-2))
assert num_letters(3,4) == 10
assert num_letters(4,13) == 30
assert num_letters(4,4) == 12
import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = []
reverse_column=[]
reverse_row=[]
rows, columns = data.shape

row_1=data[0,:]
column_1=data[1:columns-1,0]
row_last = data[rows-1,:columns-1]
column_last = data[1:,columns-1]

for term in row_1:
    words.append(str(term))

for term in column_last:
    words.append(str(term))

i = 2
while i<=columns:
    words.append(str(data[rows-1,-i]))
    i=i+1

i = 2
while i<rows:
    words.append(str(data[-i,0]))
    i=i+1

    

    
print(words) #check that you collected all the letters in your data file
assert len(words) == num_letters(rows,columns)

words = []
temp_word=[]
reverse_column=[]
reverse_row=[]
rows, columns = data.shape
first_letter=''

row_1=data[0,:]
column_1=data[1:columns-1,0]
row_last = data[rows-1,:columns-1]
column_last = data[1:,columns-1]

for term in row_1:
    if len(temp_word) == 0:
        first_letter = term
    if len(temp_word) == 0 or len(temp_word) == 1:
        temp_word.append(term)
    elif len(temp_word) == 2 and temp_word[1] == '':
        temp_word[1] = term
        words.append(temp_word[0]+temp_word[1])
        temp_word[0] = temp_word[1]
        temp_word[1] = ''
    else:
        words.append(temp_word[0]+temp_word[1])
        temp_word[0] = temp_word[1]
        temp_word[1] = term
        words.append(temp_word[0]+temp_word[1])
        temp_word[0] = temp_word[1]
        temp_word[1] = ''
#I'm almost positive I did this in the worst way possible

for term in column_last:
    temp_word[1] = term.rstrip()
    words.append(temp_word[0]+temp_word[1])
    temp_word[0] = temp_word[1]
    temp_word[1] = ''

    

i = 2
while i<=columns:
    temp_word[1] = data[rows-1,-i].rstrip()
    words.append(temp_word[0]+temp_word[1])
    temp_word[0] = temp_word[1]
    temp_word[1] = ''
    i=i+1

    
i = 2
while i<rows:
    temp_word[1] = data[-i,0]
    words.append(temp_word[0]+temp_word[1])
    temp_word[0] = temp_word[1]
    temp_word[1] = ''
    i=i+1
temp_word[1] = first_letter
words.append(temp_word[0]+temp_word[1])
print(words)

