import unittest
from common import FinanceCalcs


class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_simple_interest(self):
        """
        Test that the calculation of the simple interest function
        """

        simpcalc = FinanceCalcs.SimpleFinanceCalc()
        simple_args = {'principal': 228.39,
                       'interest_rate': 3.49,
                       'time': 5}
        result = simpcalc.s_interest(**simple_args)
        self.assertEqual(result, {'interest': 39.854054999999995,
                                    'interest_rate': 3.49,
                                    'principal': 228.39,
                                    'time': 5})


    def test_future_value(self):
        """
        Test that the calculation of future value function
        """

        simpcalc = FinanceCalcs.SimpleFinanceCalc()
        simple_args = {'principal': 228.39,
                       'interest_rate': 3.49,
                       'time': 5}
        result = simpcalc.s_future_value(**simple_args)
        self.assertEqual(result, {'future_value': 268.244055,
                                  'interest': 39.854054999999995,
                                  'interest_rate': 3.49,
                                  'principal': 228.39,
                                  'time': 5})

    def test_present_value(self):
        """
        Test that the calculation of present value function
        """

        simpcalc = FinanceCalcs.SimpleFinanceCalc()
        simple_args2 = {'future_value': 268.244055,
                        'interest': 39.854054999999995,
                        'interest_rate': 3.49,
                        'principal': 228.39,
                        'time': 5}
        result = simpcalc.s_present_value(**simple_args2)
        self.assertEqual(result, {'interest_rate': 3.49,
                                  'present_value': 228.39,
                                  'principal': None, 'time': 5})


if __name__ == '__main__':
    unittest.main()