
import math
import os
import random
import re
import sys


def minimumabsolute(input):
    min =abs(input[0] - input[1])
    input.sort()
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            if abs(input[i]-input[j]) < min:
                min = abs(input[i]-input[j])
    return min

input = [3, -7, 0]
min = minimumabsolute(input)
print(min)