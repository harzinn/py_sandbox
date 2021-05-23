# open a file with error checking, and default to mbox-short.txt for nothing
while True:
    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'mbox-short.txt'
    try:
        handle = open(fname)
        print('Opening', fname, '\n')
        break
    except:
        print('Invalid file, try again')
        continue

# split file into words and save it to list ls1
ls1 = list()
for line in handle:
    line = line.split()
    for word in line:
        ls1.append(word)

# create a dictionary dic1 of the words in list ls1 and build a histogram frequency of words
dic1 = dict()
for item in ls1:
    dic1[item] = dic1.get(item, 0) + 1

# using list comprehenstion, make a new list of dic1 so its sortable by value instead of key
newls = [ (v,k) for k,v in dic1.items() ]
newls.sort(reverse = True) # reverse sort so highest number first

print('The top 10 words are...')

for item in newls[:10]: # only look at the first 10 items in list newls
    print(item[1], 'occured', item[0], 'times!')
