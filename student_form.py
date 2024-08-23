import json
import os

file_name = "student form"
registration_file = "registration form"


class StudentData:

    def registration(self):
        if os.path.exists(registration_file):
            print("The File already exists!")
        else:
            with open(registration_file + ".json", "w") as f:
                student_id = int(input("Enter student id: "))
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                date_of_birth = input("Enter date of birth: ")
                gender = input("Enter your Gender: ")
                email = input("Enter your email address: ")
                address = input("Enter your address: ")

                registration_form = {
                    "registration_form": dict(student_id=student_id, first_name=first_name, last_name=last_name,
                                              date_of_birth=date_of_birth, gender=gender, email=email,
                                              address=address)}
                json.dump(registration_form, f, indent=4)
                print("You have registered yourself successfully!")

    def student(self):
        if os.path.exists(file_name):
            print("The file already exists!")
        else:
            with open(file_name + ".json", "w") as s:
                name = input("Enter your name: ")
                father_name = input("Enter your father's name: ")
                phone_number_1 = int(input("Enter first phone number: "))
                phone_number_2 = int(input("Enter second phone number: "))
                student_form = {"student_form": {"Name": name, "Father Name": father_name,
                                                 "Phone Number": [phone_number_1, phone_number_2]}}
                json.dump(student_form, s, indent=4)
            print("You have filled student form successfully!")

    def update(self):
        select = int(input("What form do you want to update?\n1.Registration form\n2.Student form\n>"))
        if select == 1:
            if os.path.exists(registration_file + ".json"):
                with open(registration_file + ".json", "r") as registration_data:
                    registration_update = json.load(registration_data)
            while True:
                replace = int(
                    input("What do you want to update in the registration file?\n1.student id\n2.first name\n3.last "
                          "name\n4.date of birth\n5.gender\n6.email\n7.address\n8.Do you want to exit?\n>"))

                if replace == 1:
                    student_id = int(input("Enter new student id: "))
                    registration_update["registration_form"]["student_id"] = student_id
                elif replace == 2:
                    first_name = input("Enter new first name: ")
                    registration_update["registration_form"]["first_name"] = first_name
                elif replace == 3:
                    last_name = input("Enter new last name: ")
                    registration_update["registration_form"]["last_name"] = last_name
                elif replace == 4:
                    date_of_birth = input("Enter new date of birth: ")
                    registration_update["registration_form"]["date_of_birth"] = date_of_birth
                elif replace == 5:
                    gender = input("Enter your gender: ")
                    registration_update["registration_form"]["gender"] = gender
                elif replace == 6:
                    email = input("Enter new email: ")
                    registration_update["registration_form"]["email"] = email
                elif replace == 7:
                    address = input("Enter new address: ")
                    registration_update["registration_form"]["address"] = address

                elif replace == 8:
                    with open(registration_file + ".json", "w") as r:
                        json.dump(registration_update, r, indent=4)
                    print("The registration form is updated!")
                    break

        elif select == 2:
            if os.path.exists(file_name + ".json"):
                with open(file_name + ".json", "r") as file:
                    student_update = json.load(file)
                while True:
                    selection = int(input("What do you want to update?\n1.Name\n2.Father's name\n3.Phone "
                                          "number_1\n4.Phone"
                                          "number_2\n5.Do you want to exit?\n>"))
                    if selection == 1:
                        new_name = input("Enter new name: ")
                        student_update["student_form"]["Name"] = new_name
                    elif selection == 2:
                        father_name = input("Enter father's name: ")
                        student_update["student_form"]["Father Name"] = father_name
                    elif selection == 3:
                        phone_number_01 = int(input("Enter new phone number 01: "))
                        student_update["student_form"]["Phone Number"][0] = phone_number_01
                    elif selection == 4:
                        phone_number_02 = int(input("Enter new phone number 02: "))
                        student_update["student_form"]["Phone Number"][1] = phone_number_02
                    elif selection == 5:
                        print("The student form is updated!")
                        with open(file_name + ".json", "w") as d:
                            json.dump(student_update, d, indent=4)
                        break
                    else:
                        print("Invalid number!")

        else:
            print("Invalid number!")


s = StudentData()


def main():
    student_data = StudentData()

    while True:
        choice = int(input("What do you want to fill?\n1.Registration Form\n2.Student Form\n> "))

        if choice == 1:
            student_data.registration()
            if int(input("Do you also want to fill out the student form?\n1.Yes\n2.No\n> ")) == 1:
                student_data.student()

        elif choice == 2:
            student_data.student()
            if int(input("Do you also want to fill out the registration form?\n1.Yes\n2.No\n> ")) == 1:
                student_data.registration()

        else:
            print("Invalid number!")
            continue

        if int(input("Do you want to update any form?\n1.Yes\n2.No\n> ")) == 1:
            student_data.update()

        print("Take care!")
        break


if __name__ == "__main__":
    main()
