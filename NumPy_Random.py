# Numpy Random Module
#Random number does NOT mean a different number every time.\
#Random means something that can not be predicted logically.

#Random numbers generated through a generations algorithm are called Pseudo Random 

from numpy import random
import numpy as np

# Generate a random integer 
x = random.randint(100)

# Generate a random float 
print(random.rand())
print (random.rand(5))
print(random.rand(3,5))
 
#Generate random array 
y = random.randint(100, size =(5))  # 1D
z = random.randint(100, size = (3,5))

# Generate Random Number From Array
# Array as a parameter and randomly returns a value 
print(random.choice(y)) 
print(random.choice(y, size=(3)))

#Random Data Distribution 
# Data Distribution is a list of all possible values, and how often each value occurs.
# A random distribution is a set of random numbers that follow a certain probability density function.

# The probability is set by a number between 0 and 1, where 0 means that the value will never occur and \
    # 1 means that the value will always occur.
x = random.choice([3,4,5,6,7], p =[0.1,0.3,0.5,0.0,0.1], size=(10))
# sum of all probability numbers must be 1

x = random.choice([3,4,5,6,7], p =[0.1,0.3,0.5,0.0,0.1], size=(3,5))


#Random Permutations of Elements
# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# Shuffle( ) and permutation()

array = np.array([1,2,3,4,5,7])
random.shuffle(array)       # shuffle method makes changes to the original array , it means changing arrangements of elements 
print(array)        

#Generating Permutation of Arrays
# the original array remains unchanged , returns a re-arranged array
print(random.permutation(array))

# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs.\
#  It will be used to visualize random distributions.

# Displots
# Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as plt 
import seaborn as sea

# plotting a Displot 
sea.displot([0,1,2,3,4,5,6])
# plt.show()

# Plotting a Displot Without the Histogram
sea.displot([0,1,2,3,4,5,6], kind="kde")
sea.displot([0,1,2,3,4,5,6], kind="ecdf")
plt.show()
