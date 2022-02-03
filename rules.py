class RuleSet:

    rules = [
        (1, {"remaining": 1}),
        (500, {"sport_chek": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sport_chek": 75, "tim_hortons": 25}),
        (200, {"sport_chek": 75}),
        (150, {"sport_chek": 25, "tim_hortons": 10, "subway": 10}),
        (75, {"sport_chek": 25, "tim_hortons": 10}),
        (75, {"sport_chek": 20})
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

print(RuleSet().apply_rule({"sport_chek": 75, "tim_hortons": 25, "subway": 25}, 0, 2))
# class Rules:

#     definition: tuple[int, dict] = None

#     def apply_rule(self, spendings: dict, mult: int=1) -> tuple[int, dict]:
#         points = self.definition[0] * mult
#         remaining_money = spendings.copy()
#         for debit in self.definition[1]:
#             remaining_money[debit] = remaining_money[debit] - (self.definition[1][debit] * mult)
#         return (points, remaining_money)

# class Rule1(Rules):

#     definition = (500, {"sport_chek": 75, "tim_hortons": 25, "subway": 25})


# class Rule2(Rules):

#     definition = (300, {"sport_chek": 75, "tim_hortons": 25})


# class Rule3(Rules):

#     definition = (200, {"sport_chek": 75})


# class Rule4(Rules):

#     definition = (150, {"sport_chek": 25, "tim_hortons": 10, "subway": 10})


# class Rule5(Rules):

#     definition = (75, {"sport_chek": 25, "tim_hortons": 10})


# class Rule6(Rules):

#     definition = (75, {"sport_chek": 20})


# class Rule7(Rules):

#     definition = (1, {"sport_chek": 25, "tim_hortons": 10, "subway": 10})

#     def apply_rule(self, spendings: dict, mult: int = 1) -> tuple[int, dict]:
#         points = sum(spendings.values())
#         remaining_money = spendings.copy()
#         for shop in remaining_money:
#             remaining_money[shop] = 0
#         return (points, remaining_money)