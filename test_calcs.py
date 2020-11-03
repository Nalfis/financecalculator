import unittest
import FinanceCalcs


class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_simple_interest(self):
        """
        Test that the calculation of the simple interest method
        """

        simpcalc = FinanceCalcs.SimpleFinanceCalc()
        simple_args = {'principal': 228.39,
                       'interest_rate': 3.49,
                       'time': 5}
        result = simpcalc.s_interest(**simple_args)
        pass_result = {'interest': 39.854054999999995,
                                  'interest_rate': 3.49,
                                  'principal': 228.39,
                                  'time': 5}
        self.assertEqual(result, pass_result)

    def test_future_value(self):
        """
        Test that the calculation of future value method
        """

        simpcalc = FinanceCalcs.SimpleFinanceCalc()
        simple_args = {'principal': 228.39,
                       'interest_rate': 3.49,
                       'time': 5}
        result = simpcalc.s_future_value(**simple_args)
        pass_result = {'future_value': 268.244055,
                                  'interest': 39.854054999999995,
                                  'interest_rate': 3.49,
                                  'principal': 228.39,
                                  'time': 5}
        self.assertEqual(result, pass_result)

    def test_present_value(self):
        """
        Test that the calculation of present value method
        """

        simpcalc = FinanceCalcs.SimpleFinanceCalc()
        simple_args2 = {'future_value': 268.244055,
                        'interest': 39.854054999999995,
                        'interest_rate': 3.49,
                        'principal': 228.39,
                        'time': 5}
        pass_result = {'interest_rate': 3.49,
                                  'present_value': 228.39,
                                  'principal': None, 'time': 5}
        result = simpcalc.s_present_value(**simple_args2)
        self.assertEqual(result, pass_result)

    def test_compound_future_value(self):
        """
        Test Compound Future Value method
        """
        compcalc = FinanceCalcs.CompoundFinanceCalc()
        graduateplus_pv = {'principal': 139492.06,
                           "interest_rate": 4.5,
                           "time": 10,
                           "periods": 12}
        result = compcalc.c_futurevalue(**graduateplus_pv)
        pass_result = {'future_value': 218583.05036866403,
                       'interest_rate': 4.5,
                       'periods': 12,
                       'principal': 139492.06,
                       'time': 10}

        self.assertEqual(result, pass_result)

    def test_compound_present_value(self):
        """
        Test Compound Future Value method
        """
        compcalc = FinanceCalcs.CompoundFinanceCalc()
        graduateplus_pv = {'principal': 139492.06,
                           "interest_rate": 4.5,
                           "time": 10,
                           "periods": 12}
        result = compcalc.c_presentvalue(**compcalc.c_futurevalue(**graduateplus_pv))
        pass_result = {'future_value': 218583.05036866403,
                       'interest_rate': 4.5,
                       'periods': 12,
                       'present_value': 139492.06,
                       'time': 10}
        self.assertEqual(result, pass_result)

    def test_compound_pv_pmt(self):
        """
        Test Compound Present Value to Payment method
        """
        compcalc = FinanceCalcs.CompoundFinanceCalc()
        staffordloans_pv = {'present_value': 131598.83,
                            "interest_rate": 3.7,
                            "time": 10,
                            "periods": 12}
        result = compcalc.c_pv2pmt(**staffordloans_pv)
        pass_result = {'present_value': 131598.83,
                       'interest_rate': 3.7000000000000006,
                       'pmt': 1313.69171513367,
                       'time': 10,
                       'periods': 12}
        self.assertEqual(result, pass_result)

    def test_compound_pmt_pv(self):
        """
        Test Compound Present Payment to Present Value method
        """
        compcalc = FinanceCalcs.CompoundFinanceCalc()
        staffordloans_pv = {'present_value': 131598.83,
                            "interest_rate": 3.7,
                            "time": 10,
                            "periods": 12}
        result = compcalc.c_pmt2pv(**compcalc.c_pv2pmt(**staffordloans_pv))
        pass_result = {'present_value': 131598.83,
                       'interest_rate': 3.7000000000000006,
                       'pmt': 1313.69171513367,
                       'time': 10,
                       'periods': 12}
        self.assertEqual(result, pass_result)

    def test_compound_fv_pmt(self):
        """
        Test Compound Future Value to Payment method
        """
        compcalc = FinanceCalcs.CompoundFinanceCalc()
        staffordloans_pv = {'future_value': 131598.83,
                            "interest_rate": 3.7,
                            "time": 10,
                            "periods": 12}
        result = compcalc.c_fv2pmt(**staffordloans_pv)
        pass_result = {'future_value': 131598.83,
                       'interest_rate': 3.7000000000000006,
                       'pmt': 907.9286559670032,
                       'time': 10,
                       'periods': 12}
        self.assertEqual(result, pass_result)

    def test_compound_pmt_fv(self):
        """
        Test Compound Future Value to Payment method
        """
        compcalc = FinanceCalcs.CompoundFinanceCalc()
        staffordloans_pv = {'future_value': 131598.83,
                            "interest_rate": 3.7,
                            "time": 10,
                            "periods": 12}
        result = compcalc.c_pmt2fv(**compcalc.c_fv2pmt(**staffordloans_pv))
        pass_result = {'future_value': 131598.83,
                       'interest_rate': 3.7000000000000006,
                       'pmt': 907.9286559670032,
                       'time': 10,
                       'periods': 12}
        self.assertEqual(result, pass_result)


if __name__ == '__main__':
    unittest.main()