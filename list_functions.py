import json
import os


class JsonFile:
    def __init__(self):

        self.file_name = None

    def create_file(self, file_name=None):
        self.file_name = file_name
        self.file_name = input("Enter File Name:")
        if self.file_name is not None:
            if os.path.exists(f"{self.file_name}.json"):
                print("The file already exists!")
            else:
                with open(f"{self.file_name}.json", "w") as c:
                    name = input("Enter your name: ")
                    father_name = input("Enter your father's name: ")
                    reads_in = int(input("Enter the class in which you read: "))
                    semester = int(input("Enter your current semester: "))
                    python_data = {"Name": name, "Father Name": father_name, "Class": reads_in, "Semester": semester}
                    json.dump(python_data, c, indent=4)
                    print("The file is created ")

    def show_data(self):
        if os.path.exists(self.file_name + ".json"):
            try:
                with open(self.file_name + ".json", "r") as o:
                    data = json.load(o)
                    print(data)
            except:
                print("The file is empty!")
        else:
            print("The File does not exist")

    def replace_data(self):
        if os.path.exists(self.file_name + ".json"):
            with open(self.file_name + ".json", "r") as file:
                python_data = json.load(file)
                replace = input("What do you want to update?\n1.Name\n2.Father's name\n3.Class\n4.Semester >")

            if replace == "1":
                name = input("Enter new name: ")
                python_data["Name"] = name
            elif replace == "2":
                father_name = input("Enter new name: ")
                python_data["Father Name"] = father_name
            elif replace == "3":
                read_in = int(input("Enter the class in which you read: "))
                python_data['Class'] = read_in
            elif replace == "4":
                semester = int(input("Enter your current semester: "))
                python_data["Semester"] = semester
            else:
                print("Invalid number!")
            with open(self.file_name + ".json", "w") as file:
                json.dump(python_data, file, indent=4)
        else:
            print("The File does not exists!")

    def delete_file(self):
        if os.path.exists(self.file_name + ".json"):
            os.remove(self.file_name + ".json")
            print("The file has been deleted!")
        else:
            print("There is no such file!")

    def printing_list(self):
        print(
            "\n1.Create File\n2.Show the data\n3.Replace the data\n4.Delete the file\n5.Quit")


j1 = JsonFile()
j1.printing_list()
while True:
    choose = int(input("What function do you want to perform? "))
    match choose:

        case 1:
            j1.create_file()
            j1.printing_list()

        case 2:
            j1.show_data()
            j1.printing_list()

        case 3:
            j1.replace_data()
            j1.printing_list()

        case 4:
            j1.delete_file()
            j1.printing_list()

        case 5:
            print("The process Ended!")
            break
