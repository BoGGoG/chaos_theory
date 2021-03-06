<!--using this web service-->
<!--https://www.codecogs.com/latex/eqneditor.php-->
<!--to make latex equations-->
# Chaos Theory
This is an easy python program for showing how the logistic map leads to chaos.

## Sources
- https://en.wikipedia.org/wiki/Logistic_map
- http://code.activestate.com/recipes/577332-bifurcation-diagram-of-logistic-map/
- https://www.codecogs.com/latex/eqneditor.php for <a href="https://www.codecogs.com/eqnedit.php?latex=\LaTeX{}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\LaTeX{}" title="\LaTeX{}" /></a> equations in the Readme

## Theory
The logistic map

<a href="https://www.codecogs.com/eqnedit.php?latex=$$&space;x_{n&plus;1}&space;=&space;r&space;x_n(1&space;-&space;x_n)&space;$$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$$&space;x_{n&plus;1}&space;=&space;r&space;x_n(1&space;-&space;x_n)&space;$$" title="$$ x_{n+1} = r x_n(1 - x_n) $$" /></a>

describes a population of relative size <a href="https://www.codecogs.com/eqnedit.php?latex=$x_n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$x_n$" title="$x_n$" /></a> (relativ to the maximal size). 
The population at time step <a href="https://www.codecogs.com/eqnedit.php?latex=$x_{n+1}$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$x_{n+1}$" title="$x_n$" /></a> only depends on the reproduction/starvation parameter r and the previous population <a href="https://www.codecogs.com/eqnedit.php?latex=$x_n$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$x_n$" title="$x_n$" /></a>.
Reproduction and starvation are at a constant fight and the parameter r represents this. 

Depending on r we get different population sizes for late times, see (Wiki)[https://en.wikipedia.org/wiki/Logistic_map]
