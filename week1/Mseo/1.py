#나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    #가장 큰 값부터 2까지 계산을 해주면 마지막에는 가장 작은 값이 변수에 저장된다
    for i in range(n,1, -1):
        if n%i==1:
            answer=i
    return answer

print(solution(int(input())))

'''
다른 사람 풀이
return [x for x in range(1n+1) if n%x==1][0]
'''