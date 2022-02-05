"""
This file contains my initial brute force implementation of the rewards points system.
The algorithm isn't completely brute force as some simplifcations/improvements were added
however it is still relatively dynamic, albeit theoretically slow.
"""
from rules import RuleSet
from itertools import permutations

def reduced_bf(spendings: dict) -> tuple:
    """Returns a tuple containing maximum rewards points possible, perumation of ruled
    applied to reach this maximum value as well as how many times each rule was applied.

    Args:
        - spendings: dictionary containing total monthly spendings at merchants in a month

    Returns:
        - points_from_permute: tuple of (maximum points, rule order applied for points,
                                         number of times rule[n] was applied from perumatation)

    >>> print(reduced_bf({"sportcheck": 210}))
    [3, 6]
    """
    valid_rules = get_valid_rules(spendings)
    permutes = list(permutations(valid_rules)) # generate all permutations of applicable rules
    points_from_permutes = [] # keep track of points from each permutation
    for permute in permutes:
        points = 0
        spendings_to_try = spendings.copy()
        times = [] # keep track of how many times the rules in order are applied
        for i in permute:
            rule = RuleSet().rules[i]
            # can only apply a rule as the minimum value in spendings divided by maximum dollar value in rule
            times_to_app = min([spendings_to_try[debit] // rule[1][debit] for debit in rule[1].keys()])
            times.append(times_to_app)
            applied = RuleSet().apply_rule(spendings_to_try, i, times_to_app)
            points += applied[0]
            spendings_to_try = applied[1]
        points += RuleSet().apply_rule(spendings_to_try, 0)[0]
        points_from_permutes.append((points, permute, times))
    return max(points_from_permutes)


def get_valid_rules(spendings: dict) -> list:
    """Returns a list of all applicable rules for given monthly spendings.

    Args:
        - spendings: dictionary containing total monthly spendings at merchants in a month

    Returns:
        - valid_rules: list containing the tuples of all valid rules

    >>> print(get_valid_rules({"sportcheck": 210}))
    [3, 6]
    """
    total_rules = RuleSet().rules
    valid_rules = []
    for i in range(1, len(total_rules)):
        valid = True
        for shop in total_rules[i][1].keys():
            if shop not in spendings.keys(): # check if store not even bought at
                valid = False
            elif spendings[shop] < total_rules[i][1][shop]: # check if spent necessary amount
                valid = False
        if valid:
            valid_rules.append(i)
    return valid_rules