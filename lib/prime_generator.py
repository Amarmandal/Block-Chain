import random
import math

#check whether a given number is a prime number or not
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#generate random prime number with the given range
def generate_random_prime(start, end):
    p = random.randint(start, end)
    while not is_prime(p):
        p = random.randint(start, end)
    return p


