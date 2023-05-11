def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

streaming = ["netflix", "hulu", "disney+", "youtube", "appletv+", "HBO Max", "amazon prime", "paramount+", "pornhub premium", "crunchyroll", "apple one", "spotify", "bestality.com"]
platform = "pornhub premium"

if search(streaming, platform):
    print("platform is found")
else:
    print("platform is not found")
    
    
arr = [10,20,80,30,60,50,110,100,130,170] 

x = 10

def search2(arr, x):
     
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1
print(search2(arr,x))


numbers = [1,2,3,4,5,6,7,8]
N = 8

if N in numbers: 
    print (numbers.index(N))
if N not in numbers: 
    print(-1)
        