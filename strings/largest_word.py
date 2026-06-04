text = "I am learning Python programming"

words = text.split()

largest = max(words, key=len)

print(largest)
