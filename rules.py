"""
This file contains the information for the rules that govern how points
are earned for the credit card purchases. To add/remove/change any rules,
just changing the rules attribute should be sufficient for the program to
adapt accordingly.

For the brute force implementation, the class also has a generic apply rule function
to be called when a rule is satisfied in a month.
"""
class RuleSet:
    """
    The rules for the credit card's rewards system.
    Rules are contained in a list of a specified format. For example, "Rule 1: 500 points for every
    $75 spend at Sport Check, $25 spend at Tim Hortons and $25 spend at Subway" would be
    represented as: (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}).

    Instance Attributes:
      - rules: list containing all rewards rules of the format (points, {merchant: dollars needed})
      - apply_rule: returns the points earned from applying a rule to a given monthly spending

    Representation Invariants:
        - rules[0][1].keys() == {"remainder"}
    """
    rules = [
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75}),
        (150, {"sportcheck": 25, "tim_hortons": 10, "subway": 10}),
        (75, {"sportcheck": 25, "tim_hortons": 10}),
        (75, {"sportcheck": 20})
    ]


    def apply_rule(self, spendings: dict, rule: int, mult: int=1) -> tuple[int, dict]:
        """Applies a rewards rule to a given monthly spendings. Only used for the brute
        force implementation.

        Args:
            - spendings: dictionary containing total monthly spendings at merchants in a month
            - rule: which rules to be applied to spendings
            - mult: how many times to apply given rule to spendings
 
        Returns:
            - (points, remaining_spendings): tuple containg points earned and remaning money to
                                           calculate

        >>> monthly_spendings = {"sportcheck": 75, "tim_hortons": 25, "subway": 25}
        >>> print(RuleSet().apply_rule(monthly_spendings, 1, 1))
        (500, {'sportcheck': 0, 'tim_hortons': 0, 'subway': 0})
        """
        if rule == 0: # rule 0 is for leftover amounts
            points = sum(spendings.values())
            # return a copy of no more spendings left at merchants
            remaining_money = spendings.copy()
            for shop in remaining_money:
                remaining_money[shop] = 0
            return (points, remaining_money)
        else:
            rule_to_apply = self.rules[rule] # get rule's values
            points = rule_to_apply[0] * mult
            remaining_money = spendings.copy()
            # deduct the dollar amounts from total monthly spending
            for debit in rule_to_apply[1]:
                remaining_money[debit] = remaining_money[debit] - (rule_to_apply[1][debit] * mult)
            return (points, remaining_money)