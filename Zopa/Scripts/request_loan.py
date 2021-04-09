# Request Loan Script

import argparse
my_parser = argparse.ArgumentParser()
my_parser.add_argument('loan', type=int)
args = my_parser.parse_args()
input_loan = args.loan

import sys
sys.path.append('..')
from ToolsLoanCalculator import LoanCalculator
LoanCalculator.LoanCalculatorFun(input_loan)
