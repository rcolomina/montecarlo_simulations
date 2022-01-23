# Monte Carlo Simulations 

This project aim is to create templates to apply MC to any type of problem. 

This project contains simple examples applied to calculate areas on on geometric problems.

The kernel of this project is a random number generator (RNG) that is inicialised with a constant seed, in order to make it testeable i.e. fix number given to the RNG allowing to produce repeatable experiments. The tradition is to use 42 to wink the film "The Hitchhiker's guide to the Galaxy". 

## Random Number Generator

In order to apply MC, a good random number generator is requried to create samples.

## Monte Carlo Method (MC)

The mathematical foundations of MC are in the law of big numbers. 

MC calculates expected values of random variables.  

## Geometric Area Calculations

As example, here is show how to calculate the area of a surface. Starting with a square of side L, we draw from each square's vertex, quarter of circumference having radius L. The four quarters of circumferences intersects into a central area A. This will be calculated with MC.

The exact solution is `A = (1/6) * L^2 * ( 6 * SQRT(3) - 2 PI + 6 )` so it is used as MC testing

## Geometric Brownian Motion
TBC
## Neural Network Parameter Selection
TBC
## Convergence Analysis
TBC



