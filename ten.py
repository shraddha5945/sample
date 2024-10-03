def add_numbers(n):
    """
    Adds n numbers together.

    Args:
        n: The number of numbers to add.

    Returns:
        The sum of the numbers.
    """

    sum = 0
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        sum += num
    return sum

# Get the number of numbers to add from the user
num_numbers = int(input("How many numbers do you want to add? "))

# Call the function to add the numbers
result = add_numbers(num_numbers)

# Print the result
print(f"The sum of the numbers is: {result}")
