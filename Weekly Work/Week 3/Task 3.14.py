def nroots(a,b,c):
    n = (b**2-4*a*c)
    if n > 0:
        return 2
    if n == 0:
        return 1
    else:
        return 0


def roots(a,b,c):
    if nroots(a,b,c) == 2:
        val1 = (-b+(b**2-4*a*c)**(1/2))/2*a
        val2 = (-b-(b**2-4*a*c)**(1/2))/2*a
        return [val1, val2]
    if nroots(a,b,c) == 1:
        val1 = val1 = (-b+(b**2-4*a*c)**(1/2))/2*a
        return [val1]
    if nroots(a,b,c) == 0:
        return []

print(roots(1,-4,4))