import matplotlib.pyplot as plt
import random as rd

from random import randint

import numpy as np


def cal_fitness(weight, value, population, threshold):
    fitness = np.empty( population.shape[0] )
    for i in range( population.shape[0] ):
        s1 = np.sum( population[i] * value )
        s2 = np.sum( population[i] * weight )
        if s2 <= threshold:
            fitness[i] = s1
        else:
            fitness[i] = 0
    return fitness.astype( int )


def selection(fitness, num_parents, population):
    fitness = list( fitness )
    parents = np.empty( (num_parents, population.shape[1]) )
    for i in range( num_parents ):
        max_fitness_idx = np.where( fitness == np.max( fitness ) )
        parents[i, :] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return parents


def crossover(parents, num_offsprings):
    offsprings = np.empty( (num_offsprings, parents.shape[1]) )
    crossover_point = int( parents.shape[1] / 2 )
    crossover_rate = 0.5
    i = 0
    while parents.shape[0] < num_offsprings:
        parent1_index = i % parents.shape[0]
        parent2_index = (i + 1) % parents.shape[0]
        x = rd.random()
        if x > crossover_rate:
            continue
        parent1_index = i % parents.shape[0]
        parent2_index = (i + 1) % parents.shape[0]
        offsprings[i, 0:crossover_point] = parents[parent1_index, 0:crossover_point]
        offsprings[i, crossover_point:] = parents[parent2_index, crossover_point:]
        i += 1
    return offsprings


def mutation(offsprings, rate):
    mutants = np.empty( (offsprings.shape) )
    mutation_rate = rate
    for i in range( mutants.shape[0] ):
        random_value = rd.random()
        mutants[i, :] = offsprings[i, :]
        if random_value > mutation_rate:
            continue
        int_random_value = randint( 0, offsprings.shape[1] - 1 )
        if mutants[i, int_random_value] == 0:
            mutants[i, int_random_value] = 1
        else:
            mutants[i, int_random_value] = 0
    return mutants


def optimize(weight, value, population, pop_size, num_generations, threshold, mut_rate):
    parameters, fitness_history = [], []
    num_parents = int( pop_size[0] / 2 )
    num_offsprings = pop_size[0] - num_parents

    for _ in range( num_generations ):
        fitness = cal_fitness( weight, value, population, threshold )
        fitness_history.append( fitness )
        parents = selection( fitness, num_parents, population )
        offsprings = crossover( parents, num_offsprings )
        mutants = mutation( offsprings, mut_rate )
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants

    print('Last generation: \n{}\n'.format(population))

    fitness_last_gen = cal_fitness(weight, value, population, threshold)
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))

    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0], :])

    return parameters, fitness_history


def mutation_with_param(offsprings, mutation_rate):
    mutants = np.empty( (offsprings.shape) )
    for i in range( mutants.shape[0] ):
        random_value = rd.random()
        mutants[i, :] = offsprings[i, :]
        if random_value > mutation_rate:
            continue
        int_random_value = randint( 0, offsprings.shape[1] - 1 )
        if mutants[i, int_random_value] == 0:
            mutants[i, int_random_value] = 1
        else:
            mutants[i, int_random_value] = 0
    return mutants


# list of different mutation rates to test
mutation_rates = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
fitness_history_list = []

items = 100
knapsack_threshold = 500

item_index = np.arange(1, items + 1)
weight = np.random.randint(1, 20, size=items)
value = np.random.randint(2, 30, size=items)

solutions_per_pop = 80
pop_size = (solutions_per_pop, item_index.shape[0])

initial_population = np.random.randint(2, size=pop_size)
initial_population = initial_population.astype(int)

num_iterations = 1000

for rate in mutation_rates:
    _, fitness_history = optimize(weight, value, initial_population, pop_size, num_iterations, knapsack_threshold,
                                   rate)
    fitness_history_list.append(fitness_history)

# plot the mean fitness of each generation for each mutation rate
for i in range(len(mutation_rates)):
    mean_fitness = [np.mean(fitness_history_list[i][j]) for j in range(num_iterations)]
    plt.plot(list(range(num_iterations)), mean_fitness, label='Mutation rate = {}'.format(mutation_rates[i]))
    print(mutation_rates[i], '----->', np.mean(mean_fitness), sep=' ')

plt.legend()
plt.title('Effect of Mutation Rate on Mean Fitness')
plt.xlabel('Generation')
plt.ylabel('Mean Fitness')
plt.show()
