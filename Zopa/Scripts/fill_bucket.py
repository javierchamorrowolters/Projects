# Fill the Bucket Script

import argparse
my_parser = argparse.ArgumentParser()
my_parser.add_argument('n_groups', type=int)
args = my_parser.parse_args()
input_n_groups = args.n_groups

import sys
sys.path.append('..')
from ToolsLoanCalculator import LoanCalculator
LoanCalculator.FillTheBucket(input_n_groups)
