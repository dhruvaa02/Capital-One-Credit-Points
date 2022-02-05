from monthly import get_monthly_spendings
from dynamic_lpp import dynamic_lpp_points_calc
from rules import RuleSet

if __name__ == "__main__":
    monthly = get_monthly_spendings("transactions.json")
    dynamic_lpp_points_calc(RuleSet.rules, monthly)