from rules import RuleSet
from itertools import permutations

def reduced_bf(spendings: dict) -> int:
    points = 0
    valid_rules = get_valid_rules(spendings)
    permutes = list(permutations(valid_rules))
    print(permutes)
    return points

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

print(reduced_bf({"sport_chek": 75, "subway": 25}))

# rules = [1, 2, 3, 4, 5]
# print(list(permutations(rules)))