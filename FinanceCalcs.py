
"""Financial Calculator formulas
m = number of compounding periods per year:
 (annually m=1, semi-annually m=2, quarterly m=4; monthly m=12, daily = 365)
r = the annual interest rate as a decimal: (12% = 0.12)
t= the time in years: (6 months = 0.5 years)
i= interest
p= principal
A = Future Value
P = Present Value
"""


class SimpleFinanceCalc(object):

    def __init__(self):

        self.principal = None
        self.interest_rate = None
        self.time = 1
        self._interest = None
        self._future_value = None
        self._present_value = None

    def s_interest(self, **kwargs):

        if kwargs is not None:
            self.principal = kwargs['principal']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self.principal <= 0:
            print("Principal amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._interest = self.principal * self.interest_rate * self.time
            print("\nPrincipal %s \nInt Rate: %s \nLoan Time: %s \nInterest: %s"
                  % ('${:0,.2f}'.format(self.principal),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     '${:0,.2f}'.format(self._interest)))
            r_interest = {'interest': self._interest,
                          'interest_rate': self.interest_rate * 100,
                          'time': self.time,
                          'principal': self.principal}
            return r_interest

    def s_future_value(self, **kwargs):

        if kwargs is not None:
            self.principal = kwargs['principal']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self.principal <= 0:
            print("Principal amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._interest = (self.principal * self.interest_rate * self.time)
            self._future_value = self.principal + (self.principal * self.interest_rate * self.time)
            print("\nPrincipal %s \nInt Rate: %s \nLoan Time: %s \nInterest: %s \nFuture Value: %s"
                  % ('${:0,.2f}'.format(self.principal),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     '${:0,.2f}'.format(self._interest),
                     '${:0,.2f}'.format(self._future_value)))

            r_future_value = {'future_value': self._future_value,
                              'interest': self._interest,
                              'interest_rate': self.interest_rate * 100,
                              'time': self.time,
                              'principal': self.principal}
            return r_future_value

    def s_present_value(self, **kwargs):

        if kwargs is not None:
            self._future_value = kwargs['future_value']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self._future_value <= 0:
            print("Principal amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._present_value = self._future_value / (1 + self.interest_rate * self.time)
            print("\nFuture Value %s \nInt Rate: %s \nLoan Time: %s \nPresent Value: %s"
                  % ('${:0,.2f}'.format(self._future_value),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     '${:0,.2f}'.format(self._present_value)))

            r_present_value = {'present_value': self._present_value,
                               'interest_rate': self.interest_rate * 100,
                               'time': self.time,
                               'principal': self.principal}
            return r_present_value


class CompoundFinanceCalc(object):

    def __init__(self):

        self.principal = None
        self.interest_rate = None
        self.time = 1
        self.periods = 1
        self._interest = None
        self._future_value = None
        self._present_value = None
        self._pmt = None

    def c_futurevalue(self, **kwargs):

        if kwargs is not None:
            self.principal = kwargs['principal']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self.principal <= 0:
            print("Principal amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._future_value = self.principal * (1 + (self.interest_rate/self.periods)) ** (self.periods * self.time)
            print("\nPrincipal %s \nInt Rate: %s\nLoan Time: %s\nPeriods: %s\nTotal Periods %s\nFuture Value: %s"
                  % ('${:0,.2f}'.format(self.principal),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     self.periods,
                     self.time * self.periods,
                     '${:0,.2f}'.format(self._future_value)))

            r_future_value = {'future_value': self._future_value,
                              'principal': self.principal,
                              'interest_rate': self.interest_rate * 100,
                              'time': self.time,
                              'periods': self.periods}
            return r_future_value

    def c_presentvalue(self, **kwargs):

        if kwargs is not None:
            self._future_value = kwargs['future_value']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self._future_value <= 0:
            print("Future Value amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._present_value = self._future_value / (
                (1 + (self.interest_rate / self.periods)) ** (self.periods * self.time))
            print("\nFuture Value %s\nInt Rate: %s\nLoan Time: %s\nPeriods: %s\nTotal Periods %s\nPresent Value: %s"
                  % ('${:0,.2f}'.format(self._future_value),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     self.periods,
                     self.time * self.periods,
                     '${:0,.2f}'.format(self._present_value)))

            r_present_value = {'present_value': self._present_value,
                               'future_value': self._future_value,
                               'interest_rate': self.interest_rate * 100,
                               'time': self.time,
                               'periods': self.periods}
            return r_present_value

    def c_pv2pmt(self, **kwargs):
        if kwargs is not None:
            if 'principal' in kwargs:
                self._present_value = kwargs['principal']
            else:
                self._present_value = kwargs['present_value']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self._present_value <= 0:
            print("Future Value amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._pmt = self._present_value * ((self.interest_rate / self.periods) / (
                1 - (1 + (self.interest_rate / self.periods)) ** (-1 * self.periods * self.time)))
            print("\nPresent Value %s\nInt Rate: %s\nLoan Time: %s\nPeriods: %s\nTotal Periods %s\nPayment: %s"
                  % ('${:0,.2f}'.format(self._present_value),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     self.periods,
                     self.time * self.periods,
                     '${:0,.2f}'.format(self._pmt)))

            r_pmt = {'pmt': self._pmt,
                     'present_value': self._present_value,
                     'interest_rate': self.interest_rate * 100,
                     'time': self.time,
                     'periods': self.periods}
            return r_pmt

    def c_pmt2pv(self, **kwargs):

        if kwargs is not None:
            self._pmt = kwargs['pmt']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self._pmt <= 0:
            print("Principal amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._present_value = self._pmt * (
                        (1 - (1 + (self.interest_rate / self.periods)) ** (-1 * self.periods * self.time)) / (
                            self.interest_rate / self.periods))
            print("\nPayment %s\nInt Rate: %s\nLoan Time: %s\n" \
                  "Periods: %s\nTotal Periods %s\nPresent Value of Annuity: %s"
                  % ('${:0,.2f}'.format(self._pmt),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     self.periods,
                     self.time * self.periods,
                     '${:0,.2f}'.format(self._present_value)))

            r_present_value = {'present_value': self._present_value,
                               'pmt': self._pmt,
                               'interest_rate': self.interest_rate * 100,
                               'time': self.time,
                               'periods': self.periods}
            return r_present_value

    def c_fv2pmt(self, **kwargs):

        if kwargs is not None:
            if 'principal' in kwargs:
                self._future_value = kwargs['principal']
            else:
                self._future_value = kwargs['future_value']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self._future_value <= 0:
            print("Future Value amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._pmt = self._future_value * ((self.interest_rate / self.periods) / (
                  (1 + (self.interest_rate / self.periods)) ** (self.periods * self.time)-1))
            print("\nPresent Value %s\nInt Rate: %s\nLoan Time: %s\nPeriods: %s\nTotal Periods %s\nPayment: %s"
                  % ('${:0,.2f}'.format(self._future_value),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     self.periods,
                     self.time * self.periods,
                     '${:0,.2f}'.format(self._pmt)))

            r_pmt = {'pmt': self._pmt,
                     'future_value': self._future_value,
                     'interest_rate': self.interest_rate * 100,
                     'time': self.time,
                     'periods': self.periods}
            return r_pmt

    def c_pmt2fv(self, **kwargs):

        if kwargs is not None:
            self._pmt = kwargs['pmt']
            self.interest_rate = float(kwargs['interest_rate'])/100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        if self._pmt <= 0:
            print("Principal amount should be larger than zero")
        elif self.interest_rate <= 0:
            print("Interest rate should be larger than zero")
        else:
            self._future_value = self._pmt * (
                        ((1 + (self.interest_rate / self.periods)) ** (self.periods * self.time)-1) / (
                            self.interest_rate / self.periods))
            print("\nPayment %s\nInt Rate: %s\nLoan Time: %s\n"
                  "Periods: %s\nTotal Periods %s\nPresent Value of Annuity: %s"
                  % ('${:0,.2f}'.format(self._pmt),
                     '{:0,.4f}'.format(self.interest_rate),
                     self.time,
                     self.periods,
                     self.time * self.periods,
                     '${:0,.2f}'.format(self._future_value)))

            r_present_value = {'future_value': self._future_value,
                               'pmt': self._pmt,
                               'interest_rate': self.interest_rate * 100,
                               'time': self.time,
                               'periods': self.periods}
            return r_present_value

    def amort_sched(self, **kwargs):

        if kwargs is not None:
            if 'principal' in kwargs:
                self.principal = kwargs['principal']
            else:
                self.principal = kwargs['present_value']
            self._pmt = kwargs['pmt']
            self.interest_rate = float(kwargs['interest_rate']) / 100
            self.time = kwargs['time']
            self.periods = kwargs['periods']
        else:
            print("Something went wrong, check the Args in the Dictionary")

        periods = int(self.time * self.periods)
        interest_paid = self.principal * (self.interest_rate / self.periods)
        principal_paid = self._pmt - interest_paid
        balance = self.principal - principal_paid

        print("\nPayment#:  Payment  Principal paid:  Interest paid: Balance:")
        print("   0        %s     %s           %s    %s" % (
            '${:0,.2f}'.format(self._pmt), '${:0,.2f}'.format(principal_paid), '${:0,.2f}'.format(interest_paid),
            '${:0,.2f}'.format(balance)))

        for i in range(periods - 1):
            self.principal -= principal_paid
            interest_paid = self.principal * (self.interest_rate / self.periods)
            principal_paid = self._pmt - interest_paid
            balance = self.principal - principal_paid
            if interest_paid < 0:
                break
            print("    %s        %s     %s           %s    %s" % (i + 1, '${:0,.2f}'.format(self._pmt),
                                                                  '${:0,.2f}'.format(principal_paid),
                                                                  '${:0,.2f}'.format(interest_paid),
                                                                  '${:0,.2f}'.format(balance)))
