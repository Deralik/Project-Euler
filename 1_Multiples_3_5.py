# https://projecteuler.net/problem=1

# Made to work with any bound and set of multiples

'''
Correct Answer: 233168
'''

from itertools import combinations

BOUND = 1000
MULS = [3, 5]

# Function to sum all multiples of @mul under the bound
def bounded_sum(mul):
    total = 0
    num = mul
    for i in range(0, int((BOUND-1)/mul)):
        total += num
        num += mul
    
    return total

def main():
    total = 0

    # Find individual total
    for i in range(0, len(MULS)):
        total += bounded_sum(MULS[i])

    # Find and subtract set of duplicate multiples
    dups = list(map(lambda a: a[0] * a[1], combinations(MULS, 2)))
    for i in range(0, len(dups)):
        total -= bounded_sum(dups[i])

    print(f"Total: {total}")

if __name__ == "__main__":
    main()