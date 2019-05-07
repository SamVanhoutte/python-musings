#############################################################################
# Sam Vanhoutte - PG Applied AI - Programming                               #
# Examples of measuring the performance of different algorithms, with Big-O #
#############################################################################

# perform big o analysis on fact method
import matplotlib.pyplot as plt
import numpy as np
import sys
from bigo import bigo
#from big_o import BigOAnalysis

n_values = [10,20,30,50, 100, 200, 400, 600, 1000]

# Test the masking of an image, which seems to be O(n), looking at the graph
# n values are the size (dimension) of the image that has to be masked
def maskRandomPhoto(width):
    photo = bigo.getRandomImage(width, width)
    masked_image = np.where (photo > 150, 255, 0)

def mask(x): return lambda : maskRandomPhoto(x)
    
maskLambdas = [mask(i) for i in n_values]
bigo.multiPerfTest(maskLambdas, n_values, 10, 'Masking photos')

# Test the factor function version 1, which seems to be O(n), looking at the graph
# n values are the numbers that have to be 'factored'

def calculate_regular_fact(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

def regular_fact(x): return lambda : calculate_regular_fact(x)
    
regularFactLambdas = [regular_fact(i) for i in n_values]
bigo.multiPerfTest(regularFactLambdas, n_values, 1000, 'Regular factor function')

# Test the factor function version 1, which seems to be O(n), looking at the graph
# n values are the numbers that have to be 'factored'
def calculate_recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * calculate_recursive_fact(n-1)

def recursive_fact(x): return lambda : calculate_recursive_fact(x)

recursiveFactLambdas = [recursive_fact(i) for i in n_values]
sys.setrecursionlimit(np.max(n_values) * 2)
bigo.multiPerfTest(recursiveFactLambdas, n_values, 1000, 'Recursive factor function')