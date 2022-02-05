from ast import expr
from ortools.linear_solver import pywraplp

def find_defined_merchants(rules: list, monthly: dict) -> dict:
    merchants = {}
    for rule in rules:
        for merchant in rule[1].keys():
            if merchant in monthly.keys():
                if merchant not in merchants:
                    merchants[merchant] = ""
    return merchants

def rule_applicable(rule: dict, monthly: dict) -> bool:
    app = True
    for shop in rule.keys():
        if shop not in monthly.keys():
            app = False
    return app

def generate_constraints(rules: list, monthly: dict) -> tuple:
    exprs = find_defined_merchants(rules, monthly)
    valid_rules = set()
    for i in range(1, len(rules)):
        for shop in exprs.keys():
            if rule_applicable(rules[i][1], monthly):
                if shop in rules[i][1]:
                    valid_rules.add(i)
                    if exprs[shop] == "":
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
    
    other = 0
    for shop in monthly.keys():
        if shop not in exprs.keys():
            other += monthly[shop]
    remainder = remainder + f" + {other}"

    exprs["remainder"] = remainder
   
    return (exprs, valid_rules)

def gen_maximizer_expr(rules: list, valid_rules: set) -> str:
    max = ""
    for i in valid_rules:
        if max == "":
            max = max + f"x[{i}]*{rules[i][0]}"
        else:
            max = max + f" + x[{i}]*{rules[i][0]}"
    max = max + f" + x[{len(rules)}]*{rules[0][0]}"
    
    return max

def dynamic_lpp_points_calc(rules: list, monthly: dict) -> None:
    solver = pywraplp.Solver.CreateSolver('CBC')
    x = [0]

    for i in range(1, len(rules) + 1):
        x.append(solver.IntVar(0, solver.infinity(), f"x{i}"))

    generated = generate_constraints(rules, monthly)
    constraints, valids = generated[0], generated[1]

    for expr in constraints.values():
        solver.Add(eval(expr))

    max = gen_maximizer_expr(rules, valids)

    solver.Maximize(eval(max))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Total points =', int(solver.Objective().Value()))
        for i in range(1, len(rules) + 1):
            print(f"Rule {i}: {int(x[i].solution_value())} times")
    else:
        print('The problem does not have an optimal solution.')
    
# dynamic_lpp_points_calc([
#         (1, {"remainder": 1}),
#         (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
#         (300, {"sportcheck": 75, "tim_hortons": 25}),
#         (200, {"sportcheck": 75}),
#         (150, {"sportcheck": 25, "tim_hortons": 10, "subway": 10}),
#         (75, {"sportcheck": 25, "tim_hortons": 10}),
#         (75, {"sportcheck": 20})
#     ], {"sportcheck": 25, "tim_hortons": 10, "the_bay": 5})