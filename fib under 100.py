def nextfib():
    prevPrev=0
    yield 0
    prev=1
    yield 1
    while True:
        nextF=prev+prevPrev
        prevPrev, prev = prev, nextF
        yield nextF
 
fib=0
gen=nextfib()
while fib<=1000:
    fib=next(gen)
    print (fib)