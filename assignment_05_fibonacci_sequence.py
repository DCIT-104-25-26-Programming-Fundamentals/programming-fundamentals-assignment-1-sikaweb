# =============================================================================
## Part A: Print the first N Fibonacci numbers
def print_fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be greater than 0.")
        return

    first = 0
    second = 1

    print("Fibonacci sequence:", end=" ")

    for i in range(n):
        print(first, end=" ")
        next_number = first + second
        first = second
        second = next_number

    print()


# Part B: Check if a number is a Fibonacci number
def is_fibonacci(number):
    if number < 0:
        return False

    first = 0
    second = 1

    while first < number:
        next_number = first + second
        first = second
        second = next_number

    return first == number


# Main program
def main():
    # Part A
    n = int(input("How many terms? "))
    print_fibonacci(n)

    # Part B
    number = int(input("Enter a number to check: "))

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


# Run the program
main()