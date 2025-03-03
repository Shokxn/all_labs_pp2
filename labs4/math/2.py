def trapezoid_area(h, a, b):
    S = (a + b) * h / 2
    return S

h = int(input())
a = int(input())
b = int(input())

print(trapezoid_area(h, a, b))