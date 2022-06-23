#o(n)complexity
'''def kangaroo(x1, v1, x2, v2):
    # Write your code here
    result="NO"
    while 1:
        if  x1==x2:
            result="YES"
            break
        else:
            x1=x1+v1
            x2=x2+v2
    return result
'''
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    result="NO"
    if x2>x1 and v2>v1:
        return "NO"
    if (x1-x2)%(v2-v1) ==0 or (x2-x1)%(v1-v2)==0:
        result="YES"
    return result

x1=43
x2=70
v1=2
v2=2
result = kangaroo(x1, v1, x2, v2)
print(result)
