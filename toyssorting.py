


def maximumToys(prices,sum):
    tempsum =0
    count =0
    prices.sort()
    print(prices)
    for j in prices:
        if tempsum + j < sum:
            tempsum = tempsum + j
            count +=1
    return count




if __name__ == '__main__':
    n= 7
    k =50
    prices =[111,12, 5, 111, 200, 1000, 10]
    result = maximumToys(prices, k)
    print(result)
