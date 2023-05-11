import random
random_list = []
for i in range(0,7):
    n = random.randint(1,40)
    random_list.append(n)
random_list.sort()
print(random_list)