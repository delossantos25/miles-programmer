fname = 'miles'
mname = 'luis'
lname = 'de los santos'

print(f"My name is {fname.upper()} {mname.upper()} {lname.upper()}")

sum = 0
for i in range(1,6,1):
    x = eval(input(f"{i} input any number ---> "))
    sum += x
print(f"The sum of all the number given is {sum}")