fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Invalid input')
    quit()

lst = list()

for line in fh:
    lineSplit = line.split()
    for word in lineSplit:
        if word in lst : continue
        lst.append(word)

lst.sort()
print(lst)

