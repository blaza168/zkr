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
        is_generator = True
        for i in int_factors:
            if pow(a, int(phi_p / i), p) == 1:
                is_generator = False
                break

        if is_generator:
            found_generators.append(a)
        a += 1

    return found_generators


# if __name__ == '__main__':
#
#     generators = get_generators(int(sys.argv[1]))
#
#     print("Generators: ")
#     for i in generators:
#         print(i, end=" ")

generators = get_generators(13)

print("Generators: ")
for i in generators:
    print(i, end=" ")