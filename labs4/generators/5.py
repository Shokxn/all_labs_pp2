def generator(n):
    for i in range(n, 0-1, -1):
        yield i

x = int(input())
print(','.join(map(str, generator(x))))