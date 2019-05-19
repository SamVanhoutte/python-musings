import unittest                     # unit testing ftw
# import numpy as np
import genetics as gen
import route as rt
import city
import random
import math

class TestMethods(unittest.TestCase):
    def test_city(self):
        antwerp = city.City('Antwerp', 34, 33)
        ghent = city.City('Ghent', 54, 34)
        kortrijk = city.City('Kortrijk', 80, 23)
        brussels = city.City('Brussels', 62, 44)
        route01 = rt.Route([antwerp, ghent, kortrijk, brussels, antwerp])
        route02 = rt.Route([antwerp, kortrijk, ghent, brussels, antwerp])
        route03 = rt.Route([antwerp, ghent, brussels, kortrijk, antwerp])
        #population = gen.Population([route01, route02, route03], 3)
        self.assertEqual(antwerp.Name, 'Antwerp')
        route01.calculate_fitness()
        self.assertGreater(route01.Fitness, 0)
    
    def test_distance(self):
        city01 = city.City('01', 0, 2)
        city02 = city.City('02', 4, 5)
        city03 = city.City('03', 4, 2)
        
        # 1D Horizontal calculation
        self.assertEqual(4.0, rt.Route.calculate_distance(city01, city03))
        # 1D Vertical calculation
        self.assertEqual(3.0, rt.Route.calculate_distance(city03, city02))
        # 2D Pythagoras calculation
        self.assertEqual(5.0, rt.Route.calculate_distance(city01, city02))

        route01 = rt.Route([city01, city02, city03])
        route01.calculate_fitness()
        self.assertLess(0, route01.Fitness)
        self.assertEqual(12, route01.get_distance())

        route02 = rt.Route([city01, city02, city03, city01])
        route02.calculate_fitness()
        self.assertLess(0, route02.Fitness)
        self.assertEqual(12, route02.get_distance())

    def test_mating_pool(self):
        city01 = city.City('01', 0, 2)
        city02 = city.City('02', 4, 5)
        city03 = city.City('03', 4, 2)
        city04 = city.City('04', 7, 3)
        city05 = city.City('05', 1, 6)
        city06 = city.City('06', 3, 2)
        city07 = city.City('07', 10, 8)
        genes = [city01, city02, city03, city04, city05, city06, city07]
        pop_size = 8
        elite_size = 3
        routes = []

        for i in range(0, pop_size):
            routes.append(rt.Route(random.sample(genes, len(genes))))
            
        population = gen.Population(routes, pop_size, elite_size)
        mating_pool = population.create_mating_pool()
        self.assertEqual(len(mating_pool), elite_size)

    def test_breeding(self):
        city01 = city.City('01', 0, 2)
        city02 = city.City('02', 4, 5)
        city03 = city.City('03', 4, 2)
        city04 = city.City('04', 7, 3)
        city05 = city.City('05', 1, 6)
        city06 = city.City('06', 3, 2)
        city07 = city.City('07', 10, 8)
        sequence = [city01, city02, city03, city04, city05, city06, city07]
        mating_sequence = [city03, city01, city04, city07, city05, city06, city02]
        route01 = rt.Route(sequence)
        route02 = rt.Route(mating_sequence)
        child_route = route01.mate(route02)
        self.assertEqual(len(route01.Sequence), len(child_route.Sequence))
        return

    def test_new_generation(self):
        city01 = city.City('01', 0, 2)
        city02 = city.City('02', 4, 5)
        city03 = city.City('03', 4, 2)
        city04 = city.City('04', 7, 3)
        city05 = city.City('05', 1, 6)
        city06 = city.City('06', 3, 2)
        city07 = city.City('07', 10, 8)
        genes = [city01, city02, city03, city04, city05, city06, city07]
        pop_size = 8
        routes = []

        for i in range(0, pop_size):
            routes.append(rt.Route(random.sample(genes, len(genes))))
            
        population = gen.Population(routes, pop_size)
        new_generation = population.breed()
        self.assertEqual(pop_size, len(new_generation))

    def test_shortest_route(self):
        # define 10 routes each with the same x and y - shortest route would be the sequence of those routes by name
        genes = []
        route_length = 10
        for i in range(0, route_length):
            genes.append(city.City(str(i), i, i))
        pop_size = 100
        routes = []

        for i in range(0, pop_size):
            routes.append(rt.Route(random.sample(genes, len(genes))))
            
        population = gen.Population(routes, pop_size, pop_size // 2)
        fastest_route = population.survival_of_the_fittest(30)

        shortest_distance  = math.sqrt((route_length-1)**2 * 2) * 2 # (pythagoras to x,y = 10,10)

        self.assertAlmostEqual(fastest_route.get_distance(), shortest_distance)