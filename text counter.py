from collections import Counter

text = str(input("insert your text here "))
split = text.split()
print(text.count(","))
Counter = Counter(split)
most_occur = Counter.most_common(4)
print(most_occur)