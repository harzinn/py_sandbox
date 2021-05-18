testString = input('Enter your string: ')
testList = list()
testIndex = list()

testList = testString.split()

print(testList)

for obj in testList:
    testIndex.append(testList.index(obj))

print(testIndex)

