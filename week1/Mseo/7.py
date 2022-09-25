"""
정수를 담고 있는 배열 arr의 평균값을 return 하는 함수, solution을 완성해보세요
제한사상
arr은 1이상, 100이하인 배열
arr의 원소는 -10000 이상 10000이하인 정수입니다
"""
def solution(arr):
    return sum(arr)/len(arr)

print(solution([1,2,3,4]))