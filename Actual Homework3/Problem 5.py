a = [1, 4, 5, 7, 8, -2, 0, -1]

print(f"The 3-th and 5-th elements in list a are: {a[2]} and {a[4]}")

a_sorted = sorted(a)
print(a_sorted)

print(a_sorted[1:3], '\n', a_sorted[2:6])

a_sorted.pop(2)
a_sorted.pop(3)
print(a_sorted)

b = ["grapes", "Potatoes", "tomatoes", "Orange", "Lemon", "Broccoli", "Carrot", "Sausages"]
b_sorted = sorted(b)
print(b_sorted)


c = a[1:3] + b[4:6]
print("c:", c)
