from ortools.linear_solver import pywraplp

def find_defined_merchants(rules: list) -> dict:
    merchants = {}
    for rule in rules:
        for merchant in rule[1].keys():
            if merchant not in merchants:
                merchants[merchant] = ""
    merchants.pop("remaining")
    return merchants

def generate_constraints(rules: list) -> tuple[dict, dict]:
    exprs = find_defined_merchants(rules)
    equations = exprs.copy()
    for i in range(1, len(rules)):
        for shop in exprs.keys():
            if shop in rules[i][1]:
                if i == 1:
                    exprs[shop] = exprs[shop] + f"{rules[i][1][shop]}*x[{i}]"
                    equations[shop] = equations[shop] + f"{rules[i][1][shop]}*x[{i}].solution_value()"
                else:
                    exprs[shop] = exprs[shop] + f" + {rules[i][1][shop]}*x[{i}]"
                    equations[shop] = equations[shop] + f" + {rules[i][1][shop]}*x[{i}].solution_value()"
    
    for shop in exprs.keys():
        exprs[shop] = exprs[shop] + f" <= {monthly[shop]}"

    return (exprs, equations)

def gen_maximizer_expr(rules: list) -> str:
    max = ""
    for i in range(1, len(rules)):
        if i == 1:
            max = max + f"x[{i}]*{rules[i][0]}"
        else:
            max = max + f" + x[{i}]*{rules[i][0]}"
    return max

def dynamic_lpp_points_calc(rules: list, monthly: dict) -> None:
    solver = pywraplp.Solver.CreateSolver('SCIP')
    x = [0]

    for i in range(1, len(rules)):
        x.append(solver.IntVar(0, solver.infinity(), f"x{i}"))

    maths_rules = generate_constraints(rules)
    constraints, points_eqs = maths_rules[0], maths_rules[1]
    
    other = 0
    for shop in monthly.keys():
        if shop not in constraints.keys():
            other += monthly[shop]

    for expr in constraints.values():
        solver.Add(eval(expr))

    max = gen_maximizer_expr(rules)

    solver.Maximize(eval(max))

    status = solver.Solve()

    for shop in points_eqs.keys():
        x[0] += monthly[shop] - eval(f"{points_eqs[shop]}")

    x[0] += other

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Total points =', solver.Objective().Value() + x[0])
        for i in range(1, 7):
            print(f"Rule {i}: {int(x[i].solution_value())} times")
        print(f"Rule 7: {int(x[0])} times")
    else:
        print('The problem does not have an optimal solution.')