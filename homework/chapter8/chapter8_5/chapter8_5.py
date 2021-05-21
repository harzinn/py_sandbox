fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
selection = list()

for line in fh:
    line = line.rstrip()
    if 'From' not in line : continue
    if line.startswith('From: ') : continue
    search = line.split()
    if line.startswith('From'):
        selection.append(search[1])
        count = count + 1

for email in selection:
    print(email)
    
print("There were", count, "lines in the file with From as the first word")