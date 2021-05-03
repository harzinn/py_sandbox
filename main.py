largest = None
smallest = None
inum = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        inum = int(num)
    except:
        print('Invalid input')
        continue
    #print(inum)
    if smallest is None:
        smallest = inum
        largest = inum
    elif inum < smallest:
        smallest = inum
    elif inum > largest:
        largest = inum



print("Maximum is", largest)
print("Minimum is", smallest)

