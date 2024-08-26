# This function can be used to square a number
def good(x):
    y = x**2
    return y

# This function prints out the square of a number
# but fails to return a value which can be used in
# subsequent calculations.
def bad(x):
    y = x**2
    print(y)

# This function calculates the square of a number
# but fails to return a value which can be used in
# subsequent calculations.
def bad2(x):
    y = x**2

z = bad(5)
print('z is', z)
w = z**0.5
print(w)



