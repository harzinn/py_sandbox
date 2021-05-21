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
    if 'From' not in ln : continue #skip lines without from in them
    if ln.startswith('From:') : continue #skip lines that start with From:
    ln = ln.split() # split the line into individual items
    emails.append(ln[1]) # append the email address to the emails list

#histogram creation
for email in emails:
    counts[email] = counts.get(email, 0) +  1

#figure out the most occuring word
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
