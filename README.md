# Genetic Algorithm with Differential Evolution  

## Motivation
The Genetic Algorithm with Differential Evolution (GA/DE) is an technique based on Genetic Algorithm (GA) 
for solving optimization problems. This version GA algorithms follows the same principle, Selection, Crossover and Mutation. 
However, in order to solve the optimization problem effectively, it uses different approaches 
for Mutation and Crossover steps as follows:
<img align="right" height="180" src="https://cdn4.iconfinder.com/data/icons/types-of-science-glyph/512/dna_science_genetic_gene_cell_biology-256.png">

##### Crossover:
The crossover is applied, for each dimension of an individual, weather the Crossover Probability Rate is greater than a 
random number or its ith position is equals to a random number multiplied by its ith position, i.e., 
this step is directly dependent to CPR.

##### Mutation:
The mutation can be ignored for GA/DE since the DE is applied to all the population and its mechanism is good enough 
to get way from minimal points. However, for this solution, we chose to apply a random number following the standard
distribution as a perturbation information in order to find feasible solutions in the neighborhood.   



``` python
from de_GA.run import run
```

## About


## Documentation
