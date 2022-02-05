"""
This file contains all the unit testing for the entire program, every part even if unused (i.e. the 
hard coded lpp optimizer). Should return 13 passed tests.
"""
import unittest
import rules
from brute_force import get_valid_rules, reduced_bf
from data import get_monthly_spendings
from lpp_optimizer import lpp_solver
from dynamic_lpp import *

class TestMonthly(unittest.TestCase):
    """
    Unit test class for testing the functionality in the data.py file
    """
    file_to_read = get_monthly_spendings('test_transactions.json')

    def test_file_reading(self) -> None:
        """
        Tests whether the file reading was implemented correctly for transactions reading
        """
        self.assertEquals(self.file_to_read.keys(), {"sportcheck", "tim_hortons", "subway"})
    
    def test_monthly_summation(self) -> None:
        """
        Tests whether the monthly spending values being calculated is being summed correctly
        """
        self.assertEquals(self.file_to_read["sportcheck"], 370)
        self.assertEquals(self.file_to_read["tim_hortons"], 71)
        self.assertEquals(self.file_to_read["subway"], 39)


class TestRules(unittest.TestCase):
    """
    Unit test class for testng the functionality in the rules.py file
    """
    rules_to_test = rules.RuleSet()

    def test_first_rule_remainder(self) -> None:
        """
        Tests whether the first rule in the rules list is for remainder values as specified 
        in documentation.
        """
        self.assertEquals(self.rules_to_test.rules[0][1].keys(), {"remainder"})
    
    def test_rules_format(self) -> None:
        """
        Tests whether the rules have been given in the appropriate format for the program.
        """
        for rule in self.rules_to_test.rules:
            self.assertIsInstance(rule, tuple)
            self.assertIsInstance(rule[0], int)
            self.assertIsInstance(rule[1], dict)
    
    def test_apply_rule(self) -> None:
        """
        Tests whether the a rule is being applied to spendings correctly for the brute force
        implementation.
        """
        test_spendings = {"sportcheck": 1000, "subway": 500, "tim_hortons": 800, "the_bay": 200}
        rule_applied = self.rules_to_test.apply_rule(test_spendings, 1, 2)
        self.assertEquals(rule_applied[0], 1000)
        self.assertEquals(rule_applied[1], {'sportcheck': 850, 'subway': 450, 
        'tim_hortons': 750, 'the_bay': 200})


class TestBruteForce(unittest.TestCase):
    """
    Unit test class for testing the functionality in the brute_force.py file.
    """   
    def test_get_valid_rules(self) -> None:
        """
        Tests whether the valid rules calcualted are actually applicable.
        """
        self.assertEquals(get_valid_rules({"sportcheck": 210}), [3, 6])
    
    def test_brute_force(self) -> None:
        """
        Tests whether the brute force algorithm implemented returns correct maximum points.
        """
        self.assertEquals(reduced_bf({"sportcheck": 210}), (760, (6, 3), [10, 0]))


class TestLPPOptimizer(unittest.TestCase):
    """
    Unit test class for testing the functionality in the lpp_optimizer.py file.
    """ 
    solver_to_test = lpp_solver()

    def test_solver(self) -> None:
        """
        Tests whether the Google OR-tools library was implemented correctly for one specific
        hard coded scenario.
        """ 
        self.assertEquals(int(self.solver_to_test.Objective().Value()), 1675)


class TestDynamicLPP(unittest.TestCase):
    """
    Unit test class for testing the functionality in the dynamic_lpp.py file.
    """ 
    solver_to_test = dynamic_lpp_points_calc([(1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 500, "tim_hortons": 500})

    def test_find_defined_merchants(self) -> None:
        """
        Tests whether the merchants specified in both the rules and monthly spendings
        are correctly being identified.
        """ 
        relevant = {"tim_hortons": "", "sportcheck": ""}

        self.assertEquals(find_defined_merchants([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 500, "tim_hortons": 500}), relevant)

    def test_rule_applicable(self) -> None:
        """
        Tests whether the function correctly identifies if a rule is applicable for a given
        monthly spendings.
        """ 
        rule = {"sportcheck": 75, "tim_hortons": 25, "subway": 25}

        self.assertFalse(rule_applicable(rule, {"sportcheck": 500, "the_bay": 900}))
        self.assertTrue(rule_applicable(rule, {"sportcheck": 500, "tim_hortons": 900, "subway": 500}))
    
    def test_generate_constraints(self) -> None:
        """
        Tests whether the function correctly generates the correct mathematical constraints necessary
        for the LPP solver.
        """ 
        constraints_to_test = generate_constraints([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 500, "tim_hortons": 500})

        self.assertEquals(constraints_to_test[0]["sportcheck"], "75*x[2] + 75*x[3] <= 500")
        self.assertEquals(constraints_to_test[0]["remainder"], "x[4] <= (500 - (75*x[2] + 75*x[3])) + (500 - (25*x[2])) + 0")

    def test_generate_maximizer(self) -> None:
        """
        Tests whether the function correctly generates the maximizer equation needed for the LPP
        solver i.e. the equation specifying total points earned.
        """ 
        valid_rules = set()
        valid_rules.add(2)
        valid_rules.add(3)

        maximizer_to_test = gen_maximizer_expr([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], valid_rules)

        self.assertEquals(maximizer_to_test, "x[2]*300 + x[3]*200 + x[4]*1")

    def test_dynamic_lpp_solver(self) -> None:
        """
        Tests whether the dynamic LPP solver correctly identifies the maximum number of points
        as needed by the program.
        """ 
        maximizer_to_test = dynamic_lpp_points_calc([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 1000, "the_bay": 5000})

        self.assertEquals(int(maximizer_to_test.Objective().Value()), 7625)


if __name__ == '__main__':
    unittest.main()