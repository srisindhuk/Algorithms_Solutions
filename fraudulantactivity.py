
def median(numbers):
    n = len(numbers)
    numbers.sort()

    if n % 2 == 0:
        median = (numbers[n // 2] + numbers[n // 2 - 1]) / 2
    else:
        median = numbers[n // 2]
    return median

def activityNotifications(expenditure,d):
    result =0
    n = len(expenditure)
    for i in range(0,n-d):
        if expenditure[d+i] >= (median(expenditure[i:d+i]))*2:
            result +=1
    return result

if __name__ =='__main__':
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    result = activityNotifications(expenditure, d)
    print(result)
