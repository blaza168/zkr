from utils.multiply import square_multiply
import sys
import random


def test(a, n):
    return square_multiply(a, n-1, n) == 1


if __name__ == '__main__':
    n = int(sys.argv[1])

    for i in range(10):
        a = random.randint(1, n - 1)
        if not test(a, n):
            print("False")
            exit()

    print("True")