import math

def area_of_polygon(s, l):
    area = (s * l**2) / (4 * math.tan(math.pi / s))
    return area

s = int(input())
l = int(input())
S = area_of_polygon(s, l)
print(S)