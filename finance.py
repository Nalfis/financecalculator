import argparse
import FinanceCalcs


parser = argparse.ArgumentParser()
parser.add_argument("-si", "--simple_interest", type=bool, default=False, required=False, help="Calculate Simple Interest")
parser.add_argument("-fv", "--futura_value", type=bool, default=False, required=False, help="Calculate Future Value")
parser.add_argument("-pv", "--presente_value", type=bool, default=False, required=False, help="Calculate Present Value")
parser.add_argument("-P", "--present_value", type=float, required=False, help="Input Present Value - Float")
parser.add_argument("-A", "--future_value", type=float, required=False, help="Input Future Value - Float")
parser.add_argument("-p", "--principal", type=float, required=True, help="Input Principal Ammount - Float")
parser.add_argument("-i", "--interest", type=float, required=True, help="Input Interest Ammount - Float")
parser.add_argument("-t", "--time", type=float, required=True, help="Input time in years (0.5 equals 6 months)")
parser.add_argument("-r", "--annual_interest", type=float, required=True, help="Annual Int Rate as decimal (12 percent equals 0.12)")
parser.add_argument("-m", "--compound_periods", type=int, required=True, help="number of compounding periods per year (annually m.1, semi-annually " \
                                                                              "m.2, "
                                                                              "monthly m.12, daily.365) - Integer")


parser.parse_args()
args = parser.parse_args()
simpargs = {'principal': args.principal,
            'interest_rate': args.interest,
            'time': args.time}
simplecalc = FinanceCalcs.SimpleFinanceCalc()
if args.simple_interest:
    simplecalc.s_interest(**simpargs)
elif args.futura_value:
    simplecalc.s_future_value(**simpargs)
elif args.presente_value:
    simplecalc.s_present_value(**simplecalc.s_future_value(**simpargs))
