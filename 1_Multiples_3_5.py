# https://projecteuler.net/problem=1

'''
Correct Answer: 233168
'''

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
    total += bounded_sum(MULS[0])
    total += bounded_sum(MULS[1])

    # subtract duplicates
    total -= bounded_sum(MULS[0]*MULS[1])

    print(f"Total: {total}\n")

if __name__ == "__main__":
    main()