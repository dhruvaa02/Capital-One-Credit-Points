class RuleSet:

    rules = [
        (1, {"remaining": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75}),
        (150, {"sportcheck": 25, "tim_hortons": 10, "subway": 10}),
        (75, {"sportcheck": 25, "tim_hortons": 10}),
        (75, {"sportcheck": 20})
    ]

    def apply_rule(self, spendings: dict, rule: int, mult: int=1) -> tuple[int, dict]:
        if rule == 0:
            points = sum(spendings.values())
            remaining_money = spendings.copy()
            for shop in remaining_money:
                remaining_money[shop] = 0
            return (points, remaining_money)
        else:
            rule_to_apply = self.rules[rule]
            points = rule_to_apply[0] * mult
            remaining_money = spendings.copy()
            for debit in rule_to_apply[1]:
                remaining_money[debit] = remaining_money[debit] - (rule_to_apply[1][debit] * mult)
            return (points, remaining_money)