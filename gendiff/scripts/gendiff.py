import argparse
from gendiff.generate_diff import generate_diff, path_to_file_1, path_to_file_2

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument(
    '-f', '--format', type=str, help='Set format of output', metavar='FORMAT'
)

args = parser.parse_args()


def main():
    print(generate_diff(path_to_file_1, path_to_file_2))


if __name__ == '__main__':
    main()
