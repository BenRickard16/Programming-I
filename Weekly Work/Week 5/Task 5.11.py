def det2(mat):
    val = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    return val

def inv2(mat):
    ans = [[0,0],[0,0]]
    x = det2(mat)
    y = 1/x
    ans[0][0] = y*mat[1][1]
    ans[1][1] = y*mat[0][0]
    ans[1][0] = -y*mat[1][0]
    ans[0][1] = -y*mat[0][1]
    return ans

print(inv2([[2,3],[5,1]]))