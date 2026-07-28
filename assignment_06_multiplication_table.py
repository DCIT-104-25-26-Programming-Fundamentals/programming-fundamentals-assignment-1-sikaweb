# =============================================================================
## Part A: Print the multiplication table for a single number
def print_table(number):
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")


# Part B: Print multiplication tables from 1 to N
def print_tables(n):
    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    for number in range(1, n + 1):
        print_table(number)
        print("-" * 30)


# Main program
def main():
    # Part A
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Error: Number must be greater than 0.")
        return

    print_table(number)

    # Part B
    n = int(input("\nEnter a number N: "))

    if n <= 0:
        print("Error: Number must be greater than 0.")
        return

    print_tables(n)


# Run the program
main()