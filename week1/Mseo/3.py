#자릿수 더하기
"""
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return하는 
solution함수를 만들어 주세요.
예를 들어 N=123이면 1+2+3=6을 return 하면 됨
"""
from re import I


def solution(n):
    answer=0 #각 자리수를 더한 값을 저장할 변수
    i=10
    for _ in range(len(str(n))):
        answer+=n%i
        n=n//i

    return answer

print(solution(int(input())))

"""
다른 사람 풀이

- 문자열로 변경하여 푼
sum([int(i) for i in str(n)])

- 재귀함수를 이용

def sum_digit(n):
    if n<10: #n이 10보다 작으면 더 이상 계산할 필요 x
        return n
    retun (n%10)+sum_digit(n//10)
"""