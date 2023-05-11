for num in range(0,22,2):
    print(num)


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))


def even_numbers(start,end):
    if start and end == 0:
        print("1,3,5,7,9")

    else:
        start = start+1 if start&1 else start
        [ print( x ) for x in range(start, end + 1, 2)]

print(even_numbers)





