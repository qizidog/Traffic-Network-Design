# Traffic-Network-Design
The assignment of a transportation course for my first year as a graduate student, solved the bilevel programming problem using GA algorithm and T-F algorithm.

# Quote
The main repositories used in this assignment are as follows, 
- [GeneticAlgorithmsWithPython](https://github.com/handcraftsman/GeneticAlgorithmsWithPython) is used to solve the Traffic assignment problem ——  solve User Equilibrium using F-W algorithm 
- [geatpy](https://github.com/geatpy-dev/geatpy) is used to calculate the optimal value of the upper objective function

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
For more information, please refer to the repositories I cited above. There are few changes to the code.  
Just one more thing, the following sentence may report errors, because I want to see the current generation and changed some codes in package geatpy.
```python
myAlgorithm.showCurGen = True
```
You can just Comment it or modify the file `soea_DE_rand_1_bin_templet.py` in geatpy package to print the generation information.  
The path of `soea_DE_rand_1_bin_templet.py` should be `site-packages\geatpy\templates\soeas\DE\DE_rand_1_bin`  
The file I have changed is pushed into this repository as well, you can replace the it with original file.
