from ortools.linear_solver import pywraplp

def find_defined_merchants(rules: list) -> dict:
    merchants = {}
    for rule in rules:
        for merchant in rule[1].keys():
            if merchant not in merchants:
                merchants[merchant] = ""
    merchants.pop("remaining")
    return merchants

rules = [
        (1, {"remaining": 1}),
        (500, {"sport_chek": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sport_chek": 75, "tim_hortons": 25}),
        (200, {"sport_chek": 75}),
        (150, {"sport_chek": 25, "tim_hortons": 10, "subway": 10}),
        (75, {"sport_chek": 25, "tim_hortons": 10}),
        (75, {"sport_chek": 20})
    ]

monthly = {"sport_chek": 25, "tim_hortons": 10, "subway": 0, "the_bay": 5}

solver = pywraplp.Solver.CreateSolver('SCIP')

x = [0]

exprs = find_defined_merchants(rules)

for i in range(1, len(rules)):
    x.append(solver.IntVar(0, solver.infinity(), f"x{i}"))
    for shop in exprs.keys():
        if shop in rules[i][1]:
            if i == 1:
                exprs[shop] = exprs[shop] + f"{rules[i][1][shop]}*x[{i}]"
            else:
                exprs[shop] = exprs[shop] + f" + {rules[i][1][shop]}*x[{i}]"

for shop in exprs.keys():
    exprs[shop] = exprs[shop] + f" <= {monthly[shop]}"

other = 0
for shop in monthly.keys():
    if shop not in exprs.keys():
        other += monthly[shop]

for expr in exprs.values():
    solver.Add(eval(expr))

solver.Maximize(eval("x[1]*500 + x[2]*300 + x[3]*200 + x[4]*150 + x[5]*75 + x[6]*75"))

status = solver.Solve()

x[0] = sum([monthly['sport_chek'] - (75*x[1].solution_value() + 75*x[2].solution_value() + 75*x[3].solution_value() + 25*x[4].solution_value() + 25*x[5].solution_value() + 20*x[6].solution_value()), monthly['tim_hortons'] - (25*x[1].solution_value() + 25*x[2].solution_value() + 10*x[4].solution_value() + 10*x[5].solution_value()), monthly['subway'] - (25*x[1].solution_value() + 10*x[4].solution_value()), other])

if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value() + x[0])
    for i in range(1, 7):
        print(f"Rule {i}: {x[i].solution_value()} times")
    print(f"Rule 7: {x[0]} times")
else:
    print('The problem does not have an optimal solution.')