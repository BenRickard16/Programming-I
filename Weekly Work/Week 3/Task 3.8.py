# copy the double function from function-basics.py
def double(x):
    return 2*x

# Create an empty list named x
x = []

# Calculate 1+double(4) and put the result in a list with a single element
lst = [1+double(4)]

# Just as 1+double(4) was calculated before creating the list,
# the contents of variable two go in the new list various
two = 2
various = [two, 3, 'Hello', True,]

# Concatenating (joining together) lists using +
joined = lst + various
joined2 = various + lst
asbefore = x + various

# Access an element of a lists using its 
y = various[1]
# Indexes can be expressions
z = joined2[two+1]
# We can use elements in expressions
w = 5*various[0]
# and function calls
print(joined2[-1])

# When writing a function to do something with a list whoe length is not
# predetermined, the len function is very useful
n = len(x)
print(len(joined))

# Add 'abc' as a new element at the end of various
various = various + ['abc']