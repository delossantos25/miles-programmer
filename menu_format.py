import os
from menu_lessons import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# main menu 
def main_menu():
    while True:
        clear()
        # Main Menu Title with Emojis
        print("        💻 MAIN MENU 💡")
        print("1. Basics 📘")
        print("2. Operators ➕➖")
        print("3. Conditionals ❓")
        print("4. Loops 🔁")
        print("5. Lists & Functions 📦⚙️")
        print("0. Exit 🚪")
        print("-----------------------------")

        pick = input("Select option (0-5): ").strip()

        if pick == '1':
            basics_menu()
        elif pick == '2':
            operators_menu()
        elif pick == '3':
            conditionals_menu()
        elif pick == '4':
            loops_menu()
        elif pick == '5':
            lists_functions_menu()
        elif pick == '0':
            clear()
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice.")
            input("Press Enter...")


# menu ng basics nyaknyaknyak
def basics_menu():
    while True:
        clear()
        # Basics Menu Title with Emojis
        print("       📘 BASICS 📜")
        print("1. Print Statements")
        print("2. Input & Variables")
        print("3. Escape Sequences")
        print("4. Length")
        print("5. Eval, Int, Str, Float, Type")
        print("0. Back 🔙")
        print("-----------------------------")

        pick = input("Choose: ").strip()

        if pick == '1': prints()
        elif pick == '2': inputs()
        elif pick == '3': escape_sequences()
        elif pick == '4': length()
        elif pick == '5': evals()
        elif pick == '0': break
        else:
            print("Invalid.")
            input("Press Enter...")


# operator basta
def operators_menu():
    while True:
        clear()
        # Operators Menu Title with Emojis
        print("       ➕➖ OPERATORS 🧮")
        print("1. Arithmetic")
        print("2. Assignment")
        print("3. Comparison")
        print("4. Logical")
        print("0. Back 🔙")
        print("-----------------------------")

        pick = input("Choose: ").strip()

        if pick == '1': arithmetic()
        elif pick == '2': assignment()
        elif pick == '3': comparison()
        elif pick == '4': logical()
        elif pick == '0': break
        else:
            print("Invalid.")
            input("Press Enter...")

# Conditionals ket ano
def conditionals_menu():
    while True:
        clear()
        # Conditionals Menu Title with Emojis
        print("       ❓ CONDITIONALS 🚦")
        print("1. If/Elif/Else")
        print("2. Nested")
        print("3. Combining Conditions")
        print("0. Back 🔙")
        print("-----------------------------")

        pick = input("Choose: ").strip()

        if pick == '1': if_elif_else()
        elif pick == '2': nested()
        elif pick == '3': combining()
        elif pick == '0': break
        else:
            print("Invalid.")
            input("Press Enter...")


# Loops blahblah
def loops_menu():
    while True:
        clear()
        # Loops Menu Title with Emojis
        print("        🔁 LOOPS ⏳")
        print("1. For Loops")
        print("2. While Loops")
        print("3. Nested Loops")
        print("4. Loop Control")
        print("0. Back 🔙")
        print("-----------------------------")

        pick = input("Choose: ").strip()

        if pick == '1': for_loops()
        elif pick == '2': while_loops()
        elif pick == '3': nested_loops()
        elif pick == '4': loop_control()
        elif pick == '0': break
        else:
            print("Invalid.")
            input("Press Enter...")


# List and Function kinemerut
def lists_functions_menu():
    while True:
        clear()
        # Lists & Functions Menu Title with Emojis
        print("      📦⚙️ LISTS & FUNCTIONS 🔗")
        print("1. Lists")
        print("2. Functions")
        print("3. Def / Define")
        print("4. Importing Random")
        print("5. Dictionaries")
        print("0. Back 🔙")
        print("-----------------------------")

        pick = input("Choose: ").strip()

        if pick == '1': lists()
        elif pick == '2': functions()
        elif pick == '3': defs()
        elif pick == '4': importing_random()
        elif pick == '5': dictionaries()
        elif pick == '0': break
        else:
            print("Invalid.")
            input("Press Enter...")


# Start Program
main_menu()