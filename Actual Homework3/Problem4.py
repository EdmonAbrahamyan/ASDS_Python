list3 = [4, 1, 2, 6, 8, 1, 10, 9]
print("Before list3:", list3)

list4 = list3.copy()
del list4[0]
del list4[4]
del list4[5]

print("After list3:", list3)
print("list4", list4)
