def identity_matrix(n):
    mat = [[ 0.0 for j in range (n) ]for i in range(n)]
    for i in range (n):
        mat[i][i] = 1
    return mat

print(identity_matrix(4))