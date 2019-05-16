import unittest                     # unit testing ftw
# import numpy as np
import population as pop
import route as rt
import city

class TestMethods(unittest.TestCase):
    def test_city(self):
        antwerp = city.City('Antwerp', 34, 33)
        ghent = city.City('Ghent', 54, 34)
        kortrijk = city.City('Kortrijk', 80, 23)
        brussels = city.City('Brussels', 62, 44)
        route01 = rt.Route([antwerp, ghent, kortrijk, brussels, antwerp])
        route02 = rt.Route([antwerp, kortrijk, ghent, brussels, antwerp])
        route03 = rt.Route([antwerp, ghent, brussels, kortrijk, antwerp])
        population = pop.Population([route01, route02, route03])
        self.assertEqual(antwerp.Name, 'Antwerp')
        self.assertGreater(route01.Fitness, 0)