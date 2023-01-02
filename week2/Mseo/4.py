"""
문자열을 정수로 바꾸기

문자열 s를 숫자로 변환하는 함수, solution을 완성하세요

제한조건
- s의 길이는 1이상 5이하입니다
- s의 맨 앞에는 부호가(+-)가 올 수 있습니다
- s는 부호와 숫자로만 이루어져있습니다
- s는 0으로 시작하지않습니다
"""
def solution(s):
    return int(s)
print(solution(input()))

#다른 방법으로도 풀어봄
"""
def solution(s):
    temp=0
    if s[0]=="-":
        temp=-1
    else:
        temp=1
    return temp*int(s[1::])
print(solution(input()))
"""