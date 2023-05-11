from sympy import *

x = symbols('x')


def process_equation(equation):
    try:
        equation = equation.replace(" ", "")  # remove spaces
        # replace caret with double asterisks
        equation = equation.replace("^", "**")
        # replace equals sign with double equals sign
        equation = equation.replace("=", "==")
        # replace f(x) with x for simplicity
        equation = equation.replace("f(x)", "x")
        # replace sin with sin from the math library
        equation = equation.replace("sin", "math.sin")
        # replace cos with cos from the math library
        equation = equation.replace("cos", "math.cos")
        # replace tan with tan from the math library
        equation = equation.replace("tan", "math.tan")
        result = eval(equation)
        return result
    except:
        return "Invalid equation format"


def differentiate(equation):
    result = process_equation(equation)
    if isinstance(result, (int, float)):
        return "Cannot differentiate a constant"
    else:
        return diff(result, x)


def integrate(equation):
    result = process_equation(equation)
    if isinstance(result, (int, float)):
        return "Cannot integrate a constant"
    else:
        return integrate(result, x)


equation = "math.cos(90)"
# differentiated = differentiate(equation)
# integrated = integrate(equation)
result = process_equation(equation)

print(f"Result: {result}")
# print(f"Differentiated equation: {differentiated}")
# print(f"Integrated equation: {integrated}")
