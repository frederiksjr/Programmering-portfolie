def sort(number):
    i = len(number) -1
    antalsammenligninger = 0
    
    while i >= 1:
        for j in range(0, i):
            x = number[j]
            y = number[j + 1]
            antalsammenligninger += 1
            if x > y:
                number[j] = y
                number[j + 1] = x
        i -= 1
    print("færdig. der blev fortaget", antalsammenligninger, "sammenligninger")
    return number

print(sort([4,3,5,2,1]))
