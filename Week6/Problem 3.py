def my_range(n):
    for i in range(n+1):
        yield i
    print("no values left")

print(list(my_range(4)))