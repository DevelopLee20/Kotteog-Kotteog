import sys

def push(command):
    global length
    lst.append(command)
    length += 1

def pop():
    global length
    if length == 0:
        return -1
    else:
        seed = lst[length-1]
        lst.pop()
        length -= 1
        return seed

def size():
    global length
    return length

def empty():
    global length
    return int(length == 0)

def top():
    global length
    if length == 0:
        return -1
    else:
        return lst[length-1]

lst = []
length = 0

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        push(command[1])
    
    elif command[0] == 'pop':
        print(pop())
    
    elif command[0] == 'size':
        print(size())
    
    elif command[0] == 'empty':
        print(empty())

    elif command[0] == 'top':
        print(top())