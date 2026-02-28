import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('archive', help='path to the WAM file ')
args = parser.parse_args()

with open(args.archive, 'rb') as f:
    for line in f:

