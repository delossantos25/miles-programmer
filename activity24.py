# Creating or defining your own function
# Code reusability
# Keyword -- def

def GreetPersonName(name):
    print(f"\nHi {name}, welcome to my first function")
    print("Please browse around")

def GreetInfo(name, place, age):
    print(f"Name: {name}")
    print(f"Place: {place}")
    print(f"Age: {age}")

while True:
    print("\nCode compiler program")
    print("A - First Program \nB - Second Program \nC - Exit")
    choice = input("Select from the option --> ").lower()

    if choice == 'a':
        GreetPersonName("Miles")
        continue

    elif choice == 'b':
        GreetInfo("Miles", "Sariaya", "20")
        continue

    elif choice == 'c':
        print("System Exit")
        break

    else:
        print("Invalid Choice. Try again.")
        continue
