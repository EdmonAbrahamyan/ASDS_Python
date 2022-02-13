text = input("enter the text")
print("The given text: ", text)

if "usa" or "USA" in text:
    count_usa = text.count("USA") + text.count("usa")
    print("The USA/usa count is:", count_usa)
    text1 = text.replace("USA", "Armenia", text.count("USA"))
    print("Output string: ", text1.replace("usa", "Armenia", text1.count("usa")))