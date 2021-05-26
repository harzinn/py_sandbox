#import regular expressions
import re

#file check 
while True:
    fname = input('Enter file name: ')
    if len(fname) < 1:
        fname = 'regex_sum_42.txt'  
    try:
        fh = open(fname)
        break
    except:
        print('Invalid filename, try again')
        continue

numbersList = list()
newList = list()
count = 0
sum = 0

#run through the file line by line
for line in fh:
    line = line.rstrip()
    numbersList.append(re.findall('[0-9]+', line))

#flatten the list
for number in numbersList:
    if type(number) is list:
        for item in number:
            newList.append(item)

for number in newList:
    sum = sum + int(number)
    count = count + 1

print(count)
print(sum)



        