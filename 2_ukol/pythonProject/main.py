from math import gcd, comb


def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

def main(n):

    nsk = sum([phi(x) for x in range(1, 2*n + 1)])
    sk = comb(2*n, 2) - nsk


    vybrane_kombinace = comb(n+1, 2)
    if vybrane_kombinace <= sk:
        print("neplati")
    else:
        print("plati")

main(8)

#print(phi(8) + phi(7) +phi(6) + phi(5) + phi(4) + phi(3) + phi(2) + phi(1))