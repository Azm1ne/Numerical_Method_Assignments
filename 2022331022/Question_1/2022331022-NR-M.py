#Newton Raphson Method
import my_functions

cofs = my_functions.Take_Polynomial_as_Input()
func = lambda val: my_functions.Evaluation_of_function_with_coefficients(cofs, val)
difcofs = my_functions.differentiation_of_polynomial(cofs)
funcprime = lambda val: my_functions.Evaluation_of_function_with_coefficients(difcofs, val)

xi = float(input("\nMake a guess for xi:\n"))

tolerance = float(input("\nEnter absolute relative approximate error:\n"))

table = [["\nTable sequence: Iteration, xi, func(xi), error"]]
i = 0

while True:
    if funcprime(xi) == 0:
        print("Derivative became zero. Method failed.")
        break

    xii = xi - (func(xi) / funcprime(xi))
    error = my_functions.evaluate_error(xii, xi)

    table.append([i, xii, func(xii), error])

    if error < tolerance:
        print(f"The root is {xii:.4f} and error is {error:.6f}")
        break

    xi = xii
    i += 1

for row in table:
    for val in row:
        if isinstance(val, float):
            print(f"{val:.4f}", end="\t\t")
        else:
            print(val, end="\t\t")
    print()
