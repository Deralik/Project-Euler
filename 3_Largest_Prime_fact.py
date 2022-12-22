# https://projecteuler.net/problem=3

'''
Correct Answer: 6857
'''

import time
from math import sqrt

BOUND = 600851475143

def main():
    lpf = 0
    prime_flag = True
    unique_factors = [3]

    start_time = time.time()
    # Factors larger than the squrt of the bound do not exist
    # Check only the odd numbers up to that new bound
    for i in range(1, int(sqrt(BOUND)), 2):
        # Confirm if @i is a prime
        prime_flag = True
        for j in range(3, int(sqrt(i)), 2):
            if i % j == 0:
                prime_flag = False
                break

        # Update if @i is a prime factor
        if prime_flag and BOUND % i == 0:
            lpf = i
    print(f"Normal method: {time.time() - start_time}")
    print(f"Largest Prime Factor: {lpf}")

    start_time = time.time()

    for i in range(1, int(sqrt(BOUND)), 2):
        i_bound = int(sqrt(i))
        unique_flag = True
        # when @i_bound increases, check if it's a unique factor
        if i_bound > unique_factors[-1] and i_bound % 2:
            for f in unique_factors:
                if i_bound % f == 0:
                    unique_flag = False
                    break
            if unique_flag:
                unique_factors.append(i_bound)

        # Confirm if @i is a prime
        prime_flag = True
        for j in unique_factors:
            if i % j == 0:
                prime_flag = False
                break

        # Update if @i is a prime factor of @BOUND
        if prime_flag and BOUND % i == 0:
            lpf = i
    print(f"Unique list Method: {time.time() - start_time}")

    print(f"Largest Prime Factor: {lpf}")


if __name__ == "__main__":
    main()