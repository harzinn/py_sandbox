name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

times = list()
hours = list()
hoursHisto = dict()

for line in handle:
    if 'From' not in line: continue
    if 'From: ' in line: continue
    line = line.split()
    times.append(line[5]) #add the time column to a list

for time in times:
    time = time.split(':') #split the list to find H:M:S
    hours.append(time[0]) # extract the hours collumn to a new list

#create a histogram of our extracted hours
for hour in hours:
    hoursHisto[hour] = hoursHisto.get(hour, 0) + 1

#make a new list from the dictionary and sort it by hours
timelist = [ (k,v) for k,v in hoursHisto.items() ]
timelist.sort()

for time, count in timelist:
    print(time,count)
