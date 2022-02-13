lista = ['a', 0, 2]

for i in lista:
    try:
        print(1 / i)
    except Exception as e:
        print('The entry is:', '\033[1m' + 'the current entry of the list' + '\033[0m')
        print('Oops!', '\033[1m' + ' The exception that occured' + '\033[0m')
