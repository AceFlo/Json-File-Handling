import os


class FileMaking:
    def create_file(self, ):
        if os.path.exists("myfile.txt"):
            print("The file already exist: ")
        else:
            file = open("myfile.txt", "x")
            file.close()

    def write_in_file(self):
        file = open("myfile.txt", "w")
        file.write(input(" what you want to write in file" )+ "\n")
        file.close()

    def show_file(self):
        file = open("myfile.txt", "r")
        view = file.read()
        print(view)
        file.close()

    def delete_file(self):
        if os.path.exists("myfile.txt"):
            os.remove("myfile.txt")
            print("File has been deleted")
        else:
            print("There is no such file!")

    def check_line(self):
        x = open("myfile.txt")
        for line in x:
            if line.startswith(input(" what you want to search? ").lower()):
                print(line)

    def update_file(self):
        y = open("myfile.txt", "a")
        y.write(input("What do you want to enter in the file? ") + "\n")
        y.close()

f1 = FileMaking()
print("""
>List of Functions:
1.create file
2.write in file
3.show the contents in file
4.delete file
5.print specific content
6.update file
7.exit
""")
while True:
     choose=int(input("what function you want to be executed? "))

     if (choose==1):
         f1.create_file()
         print("""
         >List of Functions:
         2.write in file
         3.show the contents in file
         4.delete file
         5.print specific content
         6.update file
         7.exit
         """)

     elif(choose==2):
         try:
             f1.write_in_file()
             print("""
             >List of Functions:
             1.create file
             3.show the contents in file
             4.delete file
             5.print specific content
             6.update file
             7.exit
             """)
         except FileNotFoundError:
             print("Create a file first!")

     elif(choose==3):
         try:
             f1.show_file()
             print("""
             >List of Functions:
             1.create file
             2.write in file
             4.delete file
             5.print specific content
             6.update file
             7.exit
             """)
         except FileNotFoundError:
             print("Create a file first")

     elif(choose==4):
        try:
         f1.delete_file()
         print("""
         >List of Functions:
         1.create file
         2.write in file
         3.show the contents in file
         5.print specific content
         6.update file
         7.exit
         """)
        except FileNotFoundError:
            print("The file is deleted!")

     elif(choose==5):
         try:
             f1.check_line()
             print("""
             >List of Functions:
             1.create file
             2.write in file
             3.show the contents in file
             4.delete file
             6.update file
             7.exit
             """)
         except FileNotFoundError:
             print("File is deleted!")

     elif(choose==6):
         try:
             f1.update_file()
             print("""
             >List of Functions:
             1.create file
             2.write in file
             3.show the contents in file
             4.delete file
             5.print specific content
             7.exit
             """)
         except FileNotFoundError:
             print("File is deleted")

     elif(choose==7):
         break

     else:
         print("invalid choice: ")