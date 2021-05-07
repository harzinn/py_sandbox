text = "X-DSPAM-Confidence:    0.8475"

#find the start position
spos = text.find(':')

#slice out the number starting with the starting position
extract = text[spos+1:]

#rip off the white space
refined = extract.strip()

#convert to float for project completion
final = float(refined)

#debug code
#print(spos)
#print(extract)

print(final)