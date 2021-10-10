list1 = [4, 1, 2, 6, 8, 1]
print("Before", list1)
val = int(input())
if val in list1:
    list1.remove(val)

print("After", list1)