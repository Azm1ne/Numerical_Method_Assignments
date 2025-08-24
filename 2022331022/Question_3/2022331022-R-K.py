#Runge-Kutta 2nd order

import my_functions

equ = input("\nEnter the differential equation:\n")
f = my_functions.equation_to_function(equ)

print("Please enter numbers only,\n")
x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y0: "))
xf = float(input("Enter final x: "))

h_values = list(map(float, input("Enter step sizes separated by spaces: ").split()))

# Euler's method
def euler(h):
    x, y = x0, y0
    n = int(xf / h)
    for _ in range(n):
        y = y + h * f(x, y)
        x += h
    return y

# Heun's method
def heun(h):
    x, y = x0, y0
    n = int(xf / h)
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h, y + h * k1)
        y = y + (h / 2) * (k1 + k2)
        x += h
    return y

# Midpoint method
def midpoint(h):
    x, y = x0, y0
    n = int(xf / h)
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + (h / 2) * k1)
        y = y + h * k2
        x += h
    return y

# Ralston's method
def ralston(h):
    x, y = x0, y0
    n = int(xf / h)
    for _ in range(n):
        k1 = f(x, y)
        k2 = f(x + (3 * h / 4), y + (3 * h / 4) * k1)
        y = y + (h / 3) * (k1 + 2 * k2)
        x += h
    return y

print("Table sequence: Euler, Heun, Midpoint, Ralston")
for h in h_values:
    e = euler(h)
    hn = heun(h)
    m = midpoint(h)
    r = ralston(h)
    print(f"{e:.4f}\t{hn:.4f}\t{m:.4f}\t{r:.4f}\t")



