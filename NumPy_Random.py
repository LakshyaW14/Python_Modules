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
print("8"*20)
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
# sea.displot([0,1,2,3,4,5,6])
# plt.show()

# Plotting a Displot Without the Histogram
# sea.displot([0,1,2,3,4,5,6], kind="kde")
# sea.displot([0,1,2,3,4,5,6], kind="ecdf")
# plt.show()


# Normal distribution 
# The Normal Distribution is one of the most important distributions.
# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
# takes three parameters log, scale , size 

x = random.normal(size=(2,3))
y = random.normal(loc=1,scale=2, size=(2,3))

# sea.displot(random.normal(size=1000), kind="kde")
# plt.show()
# The curve of a Normal Distribution is also known as the Bell Curve because of the bell-shaped curve.

# Binomial Distribution - is a Discrete Distribution 
# three parameters n ,p ,size 

x = random.binomial(n=10, p=0.5, size=10)
# sea.displot(random.binomial(n=10, p=0.5, size= 1000))
# plt.show()


# Difference between normal and binomial distribution 
data = {
    "Normal" : random.normal(loc=50, scale=5, size=1000),
    "Binomial": random.binomial(n=100, p=0.5, size=1000)
}
# sea.displot(data, kind="kde")
# plt.show()

# Poisson Distribution --is a Discrete Distribution.
# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

# It has two parameters:
# lam - rate or known number of occurrences 
# size - The shape of the returned array.
print(random.poisson(lam=2, size=10))

# sea.displot(random.poisson(lam=2,size=1000))
# plt.show()

#Difference between Normal and Poisson Distribution 

Data = {
    "Normal": random.normal(loc=50, scale=7, size=1000),
    "Poisson": random.poisson(lam=50, size=1000),
    "Binomial" : random.binomial(n =1000, p=0.1, size=1000)
}
# sea.displot(Data, kind="kde")
# plt.show()


# Uniform Distribution
# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers.

# It has three parameters:
# low - lower bound - default 0.0
# high - upper bound - default 1.0
# size - The shape of the returned array
x = random.uniform(size=(2,3))

sea.displot(random.uniform(size=1000),kind="kde")
#plt.show()

# Logistic Distribution
# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.

# It has three parameters:
# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.

x = random.logistic(loc=1, scale=2, size=(2,3))
# sea.displot(random.logistic(size=1000), kind="kde")
# plt.show()
data = {
    "Normal":random.normal(scale=2, size=1000),
    "Logistic": random.logistic(size=1000)
}
sea.displot(data, kind="kde")
plt.show()

# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
# It has three parameters:
# n - number of times to run the experiment.
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

# visualization is similar to multiple binomial distribution 

# Exponential Distribution
# Exponential distribution is used for describing time till next event e.g. failure/success etc.

# It has two parameters:

# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

# size - The shape of the returned array.
x = random.exponential(scale=2, size=(2,3))
sea.displot(random.exponential(size=1000), kind="kde")

# Chi Square Distribution
# Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:

# df - (degree of freedom).

# size - The shape of the returned array.
x = random.chisquare(df=2, size=(2,3))
sea.displot(random.chisquare(df=1, size=1000), kind="kde")

# Rayleigh Distribution
# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

x = random.rayleigh(scale=2, size=(2,3))
sea.displot(random.rayleigh(size=1000), kind="kde")

# Pareto Distribution
# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

# It has two parameter:

# a - shape parameter.

# size - The shape of the returned array.
x= random.pareto(a=2, size=(2,3))
sea.displot(random.pareto(a=2, size=1000))

# Zipf distributions are used to sample data based on zipf's law.It has two parameters:

# a - distribution parameter.

# size - The shape of the returned array.In a collection, the nth common term is 1/n times of the most common term.\
#       E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

x= random.zipf(a=2, size=(2,3))
sea.displot(random.zipf(a=2, size=1000))

