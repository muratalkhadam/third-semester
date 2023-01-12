import numpy as np
import random as rd

from random import randint
import matplotlib.pyplot as plt


def cal_fitness(weight, value, population, threshold):
    fitness = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        s1 = np.sum(population[i] * value)
        s2 = np.sum(population[i] * weight)
        if s2 <= threshold:
            fitness[i] = s1
        else:
            fitness[i] = 0
    return fitness.astype(int)


def selection(fitness, num_parents, population):
    fitness = list(fitness)
    parents = np.empty((num_parents, population.shape[1]))
    for i in range(num_parents):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        parents[i, :] = population[max_fitness_idx[0][0], :]
        fitness[max_fitness_idx[0][0]] = -999999
    return parents


def crossover(parents, num_offsprings):
    offsprings = np.empty((num_offsprings, parents.shape[1]))
    crossover_point = int(parents.shape[1] / 2)
    crossover_rate = 0.7
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


def mutation(offsprings):
    mutants = np.empty((offsprings.shape))
    mutation_rate = 0.05
    for i in range(mutants.shape[0]):
        random_value = rd.random()
        mutants[i, :] = offsprings[i, :]
        if random_value > mutation_rate:
            continue
        int_random_value = randint(0, offsprings.shape[1] - 1)
        if mutants[i, int_random_value] == 0:
            mutants[i, int_random_value] = 1
        else:
            mutants[i, int_random_value] = 0
    return mutants


def optimize(weight, value, population, pop_size, num_generations, threshold):
    parameters, fitness_history = [], []
    num_parents = int(pop_size[0] / 2)
    num_offsprings = pop_size[0] - num_parents

    for _ in range(num_generations):
        fitness = cal_fitness(weight, value, population, threshold)
        fitness_history.append(fitness)
        parents = selection(fitness, num_parents, population)
        offsprings = crossover(parents, num_offsprings)
        mutants = mutation(offsprings)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = mutants

    print('Last generation: \n{}\n'.format(population))

    fitness_last_gen = cal_fitness(weight, value, population, threshold)
    print('Fitness of the last generation: \n{}\n'.format(fitness_last_gen))

    max_fitness = np.where(fitness_last_gen == np.max(fitness_last_gen))
    parameters.append(population[max_fitness[0][0], :])

    return parameters, fitness_history


if __name__ == '__main__':
    items = 100
    knapsack_threshold = 500

    item_index = np.arange(1, items + 1)
    weight = np.random.randint(1, 20, size=items)
    value = np.random.randint(2, 30, size=items)

    print('Generated items with random weight and value:')
    print('Item No.   Weight   Value')
    for i in range(item_index.shape[0]):
        print(f'{item_index[i]}          {weight[i]}         {value[i]}')

    solutions_per_pop = 80
    pop_size = (solutions_per_pop, item_index.shape[0])
    print('Population size = {}'.format(pop_size))

    initial_population = np.random.randint(2, size=pop_size)
    initial_population = initial_population.astype(int)

    num_iterations = 1000
    print('Initial population: \n{}'.format(initial_population))

    parameters, fitness_history = optimize(weight, value, initial_population, pop_size, num_iterations,
                                           knapsack_threshold)
    print('The optimized parameters for the given inputs are: \n{}'.format(parameters))
    selected = item_index * parameters  # chromosomes

    print('\nSelected items that will maximize the knapsack:')
    total_weight = 0
    total_value = 0
    counter = 0
    for i in range(selected.shape[1]):
        if selected[0][i] != 0:
            print('{}'.format(selected[0][i]), end=" ")
            total_weight += weight[i]
            total_value += value[i]
            counter += 1

    print("\nAmount of selected items: ", counter)
    print("Total weight is:", total_weight)
    print("Total value is:", total_value)
    print("Avg value of selected items is:", total_value / counter)
    print(f"Avg value out of {items} generated:", sum(value) / items)

    # plot
    fitness_history_mean = [np.mean(fitness_history[i]) for i in range(len(fitness_history)) if i % 20 == 0]
    print("Fitness mean is", fitness_history_mean)

    fitness_history_max = [np.max(fitness_history[i]) for i in range(len(fitness_history)) if i % 20 == 0]
    print("Fitness max is", fitness_history_max)

    fitness_history_min = [np.min(fitness_history[i]) for i in range(len(fitness_history)) if i % 20 == 0]
    print("Fitness min is", fitness_history_min)

    plt.plot(list(range(0, num_iterations, 20)), fitness_history_mean, label='Mean Fitness')
    plt.plot(list(range(0, num_iterations, 20)), fitness_history_max, label='Max Fitness')
    plt.plot(list(range(0, num_iterations, 20)), fitness_history_min, label='Min Fitness')

    plt.legend()
    plt.title('Fitness through the iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness')

