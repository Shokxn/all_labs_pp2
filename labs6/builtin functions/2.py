def case(s):
    upper = sum(1 for i in s if i.isupper())
    lower = sum(1 for i in s if i.islower())

    return upper, lower

s = "INJinjkOINmklMKLmkkmkM"

print(case(s))