list2 = ['a', 'abc', 'xyz', 's', 'aba', '1221']

result = [x for x in list2 if len(x) > 2 and x[0] == x[-1]]

print(len(result))