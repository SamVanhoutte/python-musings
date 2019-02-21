import random
import string
import numpy
import timeit                       # perf testing
from excercise import Excercise     # importing the actual code

# Wrapper to call function easily with arguments
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# Actual method to be tested
def measure(value01, value02):
    Excercise.CalculateEditDistance(value01, value02)

# Test to run with variable parameters
def perfTest(stringLength01, stringLength02, executions, repeat = 10):
    # Generate random strings of the configured length
    results = []
    # Not using the timeit.repeat (as it requires string statements)
    for _ in range(0, repeat):
        value01 = ''.join(random.choices(string.ascii_uppercase, k=stringLength01))
        value02 = ''.join(random.choices(string.ascii_uppercase, k=stringLength02))
        wrapped = wrapper(measure, value01, value02)
        results.append(timeit.timeit(wrapped, number=executions))
    # Take the mean, though some say the minimum should be taken
    print(stringLength01, stringLength02, numpy.mean(results), executions, sep=";")


# Run and print duration of different string comparisons
print('stringLength01;stringLength02;duration')
perfTest(1,1,100)
perfTest(4,5,100)
perfTest(4,40,100)
perfTest(1,100,100)
perfTest(100,100,100)
perfTest(1,1,300)
perfTest(4,5,300)
perfTest(4,40,300)
perfTest(1,100,300)
perfTest(100,100,300)

print('test completed')