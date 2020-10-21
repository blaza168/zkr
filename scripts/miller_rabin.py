from argparse import ArgumentParser

from utils.multiply import square_multiply
import sys
import random
import math


# split n into pow(2, s) * r + 1
# Returns: s, r
def __split_n(n):
    i = 1
    for i in range(1, n):
        pow = math.pow(2, i)
        r = int((n - 1) / pow)
        if r % 2 == 1:
            return i, r

    return None


def test(a, n):
    s, r = __split_n(n)
    # First check if pow(a, r) % n == 1
    if square_multiply(a, r, n) == 1:
        return True
    for i in range(s):
        a_power = int(math.pow(2, i) * r)
        if square_multiply(a, a_power, n) == n - 1:
            return True

    return False


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='Display positives')
    parser.add_argument('-i', '--iterations', default=10, type=int, help='Number of iterations')
    parser.add_argument('number', type=int)
    args = parser.parse_args()

    verbose = args.verbose
    n = args.number
    iterations = args.iterations

    chance = (1 - math.pow(0.25, iterations)) * 100
    if verbose:
        print("Positives: ", end='')

    for i in range(iterations):
        a = random.randint(1, n - 1)
        if not test(a, n):
            if verbose:
                print()
            print("False")
            exit()
        if verbose:
            print(str(a) + " ", end='')

    if verbose:
        print()
    print("Change: " + str(chance))
    print("True")
