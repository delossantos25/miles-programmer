import os
import json

print("Student information system")

#Empty Dictionary

student_record = {}

while True:
    print("SELECT  FROM THE FOLLOWING OPTION")
    print("A - Add Student Record")
    print("B - Print All Student Record")
    print("C - Search Student Record")
    print("D - Delete Student Record")
    print("E - Edit Student Record")
    print("F - Export Student Record")
    print("G - Exit System")

    option = input("SELECT FROM THE OPTIONS ABOVE ---> ").lower()

    if option == 'a':
        os.system('cls')

        print('\nADDING STUDENT RECORD')

        id_no = input('Please Input Studend ID Number ---> ')

        first_name = input('Please input student name ---> ').upper()
        last_name = input('Please input student last name ---> ').upper()
        age = eval(input('Please input student age ---> '))
        course = input('Please input student course ---> ').upper()
        section = input('Please input student section ---> ').upper()
        #STORING DATA INTO DICTIONARY - student_record
        student_record[id_no] =[first_name, last_name, age, course, section]
        print('DATA SAVED SUSCESSFULLY')
        #go back to the original menu
        continue

    elif option == 'b':
        os.system('cls')
        print('PRINTING STUDENT RECORD')
        #print (student_record) simpe approach
        for i, j in student_record.items(): #key - values
            print(f"STUDENT ID - {i}, INFORMATION - {j}")
            continue

    elif option == 'c':
        os.system('cls')

        print('SEARCH STUDENT RECORD')

        search_id = input('Input student ID for search --> ').lower()

        for each in student_record.keys():
            if search_id in student_record.keys():
                print('----------------------')
                print(f' RECORD FOUND for ID {search_id}')
                #To print the record for the search ID
                for i in student_record[search_id]:
                    print(f' -- {i}')
                print('----------------------')
            else:
                print('NO RECORD FOUND')
            break
        continue


    elif option == 'd':
        os.system('cls')

        print('SEARCH STUDENT RECORD')

        search_id = input('Input student ID for search --> ').lower()

        for each in student_record.keys():
            if search_id in student_record.keys():
                print('----------------------')
                print(f' RECORD FOUND for ID {search_id}')
                #To print the record for the search ID
                for i in student_record[search_id]:
                    print(f' -- {i}')
                print('----------------------')
                student_record.pop(search_id)
                print('RECORD DELETED')
            else:
                print('NO RECORD FOUND')
            break
        continue

    elif option == 'e':
        os.system('cls')

        search_id = input('Input student ID for search --> ').lower()

        for each in student_record.keys():
            if search_id in student_record.keys():
                print('----------------------')
                print(f' RECORD FOUND for ID {search_id}')
                #To print the record for the search ID
                for i in student_record[search_id]:
                    print(f' -- {i}')
                print('----------------------')
                break

        #New set of value for the searched ID
        first_name = input('Please input student name ---> ').upper()
        last_name = input('Please input student last name ---> ').upper()
        age = eval(input('Please input student age ---> '))
        course = input('Please input student course ---> ').upper()
        section = input('Please input student section ---> ').upper()

        student_record[search_id][0] = first_name
        student_record[search_id][1] = last_name
        student_record[search_id][2] = age
        student_record[search_id][3] = course
        student_record[search_id][4] = section

        print('DATA UPDATED')
        continue


    elif option == 'f':
        os.system('cls')

        print('EXPORT STUDENT DATA')
        #json JAVA SCRIPT OBJECT NATION
        with open ('student_record.json', 'w') as new_file:
            json.dump(student_record, new_file, indent=4)

        print('DATA EXPORTED TO JSON')
        continue
    elif option == 'g':
        print('SYSTEM EXIT!')
        break
    else:
        print('INVALID CHOICE, SELECT AGAIN')
