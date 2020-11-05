from sympy import *

# Calculate: pow(a, n) % mod
def square_multiply(a, n, mod):
    a_placeholder, n_placeholder = symbols('x y')

    return Mod(a_placeholder ** n_placeholder, mod).subs({a_placeholder: a, n_placeholder: n})


if __name__ == '__main__':
    import sys
    a, n, mod = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    print(square_multiply(a, n, mod))
