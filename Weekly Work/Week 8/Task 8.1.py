from math import pi #, sin
from matplotlib import pyplot as plt
from numpy import linspace, arange, sin

# A vector-like object
x = linspace(2, 5, 31)
print(x)
print(2*x+1)
# These is not defined for vectors as mathematical objects
# in linear algebra but are allowed by numpy (and R)
print(x**2)   # Squares each element
print(sin(x)) # Computes the sin of each element

# Another vector
m = arange(8)
print(m)
# Turn the vector into a 2x4 matrix
m.shape = (2, 4)
print(m)
# These are not matrix multiplication, just multiplication
# and powers of elements of the matrix
print(m*m)
print(m**2)
# Sum the columns and rows of m: the argument says which
# dimension to sum over
print(m.sum(0))
print(m.sum(1))


def plot_function(f, startx, endx, nx):
   x = linspace(startx, endx, nx)
   y = f(x)
   plt.plot(x, y, '-+')
   plt.show()


# A test using sin(x)   
plot_function(sin, 0, 4*pi, 20)

def f(x):
   return(1/(1-x))

# Another test using 1/(1-x)
plot_function(f, -2, 2, 101)
