'''
알고리즘 함수 비교
stackSum 의 함수의 경우 num의 크기가 늘어나면 늘어날 수록 시간이 오래걸린다.
stackSumG 의 함수의 경우 num의 크기가 늘어나도 3번의 연산으로 답을 도출해낸다.
결론적으로 stackSumG 함수가 입력값이 커질 경우를 고려해서 상대적으로 효율적인 함수이다.
'''
def stackSum(num):
    # 1부터 num까지의 합
    stackNum = 0
    for x in range(num):
        stackNum += x+1
    return stackNum

def stackSumG(num):
    # 가우스의 방법
    return num*(num +1)//2

print(stackSum(5))
print(stackSumG(5))