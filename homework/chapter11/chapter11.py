fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'regex_sum_42.txt'

fh = open(fname)

for line in fh:
    print(line)