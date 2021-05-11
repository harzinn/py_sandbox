# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue

    spos = line.find(':')
    spam = line[spos+1:]

    fspam = float(spam)

    total = total + fspam
    count = count + 1

avg = total/count

print('Average spam confidence:', avg)
