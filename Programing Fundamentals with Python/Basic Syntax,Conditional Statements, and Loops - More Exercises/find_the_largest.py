num = int(input())


def printMaximum(inum):
    count = [0 for x in range(num)]
    # Converting given number to string
    string = str(num)
    # Updating the count array
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] + 1
    # Result stores final number
    result = 0
    multiplier = 1
    # traversing the count array
    # to calculate the maximum number
    for i in range(num):
        while count[i] > 0:
            result = result + (i * multiplier)
            count[i] = count[i] - 1
            multiplier = multiplier * 10
    # return the result
    return result


print(printMaximum(num))