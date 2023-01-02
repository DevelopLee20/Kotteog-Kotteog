"""
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
예를 들어 18의 자릿수의 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수를 완성하시오
"""
def solution(x):
    num=0 # 자릿수의 합을 저장할 변수
    for i in str(x): #정수를 문자열로 만들고 for문으로 돌려서
        num+=int(i)#전부 더헤줌
    return True if x%num==0 else False #더한 값으로 x를 나눠주고 나머지가 0이면 True를 반환 아니면 False를 반환

print(solution(int(input())))