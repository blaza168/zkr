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
    n = int(sys.argv[1])
    iterations = 10

    chance = (1 - math.pow(0.25, iterations)) * 100
    for i in range(10):
        a = random.randint(1, n - 1)
        if not test(a, n):
            print("False")
            exit()
    
    print("Change: " + str(chance))
    print("True")
