# Traffic-Network-Design
The assignment of a transportation course for my first year as a graduate student, solved the bilevel programming problem using GA algorithm and T-F algorithm.

# Quote
The main repositories used in this assignment are as follows, 
- [GeneticAlgorithmsWithPython](https://github.com/handcraftsman/GeneticAlgorithmsWithPython) is used to solve the Traffic assignment problem ——  solve User Equilibrium using F-W algorithm 
- [geatpy](https://github.com/geatpy-dev/geatpy) is used to calculate the optimal value of the upper objective function

The version of `geatpy` I use is updated as follow:

```bash
(base) [user@host Traffic-Network-Design (master ✗)]$ conda list geatpy
# packages in environment at /Users/user/miniforge3:
#
# Name                    Version                   Build  Channel
geatpy                    2.7.0                    pypi_0    pypi
```

# HOW TO USE
- Define your network information in class MyNetwork in `Myproblem.py` 
- Define the upper and lower bounds of the independent variable and the aimFunc in class MyProblem in `Myproblem.py` 
- Set the necessary parameters related to genetic algorithm in `main.py` such as NIND and myAlgorithm.MAXGEN
- Run the program 

```cmd
    python main.py
```

# More Info
As this is only a homework of my own, I don't want to spend too much time on this document.   
For more information, please refer to the repositories I cited above.
