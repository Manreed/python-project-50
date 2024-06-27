import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('dictionary', metavar='first_file')
parser.add_argument('dictionary', metavar='second_file')

args = parser.parse_args()
print(args.accumulate(args.integers))

