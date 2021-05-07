email = 'nicholas.a.kruger2.ctr@mail.mil'

# find the domain and print slice
stpos = email.find('@')
raw = email[stpos+1:]

#remove leading and trailing whitespace if any
final = raw.strip()

print(final)