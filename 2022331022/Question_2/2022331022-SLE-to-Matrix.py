#Input: A system of linear equation in Matrix form
print("\nEnter the system of linear equations by matrix form.\n" \
"Example: 1 2 3\n" \
"         4 5 6\n" \
"         7 8 9\n" \
"then enter the constants in one line accordingly.(separated by spaces)")
n = int(input("\nEnter dimension of the matrix: "))
mat= []
i = 0
print("input: \n")

while True:
    row = list(map(float,input().split()))
    if len(row)==n:
        mat.append(row)
        i+=1
        if i == n:
            break
        continue
    else:
        print(f"Enter {n} elements please.")
        continue
    
while True:
    constants = list(map(float,input("Enter constants:\n").split()))
    if len(constants)==n:
        break
    else:
        print(f"Enter {n} elements please.")
i = 0
for r in mat:
    for el in r:
        print(el,end=" ")
    print(f"  {constants[i]}")
    i+=1