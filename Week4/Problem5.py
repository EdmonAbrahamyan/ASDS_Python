menu = ['ice cream', 'chocolate', 'apple crisp', 'cookies']
desert = input("Enter your desert please\n")

while desert not in menu:
    desert = input("Please choose another desert\n")
else:
    print("Your desert will arrive in 10 minutes")