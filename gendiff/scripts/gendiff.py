import argparse
parser = argparse.ArgumentParser(prog ='gendiff',
                        description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file', help='')
parser.add_argument('second_file', help='')
parser.add_argument('-f','--format', help = 'set format of output')

def main():
    return parser.print_help()

if  __name__ == '__main__':
    main()