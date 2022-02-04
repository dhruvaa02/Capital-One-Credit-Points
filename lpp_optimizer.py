
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

x1 = solver.IntVar(0, solver.infinity(), 'x1')
x2 = solver.IntVar(0, solver.infinity(), 'x2')
x3 = solver.IntVar(0, solver.infinity(), 'x3')
x4 = solver.IntVar(0, solver.infinity(), 'x4')
x5 = solver.IntVar(0, solver.infinity(), 'x5')
x6 = solver.IntVar(0, solver.infinity(), 'x6')

sport = 25
tims = 10
sub = 0
other = 0

solver.Add(75*x1 + 75*x2 + 75*x3 + 25*x4 + 25*x5 + 20*x6 <= sport)
solver.Add(25*x1 + 25*x2 + 10*x4 + 10*x5 <= tims)
solver.Add(25*x1 + 10*x4 <= sub)

solver.Maximize(x1*500 + x2*300 + x3*200 + x4*150 + x5*75 + x6*75)

status = solver.Solve()

x7 = sum([sport - (75*x1.solution_value() + 75*x2.solution_value() + 75*x3.solution_value() + 25*x4.solution_value() + 25*x5.solution_value() + 20*x6.solution_value()), tims - (25*x1.solution_value() + 25*x2.solution_value() + 10*x4.solution_value() + 10*x5.solution_value()), sub - (25*x1.solution_value() + 10*x4.solution_value()), other])

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value() + x7)
    print('x1 =', x1.solution_value())
    print('x2 =', x2.solution_value())
    print('x3 =', x3.solution_value())
    print('x4 =', x4.solution_value())
    print('x5 =', x5.solution_value())
    print('x6 =', x6.solution_value())
    print('x7 =', x7)
else:
    print('The problem does not have an optimal solution.')