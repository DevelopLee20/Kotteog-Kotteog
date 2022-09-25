#정수 제곱근 판별
"""
임의의 양의 정수 n에대해, n이 어떤 양의 정수 x의 제곱이라면
x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요
"""

def solution(n):
    i=n**(1/2)
    return int((i+1)**2) if (i-int(i))==0 else -1

print(solution(int(input())))