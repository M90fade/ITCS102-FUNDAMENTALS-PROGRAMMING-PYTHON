import os
import json
os.system('cls')
print("STUDENT INFORMAITON SYSTEM")
print('----------------------------------')

#empty dictionary/storage
student_records = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW")
    print("A - Add Information \nB - Print Student Record \nC - Search a Record")
    print("D - Delete a Record \nE - Modify a Record \nF - Export Record")
    print("G - Import Record \nX - Exit the program")
    print("=======================================================")

    choice = input("Your choice --> ").lower()

#Adding information
    if choice == 'a':
        print("ADDING STUDENT INFORMATION")
        print("----------------------------------")
        search_code = input("Key search for this student ")
        first_name = input("Input Student First Name --> ").upper()
        last_name = input("Input Student Last Name --> ").upper()
        course = input("Input Student course --> ").upper()
        email = input("Input student email address --> ")
        student_records = {search_code : [first_name, last_name, course, email] }

        print("DATA SAVED")
        os.system('cls')
        continue
#Printing 
    elif choice == 'b':
        print("PRINTING STUDENT RECORD ")
        print("=============================")

        for id, records in student_records.items():
            print(f"STUDENT ID {id} in STUDENT RECORD {records}")
        continue
# Searching
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD ")
        print("============================")

        search_id = input("Input ID to search --> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("====================================")
                print("\n\nRECORD FOUND")
                print("====================================")
            else:
                print("==============================")
                print("NO RECORD FOUND")
                print("==============================")
        continue
    elif choice == 'd':
        os.system('cls')
        print("DELETE EXISTING RECORD ")
        print("============================")

        search_id = input("Input ID to search --> ").lower()
        if search_id in student_records.keys():
            print("====================================")
            print("\n\nRECORD FOUND")
            print("====================================")
            #print the record of search student
            for i in student_records[search_id]:
                print(f"-- {i}")
            
            student_records.pop(search_id)
            print("RECORD DELETED")
        else:
            print("==============================")
            print("NO RECORD FOUND")
            print("==============================")
        continue
    elif choice == 'e':
        os.system('cls')
        print("EDIT / MODIFY STUDENT RECORD ")
        print("===============================")

        search_id = input("Input ID to search --> ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("====================================")
                print("\n\nRECORD FOUND")
                print("====================================")
                #print the record of search student
                for i in student_records[search_id]:
                    print(f"-- {i}")
                
                first_name = input("Input NEW Student First Name --> ").upper()
                last_name = input("Input NEW Student Last Name --> ").upper()
                course = input("Input NEW Student Course --> ").upper()
                email = input("Input NEW Student Email --> ")

                student_records[search_id][0] = first_name
                student_records[search_id][1] = last_name
                student_records[search_id][2] = course
                student_records[search_id][3] = email

                print("DATA UPDATED")

            else:
                print("=======================================")
                print("NO RECORD FOUND")
                print("=======================================")
        continue
    elif choice == 'f':
        os.system('cls')
        print("Export Student Record")
                #file name , read / write
        with open('student_records.json', 'w') as new_file:
            json.dump(student_records, new_file, indent=4)

        print("DATA EXPORTED TO JSON")

        continue

    elif choice == 'g':
        os.system('cls')
        print("Import Student Record")
                #file name , read / write
        with open('student_records.json', 'r') as new_file:
            student_json = json.load(new_file)

        student_records = student_json
        print("DATA IMPORTED TO JSON")

        continue

    elif choice == 'x':
        print("System Exit")
        break

    else:
        print("\nINVALID CHOICE, please RE-ENTER YOUR CHOICE ")
        continue