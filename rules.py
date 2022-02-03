class Rules:
    def rule_1(spendings: dict, mult: int=1) -> tuple[int, dict]:
        points = 500 * mult
        remaining_money = spendings.copy()
        remaining_money["sportchek"] = spendings["sportchek"] - (75*mult)
        remaining_money["time_hortons"] = spendings["tim_hortons"] - (25*mult)
        remaining_money["subway"] = spendings["subway"] - (25*mult)
        return (points, remaining_money)
    
    def rule_2(spendings: dict, mult: int=1) -> tuple[int, dict]:
        points = 300 * mult
        remaining_money = spendings.copy()
        remaining_money["sportchek"] = spendings["sportchek"] - (75*mult)
        remaining_money["time_hortons"] = spendings["tim_hortons"] - (25*mult)
        return (points, remaining_money)

    def rule_3(spendings: dict, mult: int=1) -> tuple[int, dict]:
        points = 200 * mult
        remaining_money = spendings.copy()
        remaining_money["sportchek"] = spendings["sportchek"] - (75*mult)
        return (points, remaining_money)
    
    def rule_4(spendings: dict, mult: int=1) -> tuple[int, dict]:
        points = 150 * mult
        remaining_money = spendings.copy()
        remaining_money["sportchek"] = spendings["sportchek"] - (25*mult)
        remaining_money["time_hortons"] = spendings["tim_hortons"] - (10*mult)
        remaining_money["subway"] = spendings["subway"] - (10*mult)
        return (points, remaining_money)
    
    def rule_5(spendings: dict, mult: int=1) -> tuple[int, dict]:
        points = 75 * mult
        remaining_money = spendings.copy()
        remaining_money["sportchek"] = spendings["sportchek"] - (25*mult)
        remaining_money["time_hortons"] = spendings["tim_hortons"] - (10*mult)
        return (points, remaining_money)

    def rule_6(spendings: dict, mult: int=1) -> tuple[int, dict]:
        points = 75 * mult
        remaining_money = spendings.copy()
        remaining_money["sportchek"] = spendings["sportchek"] - (20*mult)
        return (points, remaining_money)
    
    def rule_7(spendings: dict) -> tuple[int, dict]:
        points = sum(spendings.values())
        remaining_money = spendings.copy()
        for shop in remaining_money:
            remaining_money[shop] = 0
        return (points, remaining_money)