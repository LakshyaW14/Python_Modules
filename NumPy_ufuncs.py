# ufunc stands for universal function,\
#  they are numpy functions that operate on ndarray object
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
# ufuncs also take additional arguments, like:

# where boolean array or condition defining where the operations should take place.

# dtype defining the return type of elements.

# out output array where the return value should be copied.



# Converting iterative statements into a vector based operation is called vectorization.

# It is faster as modern CPUs are optimized for such operations.
import numpy as np

arr1= [1,2,3,4]     #without ufunc, py builtin zip function 
arr2= [2,3,4,6]
arr3 = []
for i,j in zip(arr1,arr2):
    arr3.append(i+j)
print(arr3)

# with ufunc add()
x=np.array(arr1)
y= np.array(arr2)
z= np.add(x,y)
print(z)


#Create your own ufunction

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.
def substract(x,y):
    return x,y
def myadd(x,y):
    return x+y
myadd =np.frompyfunc(myadd, 2, 1)
print(myadd(arr1,arr2))
print(type(myadd))  # custom ufunc
print(type(substract)) # normal function 

#Simple arithmetic 
# The add() function sums the content of two arrays, and return the results in a new array.

print(np.add(arr1,arr2))

# The subtract() function subtracts the values from one array with the values from another array, \
# and return the results in a new array.
print(np.subtract(arr1,arr2))

# The multiply() function multiplies the values from one array with the values from another array, \
# and return the results in a new array.

print(np.multiply(arr1,arr2))

# The divide() function divides the values from one array with the values from another array, \
# and return the results in a new array.
print(np.divide(arr1,arr2))

# The power() function rises the values from the first array to the power of the values of the second array,\
#  and return the results in a new array.

print(np.power(arr1,arr2))

# Both the mod() and the remainder() functions return the remainder of the values in the first array corresponding to the values in the second array, \
# and return the results in a new array.
print(np.mod(arr1,arr2))
print(np.remainder(arr1,arr2))

# The divmod() function return both the quotient and the mod. The return value is two arrays, the first array contains the quotient \
    # and second array contains the mod.

print(np.divmod(arr1,arr2))

# Both the absolute() and the abs() functions do the same absolute operation element-wise but \
# we should use absolute() to avoid confusion with python's inbuilt math.abs()
print(np.absolute(x,y))

# Rounding DecimalsRemove the decimals, and return the float number closest to zero.\
#  Use the trunc() and fix() functions.

print(np.trunc([-3.44444, 3.5555]))
print(np.fix([-3.3333,3.444]))

# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
# E.g. round off to 1 decimal point, 3.16666 is 3.2
print(np.around(3.2666,2))


# The floor() function rounds off decimal to nearest lower integer.
# E.g. floor of 3.166 is 3.
print(np.floor([-3.333,5.333]))

# The ceil() function rounds off decimal to nearest upper integer.
# E.g. ceil of 3.166 is 4.
print(np.ceil([-3.444, 5.4333]))

# NumPy provides functions to perform log at the base 2, e and 10.
# We will also explore how we can take log for any base by creating a custom ufunc.
# All of the log functions will place -inf or inf in the elements if the log can not be computed.
arr = np.arange(1,10)
print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))
# log at any base 
from math import log 
nplog = np.frompyfunc(log,2,1)
print(nplog(100,15))
print()

# Summations
# What is the difference between summation and addition?

# Addition is done between two arguments whereas summation happens over n elements.

print(np.add(arr1,arr2))
print()
print(np.sum([arr1,arr2]))
# Over an Axis

print(np.sum([arr1,arr2], axis=1))
print()

# Cummulative sum means partially adding the elements in array.
# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
print(np.cumsum(arr))
print()

# To find the product of the elements in an array, use the prod() function.
print(np.prod(arr))
print(np.prod([arr1,arr2]))
# over axis 
print(np.prod([arr1,arr2], axis=1))
print(np.cumprod(arr))
print()

# A discrete difference means subtracting two successive elements.
# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

# To find the discrete difference, use the diff() function.
print(np.diff(arr))

# We can perform this operation repeatedly by giving parameter n.
print(np.diff(arr, n=2))

# The Lowest Common Multiple is the smallest number that is a common multiple of two numbers
print(np.lcm(4,6))
print(np.lcm.reduce([3,6,9]))
print(np.lcm.reduce(arr))
print()

# The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor)\
#  is the biggest number that is a common factor of both of the numbers.
print(np.gcd(6,9))
print(np.gcd.reduce([20, 8, 32, 36, 16]))
print()


# Trigonometric Functions
# NumPy provides the ufuncs sin(), cos() and tan() \
# that take values in radians and produce the corresponding sin, cos and tan values.
print(np.sin(np.pi/2))
array= np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
print(np.sin(array))

#deg to rad 
print(np.deg2rad([90,180,270,360]))
# RAD TO DEG
print(np.rad2deg(array))
print()

# Finding Angles
# Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
print(np.arcsin(1.0))
print(np.arcsin([1.0, -1, 0.1]))

print(np.hypot(3,4))
# NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values..
print(np.sinh(np.pi/2))
print(np.cosh(array))
print()

# Finding Angles
# Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
print(np.arcsinh(1.0))
# Angles of Each Value in Arrays
print(np.arctanh([1.0,0.2,0.4]))
print()

# A set in mathematics is a collection of unique elements.

# Sets are used for operations involving frequent intersection, union and difference operations.
array1 = np.array([1,1,1,1,2,3,3,2,4,4,5,6])
print(np.unique(arr))

# To find the unique values of two arrays, use the union1d() method.
print(np.union1d(arr1, arr2))

# To find only the values that are present in both arrays, use the intersect1d() method.
print(np.intersect1d(arr1, arr2, assume_unique=True))

# the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.
# To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
print(np.setdiff1d(arr1, arr2, assume_unique=True))

# To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
print(np.setxor1d(arr1, arr2, assume_unique=True))

