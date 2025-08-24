#False position method
import my_functions
cofs = my_functions.Take_Polynomial_as_Input()
func = lambda val: my_functions.Evaluation_of_function_with_coefficients(cofs,val)
xl, xu = None, None
while True:
    guesses = list(map(float,input("\nMake two guesses.(Pick xl and xu such that xl < xu, write them with separated spaces.)\n").split()))
    xl , xu = guesses[0] , guesses[1]
    if len(guesses)!=2:
        print("give two guesses please, try again\n")
        continue
    if func(xl)*func(xu)>0:
        print("\nRequirement was not fullfilled, Make a better guess!\n")
        continue
    elif func(xl)*func(xu)==0:
        if func(xl)==0:
            print(f"\nYou guessed the root!, It's {xl}\n")
        elif func(xu)==0:
            print(f"\nYou guessed the root!, It's {xu}\n")
        exit()
    break

error = float(input("\nEnter absolute relative approximate error:\n"))
table = [["\nTable sequence: Iteration ,xl ,xu ,xm , Er, f(xm)"]]
prev_xm = 0
i = 1
while error < my_functions.evaluate_error((xu*func(xl)-xl*func(xu))/(func(xl)-func(xu)), prev_xm):
    new_xm = (xu*func(xl)-xl*func(xu))/(func(xl)-func(xu))
    lst = [i, xl, xu, new_xm, my_functions.evaluate_error((xu*func(xl)-xl*func(xu))/(func(xl)-func(xu)),prev_xm), func(new_xm)]
    if func(xl)*func(new_xm) < 0:
        xu = new_xm
    elif func(xl)*func(new_xm) > 0:
        xl = new_xm
    else:
        print(f"The root is {new_xm}\n")
        prev_xm = new_xm
        i = i + 1
        table.append(lst)
        break
    prev_xm = new_xm
    i = i + 1
    table.append(lst)

for row in table:
    for i in row:
        if isinstance(i,float):
            print(f"{i:.4f}",end="\t\t")
        elif isinstance(i,int):
            print(i,end="\t\t")
        else:
            print(i,end="")
    print()