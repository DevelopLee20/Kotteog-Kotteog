"""
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어보세요
단어의 길이가 짝수라면 가운데 두 글자를 반환하면 됩니다
"""
def solution(s):
    return (s[int(len(s)/2-1)]+s[int(len(s)/2)]) if len(s)%2==0 else s[int(len(s)/2)]


"""
다른 사람들의 풀이
return str[(len(str)-1)//2:len(str)//2+1]
"""