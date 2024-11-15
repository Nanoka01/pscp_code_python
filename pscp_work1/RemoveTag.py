from sympy import symbols, integrate, sqrt, Rational

# Define the variable and the function
x = symbols('x')
function = 14*x**6 - (8 / (7 * x**Rational(3,3))) + 2

# Compute the definite integral from -1 to 1
integral_result = integrate(function, (x, -1, 1))
print(integral_result)