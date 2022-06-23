import math
import os
import random
import re
import sys


def minimumBribes(q):
    count = 0
    n = len(q)
    for i in range(n):
        if(q[i]-(i+1)>2):
            print("Too Chotic")
            return
    for i in range(len(q)):
        for j in range(len(q)-1,i,-1):
            if q[j]>q[j-1]:
                count+=1
    return count




#q = [5, 1, 2, 3, 7, 8, 6, 4]

q=[2, 1, 5, 3, 4]
print(minimumBribes(q))
print(q)