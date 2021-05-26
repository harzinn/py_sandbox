#import regular expressions
import re

#file check 
while True:
    fname = input('Enter file name or type \'done\' to quit: ' )
    if len(fname) < 1:
        fname = 'regex_sum_42.txt'
    if fname == 'done' :
        print('Quitting')
        quit()
    try:
        fh = open(fname)
        break
    except:
        print('Invalid filename, try again')
        continue

#run through the file line by line
numbersList = list()
for line in fh:
    line = line.rstrip()
    numbersList.append(re.findall('[0-9]+', line))

#flatten the list
newList = list()
for number in numbersList:
    for item in number:
        newList.append(item)

#get our sum and count
count = 0
sum = 0
for number in newList:
    sum = sum + int(number)
    count = count + 1

print(count)
print(sum)



        