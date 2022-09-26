def solution(n):
    sorter = [int(i) for i in str(n)]
    sorter.sort()
    answer = 0
    
    for i in range(len(sorter)):
        answer = answer + (10**i) * sorter[i]
    
    return answer