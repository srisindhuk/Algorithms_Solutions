import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
        # Write your code here
        acount = Counter(s)
        flag = "YES"
        removalcount = 0
        newlist = list(acount.values())
        mincount = min(newlist)
        maxcount = max(newlist)

        if mincount == maxcount or newlist.count(mincount)==1:
            return "YES"
        if maxcount - mincount > 1:
            return "NO"
        for vals in acount.values():
            if vals == mincount:
                flag = "YES"
            elif vals - 1 == mincount:
                flag = "YES"
                removalcount += 1
                if removalcount >= 2:
                    return "NO"

            else:
                return "NO"
        return flag

if __name__ == '__main__':

    #s = input()
    s = "xxxaabbccrry"
    result = isValid(s)
    print(result)


