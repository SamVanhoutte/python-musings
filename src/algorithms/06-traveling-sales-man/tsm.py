import unittest                     # unit testing ftw
import genetics as gen
import route as rt
import city
import random
import math
import matplotlib.pyplot as plt

pop_size = 100
generation_count = 100

# Hardcoded cities
city01 = city.City('01', 0, 2, 4)
city02 = city.City('02', 4, 5, 2)
city03 = city.City('03', 4, 2, 8)
city04 = city.City('04', 7, 3, 9)
city05 = city.City('05', 1, 6, -1)
city06 = city.City('06', 3, -2, -5)
city07 = city.City('07', 10, 8, 3)
city08 = city.City('08', -6, 3, 8)
genes = [city01, city02, city03, city04, city05, city06, city07, city08]

# Generating cities in one straight line
genes = []
route_length = 25
for i in range(0, route_length):
    genes.append(city.City(str(i), i, i))
print ('The shortest possible distance is ',  math.sqrt((route_length-1)**2 * 2) * 2)

routes = []
for i in range(0, pop_size):
    routes.append(rt.Route(random.sample(genes, len(genes))))
    
population = gen.Population(routes, pop_size, pop_size // 3)

distances = [population.get_fittest_indivual().get_distance()]
for _ in range(0, generation_count):
    population.breed()
    # add shortest distance in route
    fastest = population.get_fittest_indivual()
    distances.append(fastest.get_distance())
    fastest.render()

plt.plot(range(0, generation_count + 1), distances)
plt.title('Distance of the path for every generation')
plt.ylabel('Distance')
plt.ylabel('Generation')
# plt.axis([0, generation_count + 1, 0, 300])
plt.show()