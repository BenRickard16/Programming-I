def isodd2(n):
    val = n%2
    return(val == 1)

i = 1
while i<101:
    if isodd2(i):
        print(i)
    i = i+1