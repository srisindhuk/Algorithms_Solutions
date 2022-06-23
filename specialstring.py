''' Given a string, determine how many special substrings can be formed from it.
A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
'''

def ispalindrome(output):
    start = 0
    end = len(output)-1
    print(output)
    while(start<len(output) and end>=0):
        if output[start]!= output[end]:
            return False
        else:
            start +=1
            end -=1
    return True

def substrCount(n,s):
    output=[]
    def _generate_subsets(so_far,idx,count):

        if idx== len(s):
            output.append("".join(so_far))
            print(output)
            if ispalindrome("".join(so_far)):
                count +=1
            return count

        count= count + _generate_subsets(so_far+[s[idx]],idx+1,count)
        count = count +_generate_subsets(so_far,idx+1,count)

    return _generate_subsets([],0,0)


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)