market = {
          "dairy": ["yogurt", "cheese"],
          "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]
         }
print(market)
market["candies"] = ["mars", "kinder", "twix"]

market["fruits"] = list(set(market["fruits"]))
market["fruits"].sort()

print(market)