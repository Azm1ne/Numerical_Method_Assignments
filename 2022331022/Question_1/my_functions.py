import math

def differentiation_of_polynomial(pol):
    diffpol = []
    a = 1
    for i in pol[1:]:
        diffpol.append(i*a)
        a = a + 1
    return diffpol

def Take_Polynomial_as_Input():
    while True:
        try:
            degree_pol = int(input("\nWhat is the degree of the polynomial?\n"))
        except:
            print("please enter an integer.\n")
            continue
        break
    
    coefficients = []
    print("\nEnter the coefficients of the polynomial in this order.\n\n"
    "\ta_0 + a_1 x + a_2 x^2 + ... + a_n x^n \n\n"
    "Enter a_0, a_1, a_2 ... etc separated by spaces(MUST INCLUDE 0s)")
    while True:
        c = input()
        if len(c.split())<degree_pol+1:
            print("\nTo few arguments, try again.")
            continue
        elif len(c.split())>degree_pol+1:
            print("\nTo many arguments, try again.")
            continue
        break
    for i in c.split():
        coefficients.append(float(i))
    return coefficients
# aaa = diff(coffs)
# for i in aaa:
#     print(i,end=" ")
# print()
def Evaluation_of_function_with_coefficients (cof, val):
    ans = 0
    p = 0
    for i in cof:
        ans += i*(val**p)
        p = p + 1
    return ans

def equation_to_function(equation_str):
    equation_str = equation_str.replace("^", "**")
    
    def func(x, y):
        allowed_names = {"x": x, "y": y, "e": math.e}
        return eval(equation_str, {"__builtins__": None}, allowed_names)
    
    return func

def evaluate_error(neew,olld):
    return (abs(neew-olld))/neew *100

# Example usage:
# equation = "x^2 + y/3 - e"
# f = equation_to_function(equation)
# print(f(2, 9))  # Example: x=2, y=9
