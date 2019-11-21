###############################################
# Sam Vanhoutte - PG Applied AI - Programming
# Unit tests, for the minimum edit distance
###############################################
import unittest                                             # unit testing ftw
from nltk_flightbooking_intent import FlightChecker    # importing the actual code

class TestIntents(unittest.TestCase):
    def test_tampa_as_verb(self):
        statement = "I want to book a flight from Seattle to Brussels"
        source, destination = FlightChecker.DetectRoute(statement, True)
        self.assertEqual("Seattle", source)
        self.assertEqual("Brussels", destination)
    def test_easy_one_02(self):
        statement = "I need a plane from Boston to Philadelphia."
        source, destination = FlightChecker.DetectRoute(statement)
        self.assertEqual("Boston", source)
        self.assertEqual("Philadelphia", destination)
    def test_combined_name(self):
        statement = "Book me a flight from Washington D.C. to Detroit."
        source, destination = FlightChecker.DetectRoute(statement)
        self.assertEqual("Washington D.C.", source)
        self.assertEqual("Detroit", destination)
    def test_different_formulation(self):
        statement = "I want to book a flight to Atlanta, I’m leaving from Denver."
        source, destination = FlightChecker.DetectRoute(statement)
        self.assertEqual("Atlanta", source)
        self.assertEqual("Denver", destination)
        