t1 = (2, "cat", "a", -2, "Anna")
temp = list(t1)
temp.remove("a")
t1 = tuple(temp)
print(t1)

t2 = (1, 2, 3, 4, 5)
t3 = t1[:2] + t2[:3]
print(t3[2])