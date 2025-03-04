import functools

def multiply(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

print(multiply([2, 3, 4]))