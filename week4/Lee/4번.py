for _ in range(int(input())):
    list_name = list(map(str, input().split(' ')))
    
    for i in list_name:
        print(i[::-1], end=" ")