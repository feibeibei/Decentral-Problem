# Decentral-Problem
Write an algorithm that can solve for x1, x2, x3, x4 in the section for "A Political Problem" in Chapter 29 of CLRS: https://docs.google.com/document/d/15627hDCFx3bUSUp6zW93vQHeljnrUftwARNaFELycg8/

## Dependency
The latest version of scipy.optimize.linprog (SciPy v1.10.0).

## Explanation
This linear programming problem requires solving a multi-variant inequality question, which could be solved using library scipy.optimize.linprog in python.
To be more specific, we set a matrix representing coefficients of the left hand side of the inequalities and another matrix representing coefficients of the right hand side of the inequalities. We switch all signs for coefficients in two matrixes since we want the value choice of x1, x2, x3, and x4 have the minimum sum while fulfilling these inequalities. Then we set bound to our final solutions x1, x2, x3, and x4 such that they are larger than 0. Finally, we calculate the solution using scipy.optimize.linprog function while specifying integrality to guarantee an integer solution.

