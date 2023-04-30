# 시간 초과
N, K = map(int, input().split(" "))
lst = [i for i in range(1, N+1)]
output = "<"

while len(lst):
    for _ in range(K-1):
        lst = lst[1:] + [lst[0]]

    output = output + str(lst[0]) + ", "
    lst = lst[1:]

print(output[:-2]+">")