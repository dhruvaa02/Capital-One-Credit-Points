import unittest
import rules
from brute_force import get_valid_rules, reduced_bf
from data import get_monthly_spendings
from lpp_optimizer import lpp_solver
from dynamic_lpp import *

class TestMonthly(unittest.TestCase):

    file_to_read = get_monthly_spendings('test_transactions.json')

    def test_file_reading(self):
        self.assertEquals(self.file_to_read.keys(), {"sportcheck", "tim_hortons", "subway"})
    
    def test_monthly_summation(self):
        self.assertEquals(self.file_to_read["sportcheck"], 370)
        self.assertEquals(self.file_to_read["tim_hortons"], 71)
        self.assertEquals(self.file_to_read["subway"], 39)


class TestRules(unittest.TestCase):

    rules_to_test = rules.RuleSet()

    def test_first_rule_remainder(self):
        self.assertEquals(self.rules_to_test.rules[0][1].keys(), {"remainder"})
    
    def test_rules_format(self):
        for rule in self.rules_to_test.rules:
            self.assertIsInstance(rule, tuple)
            self.assertIsInstance(rule[0], int)
            self.assertIsInstance(rule[1], dict)
    
    def test_apply_rule(self):
        test_spendings = {"sportcheck": 1000, "subway": 500, "tim_hortons": 800, "the_bay": 200}
        rule_applied = self.rules_to_test.apply_rule(test_spendings, 1, 2)
        self.assertEquals(rule_applied[0], 1000)
        self.assertEquals(rule_applied[1], {'sportcheck': 850, 'subway': 450, 
        'tim_hortons': 750, 'the_bay': 200})


class TestBruteForce(unittest.TestCase):

    def test_brute_force(self):
        self.assertEquals(reduced_bf({"sportcheck": 210}), (760, (6, 3), [10, 0]))
    
    def test_get_valid_rules(self):
        self.assertEquals(get_valid_rules({"sportcheck": 210}), [3, 6])


class TestLPPOptimizer(unittest.TestCase):

    solver_to_test = lpp_solver()

    def test_solver(self):
        
        self.assertEquals(int(self.solver_to_test.Objective().Value()), 1675)


class TestDynamicLPP(unittest.TestCase):

    solver_to_test = dynamic_lpp_points_calc([(1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 500, "tim_hortons": 500})

    def test_find_defined_merchants(self):
        
        relevant = {"tim_hortons": "", "sportcheck": ""}

        self.assertEquals(find_defined_merchants([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 500, "tim_hortons": 500}), relevant)

    def test_rule_applicable(self):
        
        rule = {"sportcheck": 75, "tim_hortons": 25, "subway": 25}

        self.assertFalse(rule_applicable(rule, {"sportcheck": 500, "the_bay": 900}))
        self.assertTrue(rule_applicable(rule, {"sportcheck": 500, "tim_hortons": 900, "subway": 500}))
    
    def test_generate_constraints(self):
        
        constraints_to_test = generate_constraints([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 500, "tim_hortons": 500})

        self.assertEquals(constraints_to_test[0]["sportcheck"], "75*x[2] + 75*x[3] <= 500")
        self.assertEquals(constraints_to_test[0]["remainder"], "x[4] <= (500 - (75*x[2] + 75*x[3])) + (500 - (25*x[2])) + 0")

    def test_generate_maximizer(self):

        valid_rules = set()
        valid_rules.add(2)
        valid_rules.add(3)

        maximizer_to_test = gen_maximizer_expr([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], valid_rules)

        self.assertEquals(maximizer_to_test, "x[2]*300 + x[3]*200 + x[4]*1")

    def test_dynamic_lpp_solver(self):

        maximizer_to_test = dynamic_lpp_points_calc([
        (1, {"remainder": 1}),
        (500, {"sportcheck": 75, "tim_hortons": 25, "subway": 25}),
        (300, {"sportcheck": 75, "tim_hortons": 25}),
        (200, {"sportcheck": 75})], {"sportcheck": 1000, "the_bay": 5000})

        self.assertEquals(int(maximizer_to_test.Objective().Value()), 7625)


if __name__ == '__main__':
    unittest.main()