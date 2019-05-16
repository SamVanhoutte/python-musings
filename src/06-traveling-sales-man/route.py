import city
import numpy as np

class Individual:
    Fitness: int = 0

    def __init__(self):
        return

class Route(Individual):
    Sequence = []
    def __init__(self, individuals):
        # get sequence of cities
        Seq = individuals
        # calculate distance and set the Fitness of the Individual
        route_distance = 0.0
        for idx, city in enumerate(individuals, start=0):
            route_distance += self.calculate_distance(city, individuals[idx])
        self.Fitness = route_distance
        return

    def calculate_distance(self, city01: city.City, city02: city.City):
        coord01 = np.array([city01.Lat, city01.Lon, city01.Height])
        coord02 = np.array([city02.Lat, city02.Lon, city02.Height])
        
        squared_dist = np.sum(coord01**2 + coord02**2, axis=0)
        return np.sqrt(squared_dist)
        