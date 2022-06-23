#!/bin/python3

import math
import os
import random
import re
import sys
import numpy

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):

    # Write your code here



    """     
    while oneptr <len(c) and twoptr < len(c):
        if c[i] == 0:
            if c[oneptr] ==0 :
                count +=1
                oneptr +=1
            elif c[twoptr] == 0:
                count+=1
                twoptr +=2
        else:
            i+=1
    """
    return count




if __name__ == '__main__':
   c = [0,1,0,0,1,1,0,1,1,1]
   result = jumpingOnClouds(c)
   print(result)


