# # Finance Calculator
   #  Finance Calculator How to use it:

    m = number of compounding periods per year:(annually m=1, semi-annually m=2, quarterly m=4; monthly m=12, daily = 365)
    r = the annual interest as a decimal: (12%%  = 0.12)
    t= the time in years: (6 months = 0.5 years)
    i= interest
    p= principal
    A = Future Value
    P = Present Value

   # # how to run it from command line:

        From Python CLI:

        - python -m  finance -h [for detailed help]
        - python -m finance -ct cmp -p 15000 -t 10 -m 12 -i 5 -cpv2pmt [calculates compound present value to payment ammount]
        - python -m finance -ct cmp -p 15000 -t 10 -m 12 -i 5 -camort [calculates amortization payment table]

   # # How to run the executable
   
        From OS CLI:
        
        - finance.exe -ct smp -p 500 -i 7 -t 5 -si
        - finance.exe -ct smp -p 500 -i 7 -t 5 -spv
        - finance.exe -ct smp -p 500 -i 7 -t 5 -cpv