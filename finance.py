import argparse
import FinanceCalcs


parser = argparse.ArgumentParser(description="Finance Application",
                                 usage='''Financial Calculator formulas
m = number of compounding periods per year:(annually m=1, semi-annually m=2, quarterly m=4; monthly m=12, daily = 365)
r = the annual interest as a decimal: (12%%  = 0.12)
t= the time in years: (6 months = 0.5 years)
i= interest
p= principal
A = Future Value
P = Present Value
''')
parser.add_argument("-ct", type=str, dest='calc_type', choices=['smp', 'cmp'], help="choose interest type: compound "
                                                                                    "interest or simple interest")
parser.add_argument("-p", "--principal", type=float, required=True, help="Input Principal Ammount - Float")
parser.add_argument("-i", "--interest", type=float, required=True, help="Input Interest Ammount - Float")
parser.add_argument("-t", "--time", type=float, required=True, help="Input time in years (6 months = 0.5)")
parser.add_argument("-m", "--compound_periods", type=int, required=False, default=12, help="number of compounding periods per year (annually m=1, "
                                                                                   "semi-annually m=2, quarterly m=4; monthly m=12, daily = 365")
parser.add_argument("-si", "--simple_interest", action='store_true', required=False, help="Calculate Simple Interest")
parser.add_argument("-sfv", "--s_future_value", action='store_true', required=False, help="Calculate Simple Future Value")
parser.add_argument("-spv", "--s_present_value", action='store_true', required=False, help="Calculate Simple Present Value")
parser.add_argument("-cfv", "--c_future_value", action='store_true', required=False, help="Calculate Compound Future Value")
parser.add_argument("-cpv", "--c_present_value", action='store_true', required=False, help="Calculate Compound Present Value")
parser.add_argument("-cpv2pmt", "--c_pv2pmt", action='store_true', required=False, help="Calculate Compound Present Value to Payment")
parser.add_argument("-cpmt2pv", "--c_pmt2pv", action='store_true', required=False, help="Calculate Payment to Compound Present Value")
parser.add_argument("-cfv2pmt", "--c_fv2pmt", action='store_true', required=False, help="Calculate Compound Future Value to Payment")
parser.add_argument("-cpmt2fv", "--c_pmt2fv", action='store_true', required=False, help="Calculate Payment to Compound Future Value")
parser.add_argument("-camort", "--c_amort", action='store_true', required=False, help="Calculate Amortization Schedule")

parser.parse_args()
args = parser.parse_args()
if args.calc_type == 'smp':
    simpargs = {'principal': args.principal,
                'interest_rate': args.interest,
                'time': args.time}
    simplecalc = FinanceCalcs.SimpleFinanceCalc()
    if args.simple_interest:
        simplecalc.s_interest(**simpargs)
    elif args.s_future_value:
        simplecalc.s_future_value(**simpargs)
    elif args.s_present_value:
        simplecalc.s_present_value(**simplecalc.s_future_value(**simpargs))
else:
    compoundcalc = FinanceCalcs.CompoundFinanceCalc()
    compound_args = {'principal': args.principal,
                     'interest_rate': args.interest,
                     'time': args.time,
                     'periods': args.compound_periods}
    if args.c_future_value:
        compoundcalc.c_futurevalue(**compound_args)
    elif args.c_present_value:
        compoundcalc.c_presentvalue(**compoundcalc.c_futurevalue(**compound_args))
    elif args.c_pv2pmt:
        compoundcalc.c_pv2pmt(**compound_args)
    elif args.c_pmt2pv:
        compoundcalc.c_pmt2pv(**compoundcalc.c_pv2pmt(**compound_args))
    elif args.c_fv2pmt:
        compoundcalc.c_fv2pmt(**compound_args)
    elif args.c_pmt2fv:
        compoundcalc.c_pmt2fv(**compoundcalc.c_fv2pmt(**compound_args))
    elif args.c_amort:
        compoundcalc.c_pv2pmt(**compound_args)
        compoundcalc.amort_sched(**compoundcalc.c_pv2pmt(**compound_args))
    else:
        print("something went wrong, check the args list or use -h for more info")
