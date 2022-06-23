import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
def makeAnagramwithcouter(a,b):
    acount= Counter(a)
    bcount = Counter(b)
    acount.subtract(bcount)
    print(sum(abs(val) for val in acount.values()))

def makeAnagram(a, b):
    # Write your code here

    count =0
    sorteda= sorted(a)
    sortedb=sorted(b)
    print("length of astring is ",len(a))
    print("length of bstring is ", len(b))
    for eachachar in sorteda:
        for eachbchar in sortedb:
            if eachbchar==eachachar:
                count+=1
                eachbchar == '/'
                break
            else:
                continue
    print("count is ",count)

    return len(a)+len(b) - 2*count

if __name__ == '__main__':


    a1 = "fcrxzwscanmligyxyvym"

    b1 = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
    a= "accdr"
    b = "bddcrgha"

    #res = makeAnagram(a, b)
    res = makeAnagramwithcouter(a1,b1)
    print(res)
