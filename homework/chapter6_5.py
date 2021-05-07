text = "X-DSPAM-Confidence:    0.8475"

#find the start position
spos = text.find('0')

#slice out the number starting with the starting position
extract = text[spos:]

#convert to float for project completion
final = float(extract)

#debug code
#print(spos)
#print(extract)

print(final)