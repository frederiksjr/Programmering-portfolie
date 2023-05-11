from sympy import symbols, solve
a = int(input("input a value "))
b = int(input("input b value "))
c = int(input("input c value "))
x = symbols("x")

eq = (a*x+b=c)

sol = solve(eq)

print(sol)
