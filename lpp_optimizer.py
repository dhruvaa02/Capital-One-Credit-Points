"""
This file contains my initial linear programming implementation to learn about Google's OR
tools as well as test if my equations were correct/working. This file exists as a way of testing
hard coded values to understand how the LPP tool works/calculates. This file is not actually
used anywhere since the rule creation has been made dynamic.

My actual program takes this fundamental usage, and dynamically generates the rules,
constraints, maximization function etc. from the rules list and transactions file.

This implementation uses applied linear programming to use the SCIP algorithm to determine
the coefficients that lead to the maximum number of points.
"""
from ortools.linear_solver import pywraplp # google OR-tools

def lpp_solver():
    # initalise LPP solver
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # add the coefficients to be solved for to solver
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')
    x3 = solver.IntVar(0, solver.infinity(), 'x3')
    x4 = solver.IntVar(0, solver.infinity(), 'x4')
    x5 = solver.IntVar(0, solver.infinity(), 'x5')
    x6 = solver.IntVar(0, solver.infinity(), 'x6')
    x7 = solver.IntVar(0, solver.infinity(), 'x7')

    # hard coded spending values for testing/understanding
    sportcheck = 370
    tims = 71
    sub = 39
    other = 0

    # add the constraints, the math can be explained in the readme/by me or by searching
    # up the SCIP algorithm

    # the totals of all the deductions cannot exceed spendings at merchant that month
    solver.Add(75*x1 + 75*x2 + 75*x3 + 25*x4 + 25*x5 + 20*x6 <= sportcheck)
    solver.Add(25*x1 + 25*x2 + 10*x4 + 10*x5 <= tims)
    solver.Add(25*x1 + 10*x4 <= sub)

    # calculate the leftover amounts as well as merchants not in rules
    solver.Add(x7 <= (sportcheck - (75*x1 + 75*x2 + 75*x3 + 25*x4 + 25*x5 + 20*x6)) + (tims 
    - (25*x1 + 25*x2 + 10*x4 + 10*x5)) + (sub - (25*x1 + 10*x4)))

    # the maximization function, solver tries to find maximum points
    solver.Maximize(x1*500 + x2*300 + x3*200 + x4*150 + x5*75 + x6*75 + x7)

    # solve matrix and return if succesful and if so, how optimal
    status = solver.Solve()

    # print solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('x1 =', x1.solution_value())
        print('x2 =', x2.solution_value())
        print('x3 =', x3.solution_value())
        print('x4 =', x4.solution_value())
        print('x5 =', x5.solution_value())
        print('x6 =', x6.solution_value())
        print('x7 =', x7.solution_value())
    else:
        print('The problem does not have an optimal solution.')
    
    return solver