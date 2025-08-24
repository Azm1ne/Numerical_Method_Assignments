#Euler Method
import my_functions

equ = input("\nEnter the differential equation:\n")
f = my_functions.equation_to_function(equ)
print("Please enter numbers only,\n")
x0 = float(input("Enter initial x0: "))
y0 = float(input("Enter initial y0: "))
xf = float(input("Enter final x: "))
h_values = list(map(float, input("Enter step sizes separated by spaces: ").split()))

def euler(h):
    x, y = x0, y0
    n = int(xf / h)
    for _ in range(n):
        y = y + h * f(x, y)
        x += h
    return y

for h in h_values:
    e = euler(h)
    print(f"The answer in Euler Method is {e}")



