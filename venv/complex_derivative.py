from sympy import sympify, SympifyError, diff

expr1 = input("Input expression")

try:
    expr1 = sympify(expr1)
    print(diff(expr1))

except SympifyError:
    print("Invalid input")