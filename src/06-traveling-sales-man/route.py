import numpy as np
import math
import genetics as gen
import city 
import random

class Route(gen.Individual):
    Sequence = []
    
    def __init__(self, individuals):
        # get sequence of cities
        self.Sequence = individuals
        pass

    def calculate_fitness(self):
        # calculate distance and set the Fitness of the Individual
        route_distance = 0.0
        last_city_index = len(self.Sequence) - 1
        for idx, city in enumerate(self.Sequence):
            if(last_city_index==idx):
                # last city in the route, calculate distance to beginning
                next_city = self.Sequence[0]
            else:
                # taking the next city in the sequence
                next_city = self.Sequence[idx+1]
            edge_distance = self.calculate_distance(city, next_city)
            route_distance += edge_distance
        # We divide 1 by the distance, resulting in the highest fitness for the shortest route
        self.Fitness = 1 / route_distance
        return self.Fitness
    
    def mate(self, mating_partner):
        # ordered cross over partnering
        # taking a random part of the sequence from this Route 
        # and add the remaining ones in sequence they appear in the mating_partner 
        child_route = []

        # Taking ca 30% of this route at a random location
        seq_to_keep = len(self.Sequence) // 3
        start_position = random.randint(0, len(self.Sequence) - seq_to_keep - 1)
        parent_route = self.Sequence[start_position:start_position + seq_to_keep]
        partner_cities_to_keep = [city for city in mating_partner.Sequence if city not in parent_route]
        prefix = partner_cities_to_keep[0:start_position]
        suffix = partner_cities_to_keep[start_position:] # take remainder
        child_route = Route(prefix + parent_route + suffix)
        #print('Mating routes:')
        #self.render()
        #mating_partner.render()
        #child_route.render()
        return child_route

    def render(self):
        route_print = 'Distance (' + str(self.get_distance()) + "'): "
        for r in self.Sequence:
            route_print += (r.Name) + ' > '

        print (route_print)

    def get_distance(self):
        if (self.Fitness==0):
            self.calculate_fitness()
        return 1 / self.Fitness

    @staticmethod
    def calculate_distance(city01: city.City, city02: city.City):
        d = math.sqrt(
            math.pow(city02.Lat - city01.Lat, 2) +
            math.pow(city02.Lon - city01.Lon, 2) +
            math.pow(city02.Height - city01.Height, 2)* 1.0) 
        return d