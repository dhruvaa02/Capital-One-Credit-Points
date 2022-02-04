from ortools.linear_solver import pywraplp

rules = [
        (1, {"remaining": 1}),
        (500, {"sport_chek": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sport_chek": 75, "tim_hortons": 25}),
        (200, {"sport_chek": 75}),
        (150, {"sport_chek": 25, "tim_hortons": 10, "subway": 10}),
        (75, {"sport_chek": 25, "tim_hortons": 10}),
        (75, {"sport_chek": 20})
    ]

solver = pywraplp.Solver.CreateSolver('SCIP')

# x1 = solver.IntVar(0, solver.infinity(), 'x1')
# x2 = solver.IntVar(0, solver.infinity(), 'x2')
# x3 = solver.IntVar(0, solver.infinity(), 'x3')
# x4 = solver.IntVar(0, solver.infinity(), 'x4')
# x5 = solver.IntVar(0, solver.infinity(), 'x5')
# x6 = solver.IntVar(0, solver.infinity(), 'x6')
x = [0]

sports_expr = ""
tims_expr = ""
sub_expr = ""

for i in range(1, len(rules)):
    x.append(solver.IntVar(0, solver.infinity(), f"x{i}"))
    if "sport_chek" in rules[i][1]:
        if i == 1:
            sports_expr = sports_expr + f"{rules[i][1]['sport_chek']}*x[{i}]"

print(sports_expr)
print(tims_expr)
print(sub_expr)
sport = 2000
tims = 1469
sub = 890
other = 7328

solver.Add(eval("75*x[1] + 75*x[2] + 75*x[3] + 25*x[4] + 25*x[5] + 20*x[6] <= sport"))
solver.Add(eval("25*x[1] + 25*x[2] + 10*x[4] + 10*x[5] <= tims"))
solver.Add(eval("25*x[1] + 10*x[4] <= sub"))

solver.Maximize(eval("x[1]*500 + x[2]*300 + x[3]*200 + x[4]*150 + x[5]*75 + x[6]*75"))

status = solver.Solve()

x[0] = sum([sport - (75*x[1].solution_value() + 75*x[2].solution_value() + 75*x[3].solution_value() + 25*x[4].solution_value() + 25*x[5].solution_value() + 20*x[6].solution_value()), tims - (25*x[1].solution_value() + 25*x[2].solution_value() + 10*x[4].solution_value() + 10*x[5].solution_value()), sub - (25*x[1].solution_value() + 10*x[4].solution_value()), other])

# if status == pywraplp.Solver.OPTIMAL:
#     print('Solution:')
#     print('Objective value =', solver.Objective().Value() + x7)
#     print('x1 =', x1.solution_value())
#     print('x2 =', x2.solution_value())
#     print('x3 =', x3.solution_value())
#     print('x4 =', x4.solution_value())
#     print('x5 =', x5.solution_value())
#     print('x6 =', x6.solution_value())
#     print('x7 =', x7)
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value() + x[0])
    for i in range(1, 7):
        print(f"Rule {i}: {x[i].solution_value()} times")
    print(f"Rule 7: {x[0]} times")
else:
    print('The problem does not have an optimal solution.')