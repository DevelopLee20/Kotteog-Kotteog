#짝수와 홀수
'''
정수 num이 짝수일 경우 "Even"을 반환하고 
홀수인 경우 "Odd"를 반환하는 함수를 완성해라
'''
def solution(num):
    return "Even" if num%2==0 else "Odd"

print(solution(int(input())))

#다른 사람 풀이 num%2==0이 아니라 num%2로 작성함
#0이거나 0이 아닐때를 구분하면 됨