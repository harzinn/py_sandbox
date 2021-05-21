name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emails = list()
counts = dict()
bigword = None
bigcount = None

#parse the file and append email address in From (not From:) lines
for ln in handle:
    if 'From' not in ln : continue 
    if ln.startswith('From:') : continue 
    ln = ln.split() 
    emails.append(ln[1]) 

#histogram creation
for email in emails:
    counts[email] = counts.get(email, 0) +  1

#figure out the most occuring word
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
