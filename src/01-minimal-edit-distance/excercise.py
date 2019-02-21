###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Inspired by: https://github.com/trekhleb/javascript-algorithms/tree/master/src/algorithms/string/levenshtein-distance
###############################################

import numpy        # will be used for all matrix operations

class Excercise(object):
    @staticmethod
    def CalculateEditDistance(compareValue01, compareValue02, ignoreCase = False):
        # when ignoring the casing, we upper all values
        if(ignoreCase):    
            compareValue01 = compareValue01.upper()
            compareValue02 = compareValue02.upper()

        # init dictionary with dimensions, based on length of two values
        calculationMatrix = numpy.zeros(((len(compareValue02) + 1), (len(compareValue01) + 1)))
        # first set transitions to empty string (equal to the length of the val)
        for row in range(1, len(compareValue02) + 1):  # rows
            calculationMatrix[row][0] = row
        for col in range(1, len(compareValue01) + 1):  # cols
            calculationMatrix[0][col] = col

        # now calculate for every character
        for col in range(1, len(compareValue01) + 1):       # cols
            for row in range(1, len(compareValue02) + 1):   # rows
                if compareValue01[col - 1] == compareValue02[row - 1]:
                    cost = 0
                else:
                    cost = 1
                # Defining the cheapest option to navigate the matrix
                calculationMatrix[row][col] = min(  
                                                    calculationMatrix[row-1, col] + 1,      # the cost of deletion
                                                    calculationMatrix[row, col-1] + 1,      # the cost of insertion
                                                    calculationMatrix[row-1, col-1] + cost  # the cost of substitution
                                                )
        # return the 'bottom right' value in the matrix
        return calculationMatrix[len(compareValue02), len(compareValue01)]