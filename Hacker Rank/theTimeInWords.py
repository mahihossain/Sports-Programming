#!/bin/python3

import sys


h = int(input().strip())
m = int(input().strip())
timeDict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
            7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve',
            13:'thirteen', 14:'fourteen', 15:'quarter', 16:'sixteen', 17:'seventeen',
            18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two',
            23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six',
            27:'twenty seven', 28:'twenty eight', 29:'twenty nine', 30:'half'}
            


if m == 0:
    print(str(timeDict[h])+ ' o\' clock')
elif m == 15:
    print(str(timeDict[m])+ ' past '+timeDict[h])
elif m == 45:
    h %= 12
    h += 1
    print(str(timeDict[(60-m)])+ ' to '+timeDict[h])
elif m == 30:
    print(str(timeDict[m])+ ' past '+timeDict[h])
elif m > 30:
    h %= 12
    h += 1
    print(str(timeDict[(60-m)])+ ' minutes to '+str(timeDict[h]))
else:
    print(str(timeDict[60-(60-m)])+ ' minutes past '+str(timeDict[h]))
