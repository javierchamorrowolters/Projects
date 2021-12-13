import pandas as pd
import sys
import argparse

from Scripts import LoansCalculator

#LoansCalculator.test()

parser = argparse.ArgumentParser()
parser.add_argument('name')
args = parser.parse_args()

name = args.name
LoansCalculator.test(name)
