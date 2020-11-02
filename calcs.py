# import common.utils as Utils
import FinanceCalcs

# Construct Object Fincal
simpcalc = FinanceCalcs.SimpleFinanceCalc()
compcalc = FinanceCalcs.CompoundFinanceCalc()

# Create a Fincalc Object

# Validation
# # Simple future value has been validated

# simple_args = {'principal': 228.39,
#                'interest_rate': 3.49,
#                'time': 5}
# simple1 = simpcalc.s_interest(**simple_args)
# simple2 = simpcalc.s_future_value(**simple_args)
# simple3 = simpcalc.s_present_value(**simple2)


# compound future value has been validated
compound_args = {'principal': 12557.81,
                 'interest_rate': 3.49,
                 'time': 5,
                 'periods': 12}

compound1 = compcalc.c_futurevalue(**compound_args)
compound2 = compcalc.c_presentvalue(**compound1)
compound3 = compcalc.c_pv2pmt(**compound2)
compound4 = compcalc.c_pmt2pv(**compound3)
compound5 = compcalc.c_fv2pmt(**compound1)
compound6 = compcalc.c_pmt2fv(**compound5)

#
# sienna_pv = {'present_value': 14717.77, "interest_rate": 2.490, "time": 5.4166667, "periods": 12}
# sienna_pmt = compcalc.c_pv2pmt(**sienna_pv)
# sienna_amort = compcalc.amort_sched(**sienna_pmt)

# graduateplus_pv = {'present_value': 139492.06,
#                    "interest_rate": 4.5,
#                    "time": 10,
#                    "periods": 12}
# staffordloans_pv = {'present_value': 131598.83,
#                     "interest_rate": 3.7,
#                     "time": 10,
#                     "periods": 12}
# graduateplus_pmt = compcalc.c_pv2pmt(**graduateplus_pv)
# graduateplus_amort = compcalc.amort_sched(**graduateplus_pmt)
#
# staffordloans_pmt = compcalc.c_pv2pmt(**staffordloans_pv)
# staffordloans_amort = compcalc.amort_sched(**staffordloans_pmt)
