text = input("enter the text")
first_word = input("input the first word")
second_word = input("input the second word")

print("The given text: ", text)
print("First word: ", first_word)
print("Second word", second_word)

if first_word in text:
    print("Output string: ", text.replace(first_word, second_word, text.count(first_word)))