#Secant0 Method
import my_functions

cofs = my_functions.Take_Polynomial_as_Input()
func = lambda val: my_functions.Evaluation_of_function_with_coefficients(cofs, val)
difcofs = my_functions.differentiation_of_polynomial(cofs)

while True:
    guesses = list(map(float,input("\nMake two guesses.(Pick x0 and x1, write them with separated spaces.)\n").split()))
    if len(guesses)!=2:
        print("give two guesses please, try again\n")
        continue
    else:
        break

tolerance = float(input("\nEnter absolute relative approximate error:\n"))
xii , xi = guesses[1], guesses[0]
table = [["\nTable sequence: Iteration ,xi ,error"]]
i = 0

while True:
    if func(xii)-func(xi) == 0:
        print("Divition by zero. Method failed.")
        break

    xiii = xii - ((func(xii)*(xii-xi))/(func(xii)-func(xi)))
    error = my_functions.evaluate_error(xiii, xii)

    table.append([i, xiii, error])

    if error < tolerance:
        print(f"The root is {xiii:.4f} and error is {error:.6f}")
        break

    xi = xii
    xii = xiii
    i += 1

for row in table:
    for val in row:
        if isinstance(val, float):
            print(f"{val:.4f}", end="\t\t")
        else:
            print(val, end="\t\t")
    print()
