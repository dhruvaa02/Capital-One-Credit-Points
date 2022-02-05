"""
Main program for the Summer 2022 Capital One Credit Card Reward Points program 
technical challenge.

This file runs the etire program. Here, you can specify the name of the
file of a given user's transactions, as long as it is in JSON format.

The program then calculates the total spendings of the user at each
store during in the month and proceeds to calculate the maximum rewards
points possible. 

TO_NOTE: As soon as the transactions are read from the file,
everything in the program is dealt with in dollar amounts, NOT in cents.
Also, this program is running my dynamic linear programming implementation
of the solution, not the brute force algorithm or the hard coded LPP code.

The maximum points possible to be earned along with which rules were applied
and how many times they were applied are printed in this format if
successful:
>>>
Solution:
Total points = 1675
Rule 1: 1 times
Rule 2: 0 times
Rule 3: 0 times
Rule 4: 1 times
Rule 5: 0 times
Rule 6: 13 times
Rule 7: 50 times
"""
from data import get_monthly_spendings
from dynamic_lpp import dynamic_lpp_points_calc
from rules import RuleSet

if __name__ == "__main__":
    monthly = get_monthly_spendings("transactions.json")
    dynamic_lpp_points_calc(RuleSet.rules, monthly)