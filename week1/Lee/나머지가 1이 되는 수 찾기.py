def solution(n):
    lst = [n%i for i in range(1,n)]
    answer = lst.index(1)+1
    return answer