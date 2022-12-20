"""
길이가 같은 두 1치원 정수 배열 a,b가 매개변수로 주어집니다.
a와 b가 내적을 return 하도록 solution 함수를 완성해주세요
"""
def solution(a,b):
    return sum([a[i]*b[i] for i in range(len(a))])

"""
TypeError: 'int' object is not callable
- 예약어(sum, max등의 함수)를 변수명으로 사용했기 때문

다른 사람의 풀이
sum([x*y for x, y in zip(a,b)])

zip이라는 함수를 사용함
"""