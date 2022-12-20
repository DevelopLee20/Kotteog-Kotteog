"""
문자열 내림차순으로 배치하기

문자열 s에 나타나는 문자를 큰 것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요
s는 영문 대소문자로 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다
"""
def solution(s):
    s=list(s)
    s.sort(reverse=True)
    return ''.join(i for i in s)

"""
다른 사람의 풀이
return ''.join(sorted(s, reverse=True))

sort와 sorted의 차이
sort는 정렬된 리스트를 반환하지않음 반환값을 출력하면 none이 출력됨
sort는 문자열을 정렬하지 않음
"""