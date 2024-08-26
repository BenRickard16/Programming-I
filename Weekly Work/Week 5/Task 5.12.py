def zero_matrix(m, n):
    mat = [
        [ 0.0 for j in range (n) ]
        for i in range(m)
    ]
    return mat

print(zero_matrix(2,3))
