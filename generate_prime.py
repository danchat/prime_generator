import random

# Compute (base^exp) mod modulo using modular exponentiation
def mod_pow(base, exp, modulo):
    return pow(base, exp, modulo)

# Conduct the Miller-Rabin primality test to determine if a number is probably prime
def miller_rabin_test(n, k):
    # Handle small values of n
    if n < 2:
        return False
    if n == 2:
        return True
    # Eliminate even numbers > 2
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * s
    # Keep halving n-1 until we get an odd s
    s, r = n - 1, 0
    while s % 2 == 0:
        s //= 2
        r += 1

    # Conduct the Miller-Rabin test k times
    for _ in range(k):
        # Pick a random witness between [2, n-2]
        a = random.randrange(2, n - 1)
        # Compute x = a^s mod n
        x = mod_pow(a, s, n)
        
        # If x is 1 or n-1, continue with the next iteration
        if x == 1 or x == n - 1:
            continue
        
        # Continue squaring x
        for _ in range(r - 1):
            x = mod_pow(x, 2, n)
            # If x becomes n-1, break and continue to the next iteration
            if x == n - 1:
                break
        # If the loop didn't break early, n is composite
        else:
            return False
            
    # If none of the iterations found n to be composite, it's probably prime
    return True

# Generate a random prime number of a given bit length
def generate_large_prime(bit_length):
    while True:
        # Generate a random odd number of bit_length bits
        # The first and last bits are set to ensure the number has the desired length and is odd
        number = random.getrandbits(bit_length) | (1 << (bit_length - 1)) | 1
        
        # If the number is probably prime, return it
        if miller_rabin_test(number, 40):
            return number

# Example usage
bit_length = 2048
prime = generate_large_prime(bit_length)
print("Generated prime:", prime)
