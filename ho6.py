import openpyxl as op
work_book = op.Workbook()
sheet = work_book.active


sheet["a1"] = "Id"
sheet["b1"] = "First Name"
sheet["c1"] = "Last Name"
sheet["d1"] = "Birth Year"
sheet["e1"] = "Age"

for i in range(1,4):
    print(f"Person {i}")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    birth_year = int(input("Enter your birth year: "))
    age = 2026 - birth_year

    sheet["a"+str(1+i)] = i
    sheet["b"+str(1+i)] = first_name
    sheet["c"+str(1+i)] = last_name
    sheet["d"+str(1+i)] = birth_year
    sheet["e"+str(1+i)] = age
work_book.save("people.xlsx")

for data in sheet.iter_rows(values_only=True):
    print(data)
