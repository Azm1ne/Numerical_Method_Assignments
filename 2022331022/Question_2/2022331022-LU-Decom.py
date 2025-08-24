#LU decomposition(Copied)

def LU_Decomposition(A):
    n = len(A)
    
    L = [[0]*n for _ in range(n)]
    U = [row[:] for row in A]
    
    for i in range(n):
        L[i][i] = 1  
        
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]   
            L[j][i] = factor            
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]
    
    return L, U


# Forward Substitution
def forward_substitution(L, b):
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        sum_ = 0.0
        for j in range(i): 
            sum_ += L[i][j] * y[j]
        y[i] = b[i] - sum_
    return y


# Backward Substitution
def backward_substitution(U, y):
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_ = 0.0
        for j in range(i + 1, n):
            sum_ += U[i][j] * x[j]
        x[i] = (y[i] - sum_) / U[i][i]
    return x


# Inverse Matrix
def inverse_matrix(L, U):
    n = len(L)
    inv_A = [[0.0] * n for _ in range(n)]
    for i in range(n):
        e = [0.0] * n
        e[i] = 1.0
        y = forward_substitution(L, e)
        x = backward_substitution(U, y)
        for r in range(n):
            inv_A[r][i] = x[r]
    return inv_A


# Determinant
def determinant_from_U(U):
    det = 1.0
    for i in range(len(U)):
        det *= U[i][i]
    return det


# Main Program
print("\nEnter the system of linear equations by matrix form.\n" \
"Example: 1 2 3\n" \
"         4 5 6\n" \
"         7 8 9\n" \
"then enter the constants in one line accordingly.(separated by spaces)")
n = int(input("\nEnter dimension of the matrix: "))
mat = []
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

L, U = LU_Decomposition(mat)

print("\nLower Triangular Matrix (L)")
for _ in range(n):
    print(f"x{_+1}: {L[_]:.4f}")

print("\nUpper Triangular Matrix (U)")
for _ in range(n):
    print(f"x{_+1}: {U[_]:.4f}")

print("\nInverse of A")
inv_A = inverse_matrix(L, U)
for _ in range(n):
    print(f"x{_+1}: {inv_A[_]:.4f}")

det_A = determinant_from_U(U)
print(f"\nDeterminant of A = {det_A:.4f}")