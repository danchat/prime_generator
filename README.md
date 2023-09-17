# Large Prime Generator for RSA

This repository contains a Python script that generates large prime numbers suitable for RSA encryption.

```plaintext
## Overview

The script uses the Miller-Rabin primality test to probabilistically determine the primality of randomly generated numbers of a desired bit length.

## Requirements

- Python 3.x

## Usage

1. Clone this repository:

   git clone https://github.com/danchat/prime_generator.git
   cd prime_generator

2. Run the script:

   python generate_prime.py

By default, the script generates a 2048-bit prime number. To generate prime numbers of different lengths, modify the `bit_length` variable in `generate_prime.py`.

## Algorithm

The core of this script is the Miller-Rabin primality test. It's a probabilistic test that determines if a number is prime. The test is run multiple times (40 iterations by default) to reduce the probability of falsely identifying a composite number as prime.

The script generates random odd numbers of the desired bit length and tests them for primality. Once a probable prime is found, it's printed to the console.

## Limitations

1. The script is designed for personal use. For production-grade applications, especially with stringent performance or security requirements, relying on well-established libraries is recommended.
   
2. Python's built-in arbitrary precision arithmetic is used, which is slower than optimized libraries like GMP.

## Contributing

Feel free to fork this repository, make your enhancements, and submit pull requests.
