name = input("Whats your name ---> ")
isStudent = input("Are you a student? (yes or no) ---> ")

if isStudent.lower() == "yes":
    print("Congrats your eligible for student discount", name)
    fare = 20 * .2
    new_fare = 20 - fare
    print("Congrats your eligible for student discount your fare is ", new_fare)
    bayad = eval(input("Enter your bayad ---> "))
else:

    print("Sorry, your not eligible for student discount", name, ":<")
