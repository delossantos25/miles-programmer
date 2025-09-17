num = eval(input("Input a number: "))
print("Multiplication table for",num,":")

for y in range(1,11,1):
    print(num,"x",y,"=",num * y)