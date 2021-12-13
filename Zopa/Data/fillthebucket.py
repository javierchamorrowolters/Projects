import pandas as pd
import sys
import argparse

from Scripts import LoansCalculator

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    args = parser.parse_args()
    name = args.name
    LoansCalculator. fill_the_bucket_2(name)

except:
    LoansCalculator. fill_the_bucket_2()
