

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    strlen= n // len(s)
    reminder = n%len(s)
    a_count = strlen* s.count("a")
    remaining_str =  s[:reminder]
    a_count = a_count + remaining_str.count("a")
    print("a")

if __name__ == '__main__':

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

