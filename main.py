fname = input("Enter file name: ")
fh = open(fname)
searchTerm = input('What text are you looking for?: ')

count = 0
total = 0

for line in fh:
    total = total + 1
    if searchTerm not in line: continue
    count = count + 1

print(searchTerm, 'occured', count, 'times in this file out of', total, 'lines')  