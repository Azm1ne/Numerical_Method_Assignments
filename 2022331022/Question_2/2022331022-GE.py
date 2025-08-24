#Gaussian Elimination(Copied)

def Naive_Gaussian_Elimination(mat, consts):
    n = len(consts)
    
    # Forward Elimination
    for i in range(n-1):
        if mat[i][i] == 0:
            raise ValueError("Division by zero! Use partial pivoting to handle this.")
        for j in range(i+1, n):
            mul = mat[j][i] / mat[i][i]   # FIXED
            for k in range(i, n):
                mat[j][k] -= mul * mat[i][k]   # FIXED
            consts[j] -= mul * consts[i]       # FIXED

    # Back Substitution
    ans = [0] * n
    for i in range(n-1, -1, -1):
        summ = consts[i]
        for k in range(i+1, n):
            summ -= mat[i][k] * ans[k]   # FIXED
        ans[i] = summ / mat[i][i]        # FIXED
    
    return ans


def Gaussian_Elimination_with_Partial_Pivoting(mat, consts):
    n = len(consts)
    
    # Forward Elimination
    for i in range(n-1):
        # Partial Pivoting
        max_row = i
        for j in range(i + 1, n):
            if abs(mat[j][i]) > abs(mat[max_row][i]):
                max_row = j

        # Swap rows in matrix and constants
        if max_row != i:
            mat[i], mat[max_row] = mat[max_row], mat[i]
            consts[i], consts[max_row] = consts[max_row], consts[i]
            print(f"Row {i} swapped with Row {max_row} for pivoting")

        if mat[i][i] == 0:
            raise ValueError("Matrix is singular!")

        for j in range(i+1, n):
            mul = mat[j][i] / mat[i][i]
            for k in range(i, n):
                mat[j][k] -= mul * mat[i][k]
            consts[j] -= mul * consts[i]

    # Back Substitution
    ans = [0] * n
    for i in range(n-1, -1, -1):
        summ = consts[i]
        for k in range(i+1, n):
            summ -= mat[i][k] * ans[k]
        ans[i] = summ / mat[i][i]
    
    return ans


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

solution = Gaussian_Elimination_with_Partial_Pivoting(mat, constants)
print("Solution:")
for _ in range(n):
    print(f"x{_+1}: {solution[_]:.4f}")