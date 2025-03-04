def all_true(tuple):
    return all(tuple)

t1 = {1, True, "Hello"}
print(all_true(t1))

t2 = {0, True, True}
print(all_true(t2))