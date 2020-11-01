import argparse
import FinanceCalcs



parser = argparse.ArgumentParser()
parser.add_argument("-P", "--present_value", type=float, required=False, help="Input Present Value - Float")
parser.add_argument("-A", "--future_value", type=float, required=False, help="Input Future Value - Float")
parser.add_argument("-p", "--princial", type=float, required=True, help="Input Principal Ammount - Float")
parser.add_argument("-i", "--interes", type=float, required=True, help="Input Interest Ammount - Float")
parser.add_argument("-t", "--time", type=float, required=True, help="Input time in years (0.5 equals 6 months)")
parser.add_argument("-r", "--annual_interest", type=float, required=True, help="Annual Int Rate as decimal (12 percent equals 0.12)")
parser.add_argument("-m", "--compound_periods", type=int, required=True, help="number of compounding periods per year (annually m.1, semi-annually " \
                                                                              "m.2, "
                                                                              "monthly m.12, daily.365) - Integer")

parser.parse_args()
args = parser.parse_args()

simplecalc = FinanceCalcs.SimpleFinanceCalc()
simplecalc.s_interest(**args)
