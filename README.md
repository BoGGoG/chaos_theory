# Chaos Theory
This is an easy python program for showing how the logistic map leads to chaos.

## Sources
- https://en.wikipedia.org/wiki/Logistic_map
- http://code.activestate.com/recipes/577332-bifurcation-diagram-of-logistic-map/

## Theory
The logistic map
$$ x_{n+1} = r x_n(1 - x_n) $$
Describes a population of relative size $x_n$ (relativ to the maximal size). 
The population at time step $n+1$ only depends on the reproduction/starvation parameter $r$ and the previous population $x_{n}$.
Reproduction and starvation are at a constant fight and the parameter $r$
represents this. 

Depending on $r$ we get different population sizes for late times, see (Wiki)[https://en.wikipedia.org/wiki/Logistic_map]
