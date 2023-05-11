weight = int(input("enter the weight in KG: \n"))
height = int(input("enter the height in cm: \n"))
age = int(input("enter the age in years: \n"))
isMale = str(input("are you male? (y/n"))

if isMale == "y":
    isMale = True
elif IsMale == "n":
    isMale = False
else:
    print("error")
    quit()
    
if isMale:
    bmr = 66.5 + (13.75 * weight) + (5 * height) - (6.755 * age)
    
else:
    bmr = 655.1 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    
bmr = round(bmr)
print(bmr)
