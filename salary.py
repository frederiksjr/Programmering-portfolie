from collections import Counter

def most_frequent(salary):
    occurrences_count = Counter(salary.values())
    return occurrences_count.most_common(1)[0][0]

def average(salary):
    return sum(salary.values()) / len(salary.values())


salary = {'Niels':85000,'Peter':40000,'Jakob':90000,'Poul':100000,'Dorte':40000}
print(salary["Niels"])
print(salary["Peter"])
print(salary["Jakob"])
print(salary["Poul"])
print(salary["Dorte"])
bente = 0
if bente in salary:
    print("bente is in list")
else:
    print("bente is not in list")

average = average(salary)

maximum = max(salary.values())

minimum = min(salary.values())

print(salary.keys())
print(salary.values())
print("the average salary is =", round(average, 2))
print(most_frequent(salary))
print(maximum)
print(minimum)
