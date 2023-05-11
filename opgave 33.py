list1 = []
hej1 = input()
hej2 = input()
hej3 = input()
hej1 = int(hej1)
hej2 = int(hej2)
hej3 = int(hej3)
list1.append(hej1)
list1.append(hej2)
list1.append(hej3)
Sum = sum(list1)
i = 3
print("largerst element in list is:", max(list1))
if i in list1:
    print("exits")
else:
    print("dont exits")
print(Sum)
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")

list1.reverse()
print(list1)
uniquelsit = set(list1)
print(uniquelsit)
mynewlist = list(uniquelsit)