import re

# start with the smallest prime number
SMALLEST_PRIME = 2


def generate_prime_tuples(input_number: int) -> list[tuple[int, int]]:
    """Assuming Goldbach’s conjecture that every even natural number greater than 2
    is the sum of two prime numbers, generate the tuple(s) of primes that make up the input number.

    :param input_number: integer to be split into two primes.
    :return: A list of tuples containing two prime numbers as integers each.
    """
    input_number = handle_odd_number_input(input_number)
    list_of_primes = []
    i = SMALLEST_PRIME
    #  get the first prime number
    while i <= input_number // 2:
        if check_is_prime(i):
            # now check if j (= input_number - i) is prime
            j = input_number - i
            if check_is_prime(j):
                list_of_primes.append((i, j))
        i += 1
    return list_of_primes


def check_is_prime(n: int) -> bool:
    """If i is divisible by any divisor (excl. 1 and itself) it's not a prime.
    Return True only if n is a prime number.

    :param n: integer to be check whether it is a prime number
    """
    if n <= 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


def handle_odd_number_input(number: int) -> int:
    """Catch odd numbers from the input,
    since they are not covered by the Goldbach conjecture.
    Handles recursive calling for input in case of odd numbers.

    :param number: integer to be checked whether even or odd
    :return: an even integer
    """
    if number % 2 == 1:
        number = get_user_number_input("Your number is an ODD number."
                                       "\nPlease enter an EVEN number:")
    return number


def get_user_number_input(prompt: str) -> int:
    """Get input that exclusively matches integer pattern
    at the start of the string only accept one or more digits

    :param prompt: String to prompt user input.
    :return: The user input converted from str to int
    """
    pattern = re.compile(r"^\d+$")
    while True:
        user_input = input(prompt).strip()
        if pattern.match(user_input):
            return int(user_input)
        print(f"You entered '{user_input}'. That's not a positive integer.")


def main():
    input_number = get_user_number_input("Enter an integer:")
    list_of_prime_tuples = generate_prime_tuples(input_number)
    for i, j in list_of_prime_tuples:
        print(f"The number {input_number} equals to the sum of {i} and {j}")


if __name__ == '__main__':
    main()
