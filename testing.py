import unittest
import rules
from data import get_monthly_spendings

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


if __name__ == '__main__':
    unittest.main()