import re

# start with the smallest prime number
SMALLEST_PRIME = 2

def is_sum_of_two_primes(input_number: int) -> bool:
    """"""
    catch_odd_numbers(input_number)
    i = SMALLEST_PRIME
    #  get the first prime number
    while i <= input_number/2:
        i_is_prime = check_is_prime(i)
        if i_is_prime:
            # now check if j (= input_number - i) is prime
            j = input_number - i
            if j >= SMALLEST_PRIME:
                j_is_prime = check_is_prime(j)
                if j_is_prime:
                    print(f"The number {input_number} equals to the sum of {i} and {j}")
        i += 1
    return True


def check_is_prime(i):
    """If i is divisible by any divisor (excl. 1 and itself) it's not a prime.
    Check this condition.
    """
    is_prime = True
    divisor = SMALLEST_PRIME
    while divisor < i:
        if i % divisor == 0:
            is_prime = False
            break
        divisor += 1
    return is_prime


def catch_odd_numbers(number):
    # catch odd numbers
    if number % 2 == 1:
        get_user_number_input("Your number is an ODD number."
                              "\nPlease enter an EVEN number:")


def get_user_number_input(prompt):
    """Get input that exclusively matches integer pattern
    at the start of the string only accept one or more digits

    :param prompt:
    """
    pattern = re.compile(r"^\d+$")
    input_number = input(prompt).strip()
    if pattern.match(input_number):
        input_number = int(input_number)
    else:
        print(f"You entered '{input_number}'. That's not a positive integer.")
        input_number = get_user_number_input(prompt)
    return input_number


def main():
    input_number = get_user_number_input("Enter an integer:")
    is_sum_of_two_primes(input_number)

if __name__ == '__main__':
    main()
