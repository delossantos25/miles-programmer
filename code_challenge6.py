print("ODD number summation")

total = 0  # to store sum of odd numbers

for i in range(7):
    num = int(input("Enter a number: "))
    if num % 2 != 0:   # check if odd
        total += num

print(f"The sum of all odd numbers is {total}")