if __name__ == '__main__':
    from core_functions import phi
    from multiply import square_multiply
else:
    from .core_functions import phi
    from .multiply import square_multiply
from sympy import gcd, mod_inverse





def calculate_inverse_element(a, mod):
    return mod_inverse(a, mod)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: [a] [mod]")
        exit()
    a, mod = int(sys.argv[1]), int(sys.argv[2])
    inverse = calculate_inverse_element(a, mod)
    if inverse is None:
        print("Inverse element doesnt exist!")
        print("GDC(%d, %d) = %d" % (a, mod, gcd(a, mod)))
    else:
        print("Inverse element: " + str(inverse))
