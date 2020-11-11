if __name__ == '__main__':
    import sys
    sys.path.append('../')
from sympy import factorint
from utils.core_functions import phi


def get_generators(p):
    phi_p = phi(p)
    generators_num = phi(phi_p)
    found_generators = []
    int_factors = factorint(phi_p).keys()

    a = 2
    while len(found_generators) != generators_num:

        for i in int_factors:
            if pow(a, phi_p / i) == 1:
                continue

        found_generators.append(a)
        a += 1

    return found_generators


if __name__ == '__main__':

    generators = get_generators(int(sys.argv[1]))

    print("Generators: ")
    for i in generators:
        print(i, end=" ")
