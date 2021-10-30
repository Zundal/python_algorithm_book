def stackSum(num):
    # 1부터 num까지의 합
    stackNum = 0
    for x in range(num):
        stackNum += x+1
    return stackNum

print(stackSum(5))