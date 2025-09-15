print("The FACTORIAL program")

# ask user for input
num = int(input("Enter any number: "))

# compute factorial
factorial = 1
for i in range(1, num + 1):
    factorial *= i

# show result

print(f"The Factorial of {num} is {factorial}")
