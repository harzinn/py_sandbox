#fname = input('Enter file name: ')

while True:
    fname = input('Enter file name: ')
    try:
        handle = open(fname)
        break
    except:
        print('Invalid file, try again')
        continue

ls1 = list()
dic1 = dict()

for line in handle:
    line = line.split()
    for word in line:
        ls1.append(word)

for item in ls1:
    dic1[item] = dic1.get(item, 0) + 1

newls = [ (v,k) for k,v in dic1.items() ]

newls.sort(reverse = True)

print('The top 10 words are...')

for item in newls[:10]:
    print(item[1], 'occured', item[0], 'times!')
