# Traveling sales man - a genetic algorithm approach

Excercices that calculate shortest routes between different cities.  Here we apply genetic algorithms.  The cities are specified as 3D-points (x,y,z), so these could be used to calculate a route between planets as well. 

## Required packages

Install the following packages, with pip3 install

- random: used to randomly generate (test)data
- operator: used for sorting
- abc: used for abstract method implementation
- math: used for sqrt
- unittest: used for the unit tests 
- numpy: used for some array operations

## Source files description

__Genetics__: [genetics.py](../src/algorithms/06-traveling-sales-man/genetics.py)

In this file, the actual "generic" classes are being used, without the city/route specific logic.  This approach would allow to have other algorithms, with different principles also used, as long as ordered sequences are used in the different individuals 

- `Gene`
  - Class (currently empty) that defines a Gene (in our example, a City)

- `Individual`
  - Class that represents a possible solution for our problem.  (in our example, a Route is an individual)
  - `__init__(self, sequence)` : the constructor accepts a sequence of Gene instances that will be used to represent the individual
  - `Fitness` : the actual Fitness that will define who will survive in the mating pool.  In our case, the fitness is the inverse (1/distance) of the distance of the route.
  - `calculate_fitness(self)`: this abstract method has to be implemented (and is implemented in the Route class, in our excercises) to set the Fitness of the individual
  - `mate(self, mating_partner)`: this abstract method has to be implemented (and is implemented in the Route class, in our excercises) to mate (or breed) with another individual.  so two parent individuals will breed a child individual here

- `Population`
  - Class that represents a population of individuals.  
  - `__init__(self, individuals, population_size: int = 6, elite_size: int = 3)` : the constructor accepts a list of individuals and also values to specify the actual population size and the elite size.  The elite size will be used in the breeding of new generations and only the top N (elite size) of the current population individuals will be kept in the next generation.
  - `get_fittest_individual(self)` : this method returns the individual of the population with the highest fitness
  - `create_mating_pool(self)` : this method will rank all individuals and take the fittest individuals from the ranking (using the elite size, specified in the constructor)
  - `breed(self)` : this method will execute the following steps:
    - Create the mating pool (only keeping the fittest individuals)
    - Fill the new generation with new individuals to read the specified population size
    - These new individuals are created by randomly have two individuals from the maating pool to breed a new individual.
  - `survival_of_the_fittest(self, generation_count: int = 15)` : this method will take the initial start population and breed a number of generations in order to keep the best population at that time 

__Route__: [route.py](../src/algorithms/06-traveling-sales-man/route.py)

In this file, the different abstract methods for an Individual are implemented. 

- The fitness is calculated by adding distances between every city (taking the sequence in account) and then the inverse is taking, making sure the highest fitness will be for the shortest route.
- The mating process is implemented by taking a random part of the first parent (30% of the length) and by adding the remaining cities in sequence they appear in the second parent.  For this, some basic array operations are used.

__City__: [city.py](../src/algorithms/06-traveling-sales-man/city.py)

In this file, the city properties are kept, and the city is implemented as a Gene.  A name, the longitude, latitude and the height (for 3-d purposes) are being used.

