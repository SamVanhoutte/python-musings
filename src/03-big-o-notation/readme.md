# Big-O notation and algorithm analysis
This sample shows a generic class that can be used to analyze algorithms and plot the impact of 'N' on the actual performance and duration of an algorithm.

In order to analyse it, an array of 'n-values' has to be built and given to a lambda(x) that calls the actual algorithm to be tested.  The class also allows for data generation, in this case the random generation of an RGB image of a given width/height.

## [bigo.py](03-big-o-notation/bigo.py)

This file measures the time to execute the algorithms, and plots the impact of N on the duration.  It uses the timeit module that actually executes the lambda function to be tested.  The median value is taken and added as y-value to the plot, where the n-values are plotted on the x-axis.

The following static methods are available to the users of the module:

`multiPerfTest(listOfLambdas, n_values, executions, title='Big O', repeat = 10)`
This method executes the lambdas and plots the chart for all n-values

- `listOfLambdas`: an array of lambda functions (of the same length as the n_values array) to be tested
- `n_values`: an array of int values (of the same length as the lambda count) that are representing 'N' 
- `executions`: an int value indicating how many times the lambdas have to be executed (and the sum is taken)
- `title`: the title of the test that will be plotted on the chart
- `repeat`: the number of repeats for every execution

`getRandomImage(width, height)`
This method generates a random RGB image as a numpy array

- `width`: the width of the image in pixels
- `height`: the height of the image in pixels

## [algorithm_analysis.py](algorithm_analysis.py)

This file is testing 3 algorithms for the big-O performance test

- maskRandomPhoto : generating random picture and changing pixels in certain range
- calculate_regular_fact : calculating the factor function in a regular manner
- calculate_recursive_fact : calculating the factor function in a recursive manner