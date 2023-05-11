num = int(input("which table would you like to use"))

starting_range = int(input("write the start number"))
ending_range = int(input("write the end number"))
print()
print("so this is the table for",num)
for i in range(starting_range, ending_range + 1):
    print(num,"x",i,"=",num*i)

#the multiplacation table be like


#input from user
num = int(input("Display table of?"))

# do it 10 times
for i in range(1,11):
    print(num,"x",i,"=",num*i)