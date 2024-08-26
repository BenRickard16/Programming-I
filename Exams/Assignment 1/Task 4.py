def cmult(w,z):
    x = w[0] * z[0] - w[1] * z[1]
    y = w[0] * z[1] + w[1] * z[0]
    return [x,y]

print(cmult([-5,0],[1,12]))