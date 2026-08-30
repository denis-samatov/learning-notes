# Genetic Algorithms with DEAP

Genetic algorithms (GAs) are heuristic optimization methods inspired by natural
selection and genetics. They're applied to a wide range of optimization and search
problems — finding global minima of functions, tuning model parameters, and more.

DEAP (Distributed Evolutionary Algorithms in Python) is a Python library that provides
building blocks for implementing genetic algorithms: tools for creating and evaluating
populations of individuals, crossover and mutation operators, and utilities for running
the evolutionary process.

## How a genetic algorithm works

1. **Population initialization** — create an initial population of random individuals.
2. **Fitness evaluation** — compute the fitness function for each individual in the
   population.
3. **Parent selection** — select the fittest individuals from the population for
   crossover.
4. **Crossover** — create new individuals by combining the genetic material of
   parents.
5. **Mutation** — introduce random changes to individuals' genetic material to
   maintain diversity in the population.
6. **Fitness evaluation of offspring** — compute the fitness function for the new
   individuals.
7. **Survivor selection** — select the fittest individuals from the population for the
   next generation.
8. **Repeat** — repeat from step 3 until a stopping criterion is reached (e.g. a
   maximum number of generations, or a target fitness level).

## Implementation with DEAP

DEAP provides a convenient interface for implementing genetic algorithms, built around
a few core elements:

- **Creator** — used to define new individual and fitness classes.
- **Toolbox** — a convenient way to register the functions used for evaluation,
  selection, crossover, and mutation.
- **Operators** — ready-made crossover and mutation operators.
- **Algorithms** — implementations of common evolutionary algorithms, such as a
  simple genetic algorithm (EA), evolution strategies (ES), and others.

## Examples

This repository contains examples of using DEAP for function optimization —
[`genetic_algorithm_1.ipynb`](genetic_algorithm_1.ipynb) and
[`genetic_algorithm_2.ipynb`](genetic_algorithm_2.ipynb). Walk through the notebooks to
see the principles above applied in practice.
