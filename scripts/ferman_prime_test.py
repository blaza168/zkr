from utils.multiply import square_multiply
import random
from argparse import ArgumentParser


def test(a, n):
    return square_multiply(a, n-1, n) == 1


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='Display positives')
    parser.add_argument('number', type=int)
    args = parser.parse_args()

    verbose = args.verbose
    n = args.number

    if verbose:
        print("Positives: ", end='')
    for i in range(10):
        a = random.randint(1, n - 1)
        if not test(a, n):
            print("False")
            exit()
        if verbose:
            print(str(a) + " ", end='')

    if verbose:
        print()
    print("True")