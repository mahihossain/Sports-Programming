x = int(input())
inputDict = {}
for _ in range(x):

    strInput = str(input())
    inputList = list(strInput.split(' '))
    dictList = [0,0,0]

    dictList = inputList[1:]

    for i in range(3):
        dictList[i] = float(dictList[i])

    inputDict[inputList[0]] = dictList

x = str(input())

average = (sum(inputDict[x])) / 3.0

print('{:.2f}'.format(average))
    
