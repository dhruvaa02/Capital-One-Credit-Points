from rules import RuleSet
from itertools import permutations

def reduced_bf(spendings: dict) -> tuple:
    valid_rules = get_valid_rules(spendings)
    permutes = list(permutations(valid_rules))
    points_from_permutes = []
    for permute in permutes:
        points = 0
        spendings_to_try = spendings.copy()
        for i in permute:
            rule = RuleSet().rules[i]
            times_to_app = min([spendings_to_try[debit] // rule[1][debit] for debit in rule[1].keys()])
            applied = RuleSet().apply_rule(spendings_to_try, i, times_to_app)
            points += applied[0]
            spendings_to_try = applied[1]
        points += RuleSet().apply_rule(spendings_to_try, 0)[0]
        points_from_permutes.append((points, permute))
    return max(points_from_permutes)

def get_valid_rules(spendings: dict) -> list:
    total_rules = RuleSet().rules
    valid_rules = []
    for i in range(1, len(total_rules)):
        valid = True
        for shop in total_rules[i][1].keys():
            if shop not in spendings.keys():
                valid = False
            elif spendings[shop] < total_rules[i][1][shop]:
                valid = False
        if valid:
            valid_rules.append(i)
    return valid_rules

print(reduced_bf({"sport_chek": 210}))

# rules = [1, 2, 3, 4, 5]
# print(list(permutations(rules)))