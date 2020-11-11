if __name__ == '__main__':
    import sys
    sys.path.append('../../')

from utils.core_functions import phi
from utils.multiply import square_multiply
from argparse import ArgumentParser


def decrypt_c(c, sk, n):
    return square_multiply(c, sk, n)


if __name__ == '__main__':
    paraer = ArgumentParser()
    paraer.add_argument('-c', required=True, type=int)
    paraer.add_argument('-sk', required=True, type=int)
    paraer.add_argument('-n', required=True, type=int)

    args = paraer.parse_args()

    print(decrypt_c(args.c, args.sk, args.n))
