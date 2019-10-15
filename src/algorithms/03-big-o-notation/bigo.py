#############################################################################
# Sam Vanhoutte - PG Applied AI - Programming                               #
# Reusable class to perform BigO plotting of different lambda executions    #
#############################################################################

import random
import string
import numpy
import timeit                       # perf testing
import matplotlib.pyplot as plt

class bigo(object):
    @staticmethod
    # Wrapper to call function easily with arguments
    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    # Test to run with variable parameters
    @staticmethod
    def multiPerfTest(listOfLambdas, n_values, executions, title='Big O', repeat = 10):
        lambaresults = []
        iteration = 0
        for call in listOfLambdas:
            # Not using the timeit.repeat (as it requires string statements)
            results = []
            for _ in range(0, repeat):
                # we are executing the lambda expression for every repeat 
                # measure the execution times - one for every execution
                results.append(timeit.timeit(call, number=executions))
            
            # Take the median, though some say the minimum should be taken - or the average of the mid 8 results
            lambaresults.append(numpy.median(results))
            iteration = iteration + 1

        #now plot the results
        print(lambaresults)
        plt.plot(n_values, lambaresults)
        plt.title(title)
        plt.ylabel('Duration')
        plt.show()

    # Generate random data sets
    @staticmethod
    def getRandomImage(width, height):
        image = numpy.random.randint(low = 0, high = 255, size = (height, width, 3))
        return image


    # Test to run with variable parameters
    @staticmethod
    def perfTest(func, *args, executions, repeat = 10):
        # Generate random strings of the configured length
        results = []
        # Not using the timeit.repeat (as it requires string statements)
        for _ in range(0, repeat):
            # set up delegate
            wrapped = bigo.wrapper(func, *args)
            # measure the execution times - one for every execution
            results.append(timeit.timeit(wrapped, number=executions))
        
        # Take the mean, though some say the minimum should be taken - or the average of the mid 8 results
        print(numpy.mean(results), executions, sep=";")

