project = "cake"
difficulty = 5
ingredients = ["flour", "butter", "sugar", "eggs", "cocoa powder", "baking powder"]

print("Check if the list ingredients contains “apples”")
if "apples" in ingredients:
    print("\tyes")
else:
    print("\tno")

print("Check if the list ingredients contains “butter”")
if "butter" in ingredients:
    print("\tyes")
else:
    print("\tno")

print("Check if the list ingredients contains “eggs” or “margarine”")
if "eggs" or "margarine" in ingredients:
    print("\tyes")
else:
    print("\tno")

print("Check if the list ingredients contains “eggs” and “margarine”")
if "eggs" and "margarine" in ingredients:
    print("\tyes")
else:
    print("\tno")

flour, butter, sugar, eggs, cocoa_powder, baking_powder = 175, 175, "100g", 2, "1st", 0.5

print("Type of flour:", type(flour))
print("Type of butter:", type(butter))
print("Type of sugar:", type(sugar))
print("Type of eggs:", type(eggs))
print("Type of cocoa_powder:", type(cocoa_powder))
print("Type of baking_powder:", type(baking_powder))


print("flour:", flour)
print("butter:", butter)
print("sugar:", sugar)
print("eggs:", eggs)
print("cocoa_powder:", cocoa_powder)
print("baking_powder:", baking_powder)