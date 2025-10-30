# Nth Prime Number Calculator

A Python application that calculates and finds the nth prime number from a precomputed list of prime numbers.

## Description

This project contains a simple yet efficient implementation for finding prime numbers and retrieving the nth prime number. The application:

- **Generates prime numbers**: Uses the Sieve-like approach to find all prime numbers up to 10,000
- **Prime checking function**: Implements `is_prime(n)` that checks if a given number is prime using trial division up to the square root
- **Nth prime retrieval**: Provides `nth_prime(n)` function that returns the nth prime number from the precomputed list

## Features

- ✅ Efficiently checks if a number is prime
- ✅ Precomputes prime numbers up to 10,000 for fast lookup
- ✅ Finds the nth prime number in O(1) time after initial computation
- ✅ Clean, readable code with proper documentation

## How it works

1. The application iterates through numbers from 0 to 10,000
2. Each number is checked using the `is_prime()` function
3. Prime numbers are stored in a list called `prime_numbers`
4. The `nth_prime(n)` function returns the nth prime number by indexing into the precomputed list

## Usage

```python
# Find the 5th prime number
result = nth_prime(5)  # Returns 11

# Find the 1000th prime number
result = nth_prime(1000)  # Returns 7919
```

## Example Output

The application can find:
- 5th prime: 11
- 10th prime: 29
- 16th prime: 53
- 99th prime: 523
- 1000th prime: 7919

## Requirements

- Python 3.x
- No external dependencies required

## Running the Application

1. Make sure you have Python 3 installed
2. Clone or download this repository
3. Navigate to the project directory
4. Run the application:

```bash
python app.py
```

## Algorithm Complexity

- **Prime checking**: O(√n) for each number
- **Initial computation**: O(n√n) where n is the upper limit (10,000)
- **Nth prime lookup**: O(1) after precomputation
