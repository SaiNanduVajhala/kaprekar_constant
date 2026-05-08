# Kaprekar Constant Program (6174)

def kaprekar_steps(num):
    steps = 0

    print(f"\nStarting Number: {num}")

    while num != 6174:
        # Convert number to 4 digits
        num_str = f"{num:04d}"

        # Descending and ascending order
        desc = int("".join(sorted(num_str, reverse=True)))
        asc = int("".join(sorted(num_str)))

        # Kaprekar operation
        num = desc - asc
        steps += 1

        print(f"Step {steps}: {desc} - {asc} = {num}")

        # Prevent infinite loop for invalid inputs
        if num == 0:
            print("Kaprekar constant cannot be reached.")
            return

    print(f"\nReached Kaprekar Constant 6174 in {steps} steps.")


# User Input
number = int(input("Enter a 4-digit number: "))

# Validation
num_str = str(number)

if len(num_str) != 4 or len(set(num_str)) == 1:
    print("Enter a valid 4-digit number with at least two different digits.")
else:
    kaprekar_steps(number)