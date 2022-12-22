# https://projecteuler.net/problem=2

'''
Correct Answer: 4613732
'''

BOUND = 4000000

def main():
    # Bound Check
    if BOUND < 2:
        return 0
    if BOUND < 8:
        return 2
    if BOUND < 34:
        return 8
    
    # Store current and last two Even Fib (EF-x) numbers
    EF0, EF1, EF2 = 2, 2, 0
    total = 0

    while EF0 <= BOUND:
        total += EF0

        # Formula exploits the fact that every 3rd fib is even
        # Derivation explained on https://www.geeksforgeeks.org/nth-even-fibonacci-number/
        EF0 = (4 * EF1) + EF2
        EF1, EF2 = EF0, EF1

    return total

if __name__ == "__main__":
    total = main()
    print(f"Total: {total}")