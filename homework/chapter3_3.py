score = input("Enter Score between 0.0 and 1.0 for Grade Letter: ")

#lets make sure no nasty input gets in here for an exception
try:
    fscore = float(score)
except:
    fscore = -1

#lets look at the grades and print something
if (fscore > 1.0) or (fscore < 0.0):
    print('Bzzt, try again with a valid number')
elif fscore >= .9:
    print('A')
elif fscore >= .8:
    print('B')
elif fscore >= .7:
    print('C')
elif fscore >= .6:
    print('D')
else:
    print('F')