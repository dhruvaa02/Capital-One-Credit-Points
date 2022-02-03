from rules import RuleSet
from itertools import permutations

def reduced_bf(spendings: dict) -> int:
    points = 0
    valid_rules = get_valid_rules(spendings)
    return points

def get_valid_rules(spendings: dict) -> list:
    valid_rules = []
    for rule in RuleSet().rules[1:]:
        valid = True
        for shop in rule[1].keys():
            if shop not in spendings.keys():
                valid = False
            elif spendings[shop] < rule[1][shop]:
                valid = False
        if valid:
            valid_rules.append(rule)
    return valid_rules

# print(get_valid_rules({"sport_chek": 75, "subway": 25}))

# rules = [1, 2, 3, 4, 5]
# print(list(permutations(rules)))