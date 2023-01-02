"""
정수 내림차순으로 배치하기
 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운
 정수를 리턴해주세요. 예를 들어 n이 118372면 823211을 리턴
"""
def solution(n):
    return int(''.join(map(str,sorted([int(i) for i in str(n)], reverse=True))))
print(solution(int(input())))