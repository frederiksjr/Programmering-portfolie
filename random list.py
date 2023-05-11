import random
random_list = []
for i in range(0,5):
    n = random.randint(1,30)
    random_list.append(n)
random_list.sort()
print(random_list)

random_list.sort(reverse=True) 
print(random_list)

x = int(input("user input "))
random_list.append(x)
print(random_list)