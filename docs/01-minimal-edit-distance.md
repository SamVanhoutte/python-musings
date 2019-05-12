
# Minimal edit distance
This sample calculates the minimum required distance to go from one string to another.  This algorithm is often known and refered to as the Levenshtein distance algorithm.

Every required operation adds to the cost of that distance.  
The following operations are available:

- Remove character
- Add character
- Replace character

The sample is using a matrix to calculate the traversal from one string to the other.  This is inspired by several articles explaing this algorithm (I didn't invent it myself), such as [this one](https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/string/levenshtein-distance).

## [Excercise.py](../src/01-minimal-edit-distance/excercise.py)

This file contains the actual method that calculates the minimum distance.  It uses numpy for some basic matrix operations (such as the initiation, the calculation of the mean, etc...)
Also the method allows to calculate the distance in a case-insensitive way.  

## [Test_unit_excercise.py](../src/01-minimal-edit-distance/test_unit_excercise.py)

This file contains some unit tests, using the standard unittest module from Python.  This test class contains some basic tests that verify the distance between two strings.

## [Perf-excercise.py](../src/01-minimal-edit-distance/perf_excercise.py)

This file measures the time to execute the algorithm, and the impact of the length of the comparison values.  It uses the timeit module that needs something like a delegate if functions are to be executed with parameters.  (the wrapper function)