def decadd(d1, d2):
    ans = []
    while len(d1) != len(d2):
        if len(d1) > len(d2):
            d2.append(0)
        else:
            d1.append(0)
    for i in range(len(d1)):
        n = d1[i] + d2[i]
        ans.append(n)
    for i in range(len(ans)-1):
        if ans[i] > 9:
            ans[i+1] = ans[i+1] + 1
            ans[i] = ans[i] - 10
    if ans[len(ans)-1] >9:
        ans.append(1)
        ans[len(ans)-1] = 0
    return ans

print(decadd([4,4,5,1,5],[6,5,4,8,4]))

