from ortools.linear_solver import pywraplp

def find_defined_merchants(rules: list) -> dict:
    merchants = {}
    for rule in rules:
        for merchant in rule[1].keys():
            if merchant not in merchants:
                merchants[merchant] = ""
    merchants.pop("remaining")
    return merchants

def generate_constraints(rules: list, monthly: dict) -> dict:
    exprs = find_defined_merchants(rules)
    for i in range(1, len(rules)):
        for shop in exprs.keys():
            if shop in rules[i][1]:
                if i == 1:
                    exprs[shop] = exprs[shop] + f"{rules[i][1][shop]}*x[{i}]"
                else:
                    exprs[shop] = exprs[shop] + f" + {rules[i][1][shop]}*x[{i}]"
    remainder = ""
    for equation in exprs.keys():
        if remainder == "":
            remainder = remainder + f"x[{len(rules)}] <= ({monthly[equation]} - ({exprs[equation]}))"
        else:
            remainder = remainder + f" + ({monthly[equation]} - ({exprs[equation]}))"
        exprs[equation] = exprs[equation] + f" <= {monthly[equation]}"
    exprs["remainder"] = remainder
    return exprs

def gen_maximizer_expr(rules: list) -> str:
    max = ""
    for i in range(1, len(rules)):
        if i == 1:
            max = max + f"x[{i}]*{rules[i][0]}"
        else:
            max = max + f" + x[{i}]*{rules[i][0]}"
    max = max + f" + x[{len(rules)}]"
    return max

def dynamic_lpp_points_calc(rules: list, monthly: dict) -> None:
    solver = pywraplp.Solver.CreateSolver('CBC')
    x = [0]

    for i in range(1, len(rules) + 1):
        x.append(solver.IntVar(0, solver.infinity(), f"x{i}"))

    constraints = generate_constraints(rules, monthly)
    
    other = 0
    for shop in monthly.keys():
        if shop not in constraints.keys():
            other += monthly[shop]

    for expr in constraints.values():
        solver.Add(eval(expr))

    max = gen_maximizer_expr(rules)

    solver.Maximize(eval(max))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Total points =', int(solver.Objective().Value()))
        for i in range(1, len(rules) + 1):
            print(f"Rule {i}: {int(x[i].solution_value())} times")
    else:
        print('The problem does not have an optimal solution.')