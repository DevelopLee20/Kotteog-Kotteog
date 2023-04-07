#x만큼 간격이 있는 n개의 숫자
"""
함수 solution은 정수 x와 자연수 n을 입력받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
"""
def solution(x,n):
    #n개이고 x씩 증가이니 한번 증가할 때마다 x+x x+x+x=(x+2x) x+x+x+x(x+3x) 이렇게 증가되는 것을 이용함
    return [x+x*i for i in range(n)]
print(solution(-4,2))