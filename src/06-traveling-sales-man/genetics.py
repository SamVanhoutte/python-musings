import random
import operator
import abc

class Gene:
    def __init__(self):
        return

class Individual(object):
    __metaclass__ = abc.ABCMeta
    __sequence = []
    Fitness: int = 0

    def __init__(self, sequence):
        self.__sequence = sequence
        return

    @abc.abstractmethod
    def calculate_fitness(self):
        pass

    @abc.abstractmethod
    def mate(self, mating_partner):
        pass


class Population:
    __individuals = []
    __size = 6
    __elite_size = 3

    def __init__(self, sequence, population_size: int = 6, elite_size: int = 3):
        # We will initialize the population with the defined population size and we'll create random individuals
        self.__individuals = sequence
        self.__size = population_size
        self.__elite_size = elite_size

        return

    def get_fastest_route(self):
        return self.__rank_routes()[0]

    def __rank_routes(self):
        sorted_routes = []
        fitnessResults = {}
        for i in range(0,len(self.__individuals)):
            fitnessResults[i] = self.__individuals[i].calculate_fitness()
        fitnessResults = sorted(fitnessResults.items(), key = operator.itemgetter(1), reverse = True)
        for ind_tuple in fitnessResults:
            # tuple values of the index and the fitness, taking the index now
            sorted_routes.append(self.__individuals[ind_tuple[0]])
        return sorted_routes

    def create_mating_pool(self):
        ranked_routes = self.__rank_routes()
        return [r for r in ranked_routes[:self.__elite_size]]

    def breed(self):
        new_generation = self.create_mating_pool()
        for _ in range(0, self.__size - self.__elite_size):
            # adding breeds of the mating population
            parent01 = random.choice(new_generation)
            parent02 = parent01
            # make sure to not have 'self-mating', as that would be a waste of CPU cycles
            while(parent02 == parent01): 
                parent02 = random.choice(new_generation)
            child = parent01.mate(parent02)
            new_generation.append(child)

        self.__individuals = new_generation
        return new_generation

    def survival_of_the_fittest(self, generation_count: int = 15):
        for _ in range(0, generation_count):
            self.breed()
        
        return self.__individuals[0]