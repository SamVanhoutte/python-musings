import unittest                     # unit testing ftw
import genetics as gen
import route as rt
import city
import random
import math

city01 = city.City('01', 0, 2)
city02 = city.City('02', 4, 5)
city03 = city.City('03', 4, 2)
city04 = city.City('04', 7, 3)
city05 = city.City('05', 1, 6)
city06 = city.City('06', 3, 2)
city07 = city.City('07', 10, 8)
city08 = city.City('08', 6, 3)
genes = [city01, city02, city03, city04, city05, city06, city07, city08]

genes = []
route_length = 10
for i in range(0, route_length):
    genes.append(city.City(str(i), i, i))
print ('The shortest possible distance is ',  math.sqrt((route_length-1)**2 * 2) * 2)
pop_size = 100

routes = []
generation_count = 30

for i in range(0, pop_size):
    routes.append(rt.Route(random.sample(genes, len(genes))))
    
population = gen.Population(routes, pop_size, pop_size // 2)

distances = [population.get_fastest_route().get_distance()]
for _ in range(0, generation_count):
    population.breed()
    # add shortest distance in route
    fastest = population.get_fastest_route()
    distances.append(fastest.get_distance())
    fastest.render()