import json
import os


class FileMaking:
    def file_creation(self):
        if os.path.exists("myfile2.json"):
            print("File already exists!")
        else:
         open("myfile2.json","x")

    def file_write(self):
       w= open("myfile2.json","w")
       w.write(input("what you want to write? \n"))
       w.close()

    def file_show(self):
        with open("myfile2.json","r") as s:
           content= s.read()
           print(content)

    def file_delete(self):
        if os.path.exists("myfile2.json"):
            os.remove("myfile2.json")
            print("File has been deleted")
        else:
            print("There is no such file!")



f1=FileMaking()
f1.file_creation()
f1.file_write()
f1.file_show()
